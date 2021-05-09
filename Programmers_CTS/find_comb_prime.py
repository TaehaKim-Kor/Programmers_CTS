#https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
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
        visit[current_position] = 0 #여기선 visit 초기화를 해야되는데 network 문제에선 왜 안해도 됬는 지를 모르겠다..
    elif trial == 3:
        tgt = tgt_adder(numlist, visit)
        if primenum_classifier(tgt):
            ans = []
            for j in range(len(visit)):
                if visit[j] == 1:
                    ans.append(numlist[j])
            anslist.append(ans)
        visit[current_position] = 0
                
def findcomb(nums):
    answer_list = []
    for i in range(len(nums)):
        visit_list = [0 for i in range(len(nums))]
        dwsearcher(nums,visit_list,answer_list,i)
    answer_list = refiner(answer_list)
    answer = len(answer_list)
    return answer