class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc, dec = 0, len(arr) - 1
        if(len(arr) < 3):
            return False
        while(inc + 1 <= dec and arr[inc + 1] > arr[inc]):
            inc += 1
        while(dec - 1 > 0 and arr[dec - 1] > arr[dec]):
            dec -= 1

        return (inc == dec) and dec != 0 and inc != len(arr) - 1