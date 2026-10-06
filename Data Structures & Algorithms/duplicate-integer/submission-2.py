class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:    
        uniquelist = set()
        for i in nums:
            if i in uniquelist:
                return True
            uniquelist.add(i)
        return False

                