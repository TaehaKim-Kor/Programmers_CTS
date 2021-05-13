#https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
import math
def compressor(w,h):
    for i in range(2,min(w,h)):
        if w % i == 0 and h % i == 0:
            return int(w/i),int(h/i),True
    return w,h,False
        
def finder(w,h):
    grad = w/h
    tgt = [0]
    minus = 0
    for i in range(h):
        tgt.append(grad*i)
    for i in range(1,len(tgt)):
        btgt = math.floor(tgt[i-1])
        atgt = math.floor(tgt[i])
        minus += atgt - btgt + 1
    return minus
def finder2(w,h):
    if w<h:
        return 2*h-2
    elif w>h:
        return 2*h-1
    else:
        return h
def solution(w,h):
    ow , oh = w , h
    answer = ow*oh
    s = True
    while(s):
        w,h,s=compressor(w,h)
    answer -= int(finder2(w,h))*int(ow/w)
    return answer