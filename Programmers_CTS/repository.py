https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
def solution(lottos, win_nums):
    uc=7
    dc=7
    for tgt in lottos:
        if tgt != 0:
            try:
                win_nums.index(tgt)
                uc -= 1
                dc -= 1
            except:
                uc -= 0            
        else:
            uc -= 1
    if dc == 7: dc = 6
    if uc == 7: uc = 6
    answer = [uc,dc]
    return answer

https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        searched = array[int(commands[i][0])-1:int(commands[i][1])]
        searched.sort()
        answer.append(searched[int(commands[i][2]-1)])
    return answer

https://programmers.co.kr/learn/courses/30/lessons/42840
import numpy as np
def solution(answers):
    answer=[]
    list2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == i%5+1: ans[0] += 1
        if answers[i] == list2[i%len(list2)]: ans[1] +=1
        if answers[i] == list3[i%len(list3)]: ans[2] +=1
    tgt = np.max(ans)
    if tgt==ans[0]:
        answer.append(1)
    if tgt==ans[1]:
        answer.append(2)
    if tgt==ans[2]:
        answer.append(3)
    return answer

https://programmers.co.kr/learn/courses/30/lessons/60057
import math
def solution(s):
    answer_sheet = [s]
    for i in range(1,math.floor(len(s)/2)+1):
        tgt_ans = ""
        n=0
        flag = 0
        while(n<len(s)):
            tgt = str(s[n:n+i])
            if n == 0:
                cmp = str(s[n:n+i])
            else:
                if tgt == cmp:
                    flag += 1
                else:
                    if flag == 0:
                        tgt_ans = tgt_ans + cmp
                        cmp = str(s[n:n+i])
                    else:
                        tgt_ans = tgt_ans + str(flag+1) + cmp
                        cmp = str(s[n:n+i])
                        flag = 0
            if n+i>=len(s):
                if flag == 0:
                    tgt_ans = tgt_ans + cmp
                else:
                    tgt_ans = tgt_ans + str(flag+1) + cmp
                tgt_ans = tgt_ans + str(s[n+i:len(s)])
            n += i
            
        answer_sheet.append(tgt_ans)
    
    answer = len(answer_sheet[0])
    for i in range(1,len(answer_sheet)):        
        if len(answer_sheet[i]) < answer:
            answer = len(answer_sheet[i])
    return answer

https://programmers.co.kr/learn/courses/30/lessons/42860
charList =["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"]
def solution(name):
    tgt = []
    for i in range(len(name)):
        tgt.append("A") 
    count = 0
    ind = 0
    obj = [name[i] for i in range(len(name))]
    while(abs(ind) < len(name)):
        bef=tgt[ind]
        aft=obj[ind]
        count += abs(charList.index(bef)-charList.index(aft))
        tgt[ind] = aft
        if tgt == obj:
            return(count)
        sind = 1
        while(sind < len(obj)):
            if tgt[ind+sind] != obj[ind+sind]:
                sind *= 1
                break
            elif tgt[ind-sind] != obj[ind-sind]:
                sind *= -1
                break
            else:
                sind += 1
        ind += sind
        count += abs(sind)

https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            try: answer.index(numbers[i]+numbers[j])
            except: answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
