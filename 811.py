from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = Counter()

        for domain in cpdomains:
            x, y = domain.split()
            l = y.split('.')
            curr = ""

            for i in l[::-1]:
                curr = i + curr
                count[curr] += int(x)
                curr = '.' + curr

        res = []
        for key, value in count.items():
            res.append(str(value) + ' ' + key)

        return res