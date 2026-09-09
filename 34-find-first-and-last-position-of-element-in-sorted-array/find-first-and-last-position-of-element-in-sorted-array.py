class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        first_position=bisect.bisect_left(nums,target)
        last_position=bisect.bisect_right(nums,target)
        if bisect.bisect_right(nums,target)!=bisect.bisect_left(nums,target) :
            return [bisect.bisect_left(nums,target),bisect.bisect_right(nums,target)-1]
        return [-1,-1]    

        