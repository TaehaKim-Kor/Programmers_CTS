#https://programmers.co.kr/learn/courses/30/lessons/77485
import numpy as np

def mapping(r,c):
    vec=np.linspace(1,r*c,r*c)
    mat=np.reshape(vec,[r,c])
    return mat

def rotation(mymap,q):
    for i in range(4):
        q[i] -= 1
    temp = np.copy(mymap[q[0]][q[1]])
    minimum = temp
    for j in range(q[0],q[2]): #straight up
        tgt = np.copy(mymap[j+1][q[1]])
        mymap[j][q[1]]=tgt
        if tgt < minimum:
            minimum = tgt
    
    for i in range(q[1],q[3]): #straight left
        tgt = np.copy(mymap[q[2]][i+1])
        mymap[q[2]][i]=tgt
        if tgt < minimum:
            minimum = tgt
    
    for j in range(q[2],q[0],-1): #straight down
        tgt = np.copy(mymap[j-1][q[3]])
        mymap[j][q[3]] = tgt
        if tgt < minimum:
            minimum = tgt
    
    for i in range(q[3],q[1],-1): #straight right
        tgt = np.copy(mymap[q[0]][i-1])
        mymap[q[0]][i]=tgt
        if tgt < minimum:
            minimum = tgt
    
    mymap[q[0]][q[1]+1]=temp
    return mymap , int(minimum)
        
def map_rotating(rows, columns, queries):
    answer = []
    mymat = mapping(rows,columns)
    for i in range(len(queries)):
        mymat, minimum= rotation(mymat,queries[i])
        answer.append(minimum)
    return answer