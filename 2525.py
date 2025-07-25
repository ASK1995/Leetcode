class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        bulky, heavy = False, False

        if(length >= 10**4) or (width >= 10**4) or (height >= 10**4) or (volume >= 10**9):
            bulky = True
        if(mass >= 100):
            heavy = True
        if(bulky and heavy):
            return "Both"
        elif(bulky):
            return "Bulky"
        elif(heavy):
            return "Heavy"
        else:
            return "Neither"