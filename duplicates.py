class DuplicatesSolution:
    '''
    Checks whether a given array consists of any duplicates
    and returns true if it does else false
    '''
    def duplicates(self, nums:list) -> bool:
        #create empty dict 
        seen = {}
        for i, num in enumerate(nums):
            if nums and num in seen:
                return True
            #add i and its value to seen
            seen[num] = i
        return False

k = DuplicatesSolution()
print(k.duplicates([1,2,3,4]))#returns false
l = DuplicatesSolution()
print(l.duplicates([1,2,3,4,5,2]))#returns true