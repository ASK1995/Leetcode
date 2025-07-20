class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split()

        for i in range(len(l)):
            if(len(l[i]) > 2):
                l[i] = l[i].upper()[0] + l[i].lower()[1:]
            else:
                l[i] = l[i].lower()
        return " ".join(l)