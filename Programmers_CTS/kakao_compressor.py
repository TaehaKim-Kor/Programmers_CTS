import math
def kakao_compressor(s):
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
    
    answer = 1001
    print(s)
    print(answer_sheet)
    for i in range(len(answer_sheet)):        
        if len(answer_sheet[i]) < answer:
            answer = len(answer_sheet[i])
    print(answer)
    return answer