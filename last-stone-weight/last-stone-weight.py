class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        placeholder = []
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        while len(stones) > 1:
            placeholder.append(stones.pop(stones.index(max(stones))))
            if len(stones) == 1 and len(placeholder) == 1:
                return (placeholder[0] - stones[0])
            elif len(placeholder) == 2 and placeholder[0] == placeholder[1]:
                placeholder = []
            elif len(placeholder) == 2:
                stones.append(placeholder[0] - placeholder[1])
                placeholder = []
        return stones[0]
        


