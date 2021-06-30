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
def solution1():
    answer =[]
    return answer


# test2
def solution2():
    answer =[]
    return answer



# test3
def solution3():
    answer =[]
    return answer




    