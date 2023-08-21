class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chaMap = {}
        for cha in magazine:
            if cha in chaMap:
                chaMap[cha] +=1
            else:
                chaMap[cha] = 1
        checkFlag = True
        for cha in ransomNote:
            if cha in chaMap and chaMap[cha] >= 1:
                chaMap[cha] -=1;
            else:
                checkFlag = False
                break;
        return checkFlag