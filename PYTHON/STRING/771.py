class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        myJewels = 0
        for s in stones:
            for j in jewels:
                if s == j:
                    myJewels += 1
        return myJewels