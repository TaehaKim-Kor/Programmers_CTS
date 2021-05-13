#https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
import math
def compressor(w,h):
    for i in range(2,math.floor(min(w/2,h/2))):
        if w % i == 0 and h % i == 0:
            return int(w/i),int(h/i),True
    return w,h,False
def Euclidean_compressor(w,h):
    #https://coding-factory.tistory.com/599
    if min(w,h) == 0:
        return int(max(w,h))
    else:
        return Euclidean_compressor(min(w,h),max(w,h)%min(w,h))
def finder(w,h):
    grad = w/h
    minus = 0
    for i in range(1,h):
        minus += w-math.ceil(grad*i)
    return w*h-minus*2
def solution(w,h):
    state=1
    ow , oh = w , h
    answer = ow*oh
    if state == 0:
        s = True
        while(s):
           w,h,s=compressor(w,h)
        answer -= int(finder(w,h))*int(ow/w)
    else:
        ratio = Euclidean_compressor(w,h)
        answer -= int(finder(int(w/ratio),int(h/ratio)))*int(ratio)
    return answer