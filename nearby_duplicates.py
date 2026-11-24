class Solution:
    '''
    Leetcode 219-Duplicates II
    Given a list of integers and an integer k, returns True if 
    there are duplicates i and j in the list such that absolute(i-j)<=k
    else False
    '''
    def containsNearbyDuplicates(self, nums:list, k:int) -> bool:
        numsdict = {}
        for i, num in enumerate(nums):
            #check if there are duplicates
            if num in numsdict:
                #get the absolute difference of the indices of the duplicates
                diff = abs(numsdict[num] - i)
                if diff <= k:
                    return True
            numsdict[num] = i
        return False

k = Solution()
print(k.containsNearbyDuplicates([1,2,3,4,1,5,6], 3))#returns False
l = Solution()
print(l.containsNearbyDuplicates([1,2,3,1,4,5,6], 4))#true
