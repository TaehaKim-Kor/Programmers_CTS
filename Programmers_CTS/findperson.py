def findperson(n, lost, reserve):
    list = [0 for x in range(n+2)]
    myerror = 0
    for i in range(max(len(lost),len(reserve))):
        if i < len(lost):
            list[lost[i]] -= 1
        if i < len(reserve):
            list[reserve[i]] += 1
    for x in range(1,n+1):
        if list[x] == -1:
            if list[x+1] == 1:
                list[x] += 1
                list[x+1] -= 1
            elif list[x-1] == 1:
                list[x] += 1
                list[x-1] -= 1
            else:
                myerror +=1
    answer = n - myerror
    return answer
#https://programmers.co.kr/learn/courses/30/lessons/42862