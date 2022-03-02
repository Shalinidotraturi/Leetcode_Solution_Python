Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_of_x={}
        len_of_nums=len(nums)
        i=0
        while i<len_of_nums:
            val= target - nums[i]
            if(val in dict_of_x):
                return [dict_of_x[val],i]
            dict_of_x[nums[i]]=i
            i+=1
