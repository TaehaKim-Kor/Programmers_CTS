# Temporal test
def solution0(v):
    pa = v #point_array
    answer = [0,0]
    for i in range(2):
        va = [] #void_array
        for j in range(3):
            va.append(pa[j][i])
        va.sort()
        if va[0] != va[1]:
            answer[i] += va[0]
        else:
            answer[i] += va[2]
    return answer

# test1
def checker(S, pattern):
    unique_p= ''.join(set(pattern))
    charlist = [0 for i in range(len(unique_p))]
    charcheck = [0 for i in range(len(unique_p))]
    divlist = [0 for i in range(len(unique_p))]
    for i in range(len(pattern)):
        for j in range(len(unique_p)):
            if pattern[i]==unique_p[j]: charcheck[j] += 1
    for i in range(len(S)):
        for j in range(len(unique_p)):
            if S[i]==unique_p[j]: charlist[j] += 1
    for i in range(len(unique_p)):
        divlist[i] = charlist[i]//charcheck[i]
    answer = min(divlist)
    return answer
def solution1(S, pattern):
    answer = 0
    for i in range(len(S)-len(pattern)+1):
        tgt = S[i:i+len(pattern)]
        answer += checker(tgt,pattern)
    return answer


# test2
def searcher2(tgt,al,fwl,wl,current):
    if len(tgt)==0:
        tgt.append(fwl[current])
    else:
        tgt.append(wl[current])
    print(tgt,len(tgt))
    if len(tgt) == 5:
        mychar = ''
        for i in range(5):
            mychar += tgt[i]
        al.append(mychar)
        tgt.pop()
    else:
        for i in range(len(wl)):
            print(current,i)
            searcher(tgt,al,fwl,wl,i)
            tgt.pop()
def solution2(word):
    alist = []
    fwordlist = ["A","E","I","O","U"]
    wordlist = ["","A","E","I","O","U"]
    count = 0
    tgt = []
    for i in range(len(fwordlist)):
        searcher2(tgt,alist,fwordlist,wordlist,i)
        tgt.pop()
    alist.sort()
    return alist.index(word)+1

# test3
def searcher(current, letter, visit, plist, k):
    visit[current] = 1
    if sum(visit) >= k:
        char = ''
        for i in range(len(visit)):
            if visit[i] == 1:
                char += letter[i]
        plist.append(char)
        visit[current]=0
    else:
        for i in range(current+1,len(letter)):
            searcher(i,letter,visit,plist,k)
            visit[i]=0
def solution(letters, k):
    visit = [0 for i in range(len(letters))]
    plist = []
    for i in range(len(letters)):
        searcher(i,letters,visit,plist,k)
        visit[i]=0
    plist.sort(reverse=True)
    return plist[0]