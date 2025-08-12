class Solution:
    def compress(self, chars: List[str]) -> int:
        index, count = 0, 1
        prev = chars[0]

        for i in range(1, len(chars)):
            if(chars[i] == prev):
                count += 1
            else:
                chars[index] = prev
                prev = chars[i]
                index += 1
                if(count != 1):
                    count = str(count)
                    for num in count:
                        chars[index] = num
                        index += 1
                count = 1

        chars[index] = prev
        index += 1
        if(count != 1):
            count = str(count)
            for num in count:
                chars[index] = num
                index += 1
        count = 1

        return index