class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for i in range(len(nums)):
            if i - l > k:
                window.remove(nums[l])
                l += 1

            if nums[i] in window:
                return True

            window.add(nums[i])

        return False
            



        