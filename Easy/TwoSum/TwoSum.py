class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        # 使用dictionary來快速查詢nums中的value的index
        index_search = {}
        for i in range(0, len(nums)):
            if (target-nums[i]) in index_search:
                answer = [index_search[(target-nums[i])], i]
                return answer
            index_search[nums[i]] = i
