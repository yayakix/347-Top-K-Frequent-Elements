class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        dict = {}
        for x in range(len(nums)):
            if nums[x] in dict:
                dict[nums[x]] += 1
            else:
                dict[nums[x]] = 0
        dict_array = dict.items()
        sort_dict = sorted(dict_array, key = lambda x:x[1], reverse= True)
        print(sort_dict)
        new_array = [x[0] for x in sort_dict]
        print(new_array)
        ans = []
        for x in range(k):
           ans.append(new_array[x])
        return ans
