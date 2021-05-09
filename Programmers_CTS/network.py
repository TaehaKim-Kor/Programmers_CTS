#https://programmers.co.kr/learn/courses/30/lessons/43162
def netsearcher(net,link,visit,ll,current):
    visit[current]=1
    link.append(current)
    flag = 0
    for i in range(len(net[current])):
        if visit[i] == 0 and net[current][i] == 1:
            flag = 1
            netsearcher(net,link,visit,ll,i)
    if flag == 0:
        link.sort()
        for i in range(len(ll)):
            if ll[i] == link:
                flag = 1
                break
        if flag == 0:
            ll.append(link)

def netlink(n, computers):
    linklist = []
    for i in range(n):
        myvisit = [0 for i in range(n)]
        mylink = []
        netsearcher(computers,mylink,myvisit,linklist,i)
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