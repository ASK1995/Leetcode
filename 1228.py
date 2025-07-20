class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff1, diff2 = None, None
        first = None
        for i in range(1, len(arr)):
            if(diff1 == None):
                diff1 = arr[i] - arr[i - 1]
                first = arr[i]
            elif(arr[i] - arr[i - 1] != diff1):
                diff2 = arr[i] - arr[i - 1]
                if(diff2 == diff1 * 2):
                    return arr[i - 1] + diff1
                else:
                    return first - diff1//2
        return arr[0]