class Solution:
    ''''
    Leetcode 1346: N and its Double
    Returns true if there exist an integer N in an array and also its
    double is in the same array
    '''
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = {}
        for i, num in enumerate(arr):
            if num*2 in seen or (num%2==0 and num/2 in seen):
                return True
            seen[num] = i
        return False

k = Solution()
print(k.checkIfExist([7,1,14,4,11]))#true
l = Solution()
print(l.checkIfExist([7,2,3,5,9]))#false
