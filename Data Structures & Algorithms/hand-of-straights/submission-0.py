class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = defaultdict(int)
        for card in hand:
            counts[card] += 1
        
        minH = list(counts.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if counts[i] == 0:
                    return False

                counts[i] -= 1
                if counts[i] == 0:
                    if i != minH[0]:
                        return False
                    
                    heapq.heappop(minH)

        return True 
