import findperson as fp
import find_comb_prime as fcp
import network as nl
import rotating as rt
import pair_remove as pr
import perfect_rectangle as pr2
#fp.findperson(5,[2,4],[1,3,5])
#fcp.findcomb([1,2,3,4])
#fcp.findcomb([1,2,7,6,4])
# print(fcp.findcomb([1,2,3,4]))
# print(fcp.findcomb([1,2,7,6,4]))
# print(nl.netlink(3,[[1,1,0],[1,1,0],[0,0,1]]))
# print(rt.map_rotating(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(rt.map_rotating(100,97,[[1,1,100,97]]))
print(pr.solution("baabaa"))
print(pr.solution("cdcd"))
print(pr.solution("abccba"))
print(pr.solution("abcccba"))
print(pr.solution("abccccbaaa"))
print(pr.solution("abccaabaa"))
print(pr.solution("a"))

print(pr2.solution(8,12))