class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        addno = (int(num1), int(num2))
        
        sum = addno[0] + addno[1]
        
        return str(sum)