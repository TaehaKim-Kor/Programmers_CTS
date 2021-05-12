#https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

    
def stacker(s):
    if len(s) == 0:
        return True
    answer = [s[0]]
    flag = 0
    tgt = answer[len(answer)-1]
    for i in range(1,len(s)):
        print(tgt, s[i])
        if tgt != s[i] and flag == 0:
            answer.append(s[i]) 
            tgt = s[i]
        elif tgt != s[i] and flag == 1:
            answer.pop()
            flag = 0
            answer.append(s[i])
            tgt = s[i]
        else:
            flag = 1
        print(answer)
    if flag == 1: answer.pop()
    stack = ""
    for i in range(len(answer)):
        stack += answer[i]
    print(stack)
    if stack == s:
        return False
    else:
        return stack

def stacker2(s):
    if len(s) == 0:
        return True
    answer = [s[0]]
    tgt = answer[len(answer)-1]
    for i in range(1,len(s)):
        if tgt != s[i]:
            answer.append(s[i]) 
            tgt = s[i]
        else:
            answer.pop()
            if len(answer)>0:
                tgt = s[i-2]
            else:
                tgt = ""
    stack = ""
    for i in range(len(answer)):
        stack += answer[i]
    if stack == s:
        return False
    else:
        return stack
        

def solution(s):
    while(True):
        s=stacker2(s)
        if s == True:
            return 1
        if s == False:
            return 0