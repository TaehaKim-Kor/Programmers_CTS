def solution(dartResult):
    answer = 0
    scoretype = []
    bonustype = []
    optiontype = [0,0,0] # 0 = no option, 1 = *, 2 = #
    resulttype = [0,0,0] # result type saving
    junction = []
    for i in range(len(dartResult)):
        try :
            int(dartResult[i])
            junction.append(dartResult[i])
        except :
            if len(junction) > 0:
                strscore = ""
                for k in range(len(junction)):
                    strscore += junction[k]
                scoretype.append(int(strscore))
                junction = []
            if dartResult[i] == "S": bonustype.append("S")
            elif dartResult[i] == "D": bonustype.append("D")
            elif dartResult[i] == "T": bonustype.append("T")
            if dartResult[i] == "*": optiontype[len(scoretype)-1] = 1
            elif dartResult[i] == "#": optiontype[len(scoretype)-1] = 2
    for i in range(3):
        power=0
        if bonustype[i] == "S":
            power = 1
        elif bonustype[i] =="D":
            power = 2
        elif bonustype[i] =="T":
            power = 3
        score = int(scoretype[i])**power
        resulttype[i]=score
    for i in range(3):
        if optiontype[i] == 1:
            resulttype[max(0,i-1)] *= 2
            if max(0,i-1) != i:
                resulttype[i] *= 2
        elif optiontype[i] == 2:
            resulttype[i] *= -1
    answer = sum(resulttype)
    return answer