def solution(a, b):
    Month = [31, 29, 31, 30 ,31 , 30 , 31, 31, 30, 31, 30]
    Answer = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    day=0
    if a > 1:
        for i in range(a-1):
            day += int(Month[i])
    day += b
    answer = str(Answer[day % 7])
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s) % 2 == 0:https
        answer=s[len(s)//2-1]+s[len(s)//2]
    else:
        answer=s[len(s)//2]
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer=[]
    tgt="A"
    for i in range(len(arr)):
        if arr[i]!=tgt:
            answer.append(arr[i])
            tgt = arr[i]    
    return answer

https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    list = [0 for x in range(n+2)]
    myerror = 0
    for i in range(max(len(lost),len(reserve))):
        if i < len(lost):
            list[lost[i]] -= 1
        if i < len(reserve):
            list[reserve[i]] += 1
    for x in range(n+1):
        if list[x] == -1:
            if list[x+1] == 1:
                list[x] += 1
                list[x+1] -= 1
            elif list[x-1] == 1 and x>0:
                list[x] += 1
                list[x-1] -= 1
            else:
                myerror +=1
    answer = n - myerror
    return answer

https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

https://programmers.co.kr/learn/courses/30/lessons/67256
import numpy as np
def position(num):
    if num == 0:
        return [4,2]
    else:
        A = np.linspace(1,9,9)
        B = np.reshape(A,(3,3))
        C = np.where(B==num)
        answer = []
        for i in range(2):
            tgt = int(C[i])
            answer.append(tgt+1)
        return answer

def distance(lpos,rpos,htype,pos):
    if pos[1]==1:
        return "L"
    elif pos[1]==3:
        return "R"
    ld = 0
    rd = 0
    for i in range(2):
        ld += abs(lpos[i]-pos[i])
        rd += abs(rpos[i]-pos[i])
    if ld > rd:
        return "R"
    elif ld < rd:
        return "L"
    else:
        if htype == "left":
            return "L"
        else:
            return "R"
        
def solution(numbers, hand):
    answer = ''
    pl = [4,1]
    pr = [4,3]
    for i in numbers:
        tgt=position(i)
        decision = distance(pl,pr,hand,tgt)
        answer += decision
        if decision == "L":
            pl = tgt
        else:
            pr = tgt
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12977
def primenum_classifier(tgt):
    if tgt == 1:
        return True
    else:
        for i in range(2,tgt):
            if tgt % i == 0:
                return False
    return True

def trial_counter(visit):
    return sum(visit)

def tgt_adder(numlist, visit):
    tgt = 0
    for i in range(len(visit)):
        if visit[i] == 1:
            tgt += numlist[i]
    return tgt

def refiner(tgtlist):
    refine_anslist = []
    for i in range(len(tgtlist)):
        try:
            refine_anslist.index(tgtlist[i])
        except:
            refine_anslist.append(tgtlist[i])
    return refine_anslist
    
def dwsearcher(numlist, visit, anslist, current_position):
    visit[current_position] = 1
    trial = trial_counter(visit)
    if trial < 3:
        for j in range(len(visit)):
            if visit[j] == 0:
                dwsearcher(numlist,visit,anslist,j)  
        visit[current_position] = 0
    elif trial == 3:
        tgt = tgt_adder(numlist, visit)
        if primenum_classifier(tgt):
            ans = []
            for j in range(len(visit)):
                if visit[j] == 1:
                    ans.append(numlist[j])
            anslist.append(ans)
        visit[current_position] = 0
                
def solution(nums):
    answer_list = []
    for i in range(len(nums)):
        visit_list = [0 for i in range(len(nums))]
        dwsearcher(nums,visit_list,answer_list,i)
    answer_list = refiner(answer_list)
    answer = len(answer_list)
    return answer

https://programmers.co.kr/learn/courses/30/lessons/77485
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
        
def solution(rows, columns, queries):
    answer = []
    mymat = mapping(rows,columns)
    for i in range(len(queries)):
        mymat, minimum= rotation(mymat,queries[i])
        answer.append(minimum)
    return answer

https://programmers.co.kr/learn/courses/30/lessons/43162
def searcher(net,link,visit,ll,current):
    visit[current]=1
    link.append(current)
    flag = 0
    for i in range(len(net[current])):
        if visit[i] == 0 and net[current][i] == 1 and i != current:
            flag = 1
            searcher(net,link,visit,ll,i)
    if flag == 0:
        #print("============")
        #print(link)
        #print(visit)
        #print(ll)
        #print("============")
        link.sort()
        for i in range(len(ll)):
            if ll[i] == link:
                flag = 1
                break
        if flag == 0:
            ll.append(link)

def solution(n, computers):
    linklist = []
    for i in range(n):
        myvisit = [0 for i in range(n)]
        mylink = []
        searcher(computers,mylink,myvisit,linklist,i)
    #print(linklist)
    refinelinklist = []
    for i in range(len(linklist)):
        flag = 0
        for j in range(len(refinelinklist)):
            if linklist[i] == refinelinklist[j]:
                flag = 1
        if flag == 0:
            refinelinklist.append(linklist[i])
    answer = len(refinelinklist)
    return answer

https://programmers.co.kr/learn/courses/30/lessons/42747
import numpy as np
def solution(citations):
    answer=0
    for i in range(np.max(citations)):
        if np.sum(np.where(np.array(citations)>=i,1,0))>=i:
            answer = i
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    forget = []
    count = [0 for i in range(n)]
    for i in range(len(words)):
        count[i%n] += 1
        if i != 0:
            tgt = forget[len(forget)-1]
        else:
            tgt = ""
        try:
            forget.index(words[i])
            return [i%n+1,count[i%n]]
        except:
            if i != 0 and tgt[len(tgt)-1] != words[i][0]:
                return [i%n+1,count[i%n]]
            else:
                forget.append(words[i])
    return [0,0]

https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for target in skill_trees:
        flag = 0
        if len(skill)==1:
            break
        for x in range(len(skill)-1):
            for y in range(x+1,len(skill)):
                try:
                    target.index(skill[x])
                    try:
                        target.index(skill[y])
                        if(target.index(skill[x])>target.index(skill[y])):
                            flag=1
                            break
                        else:
                            flag=0
                    except:
                        flag = 0
                except:
                    try:
                        target.index(skill[y])
                        flag = 1
                        break
                    except:
                        flag = 0
        #for x in range(len(skill)-1,0,-1):
        #    for y in range(x-1,-1,-1):
        #        try:
        #            if (target.index(skill[x])<target.index(skill[y])):
        #                flag = 1
        #                break
        #        except:
        #            try:
        #                target.index(skill[y])
        #            except:
        #                flag = 1
        #                break
            if flag == 1:
                answer += 1
                break
    answer = len(skill_trees) - answer
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        A=arr[i]
        if A % divisor ==0:
            try: answer.index(A)
            except: answer.append(A)
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer=0
    if a==b:
        answer=a
    elif a==-b:
        answer=0
    else:
        for i in range(min(abs(a),abs(b)),max(abs(a),abs(b))+1):
            answer += i
        if a<0 and b<0:
            answer *= -1
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    answer =""
    mylist = [s[i] for i in range(len(s))]
    mylist.sort(reverse=True)
    for i in range(len(mylist)):
        answer += mylist[i]
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    answer = ""
    mylist = [str(n)[i] for i in range(len(str(n)))]
    mylist.sort(reverse=True)
    for i in range(len(mylist)):
        answer += mylist[i]
    return int(answer)

https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    myarr = arr.copy()
    myarr.sort()
    arr.remove(myarr[0])
    if len(arr) == 0: arr.append(-1)
    return arr

https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    p=0
    y=0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y += 1
    if p-y ==0:
        return True
    else:
        return False

https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            try:
                a=int(s[i])
            except:
                return False
    else:
        return False
    return True

https://programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])
    return answer

https://programmers.co.kr/learn/courses/30/lessons/12934
def solution(n):
    q= n**0.5
    if int(q)-q == 0:
        return((q+1)**2)
    else:
        return(-1)




