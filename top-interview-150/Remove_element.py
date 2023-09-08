class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        # for every number in nums
        for num in nums:
            # if the value of num is not equal to val 
            if num != val:
                # nums[0] = 2
                # nums[1] - 2
                nums[i] = num
                i += 1
            # by this way we will be able to keep only the elements that we need

        return i

# Goal in problem solving is to the see the goal of the solution and not try and solve it in conventional means. 
# identify the goal and we shalll push to towards that
        
