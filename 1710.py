class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        total = 0
        
        for box, value in boxTypes:
            if(truckSize >= box):
                total += value * box
                truckSize -= box
            else:
                total += value * (truckSize)
                break

        return total