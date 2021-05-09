def primenum_classifier(tgt):
    if tgt == 1:
        return True
    else:
        for i in range(2,tgt-1):
            if tgt % i == 0:
                return False
    return True

def dwsearcher(numlist, visit, trial, tgt, anslist):
    if trial == 3:
        if primenum_classifier(tgt):
            ans = []
            for j in range(len(visit)):
                if visit[j] == 1:
                    ans.append(visit[j])
            anslist.append(ans)
    else:
        for i in range(len(numlist)):
            if visit[i] == 0:
                print(visit)
                tgt += numlist[i]
                visit[i] = 1
                trial += 1
                dwsearcher(numlist,visit,trial,tgt,anslist)        
            
def findcomb(nums):
    answer_list = []
    visit_list = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        current_trial = 1
        target = nums[i]
        visit_list[i] = 1
        dwsearcher(nums,visit_list,current_trial,target,answer_list)
    refine_anslist = []
    answer_list.sort()
    for i in range(len(answer_list)):
        try:
            refine_anslist.index(answer_list[i])
        except:
            refine_anslist.append(answer_list[i])
    answer = len(refine_anslist)
    return answer