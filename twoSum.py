class TwoSumSolution:
    '''
    This class solve the leetcode problem twosum.
    Given two inputs, an array of integers(nums) and a target(int),
    you are required to get two integers from the list that when
    added they return the target at time complexity O(n).
    You're supposed to return an array containing the indices of 
    the two integers when added give the target.
    '''
    def twoSum(self, nums:list[int], target: int) -> int:
        #create a python dictionary to store complements
        complements = {}
        #loop through the array 
        ##use enumerate to pack in dictionary using the index as the key
        for index, num in enumerate(nums):
            complement = target - num 
            #check whether the complement is already in complements dictionary
            if complement in complements:
                return [complements[complement], index]
            #add number to dictionary
            complements[num] = index

solution1 = TwoSumSolution()
result = solution1.twoSum([2,5,7,9,13], 15)
print(result)