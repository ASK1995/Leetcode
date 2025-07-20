class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if(money < children):
            return -1
        elif money > 8 * children:
            return children - 1
        elif money == 8 * children - 4:
            return children - 2
        return (money - children) // 7