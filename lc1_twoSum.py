class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0;
        j=0;
        size=len(nums)
        print ("input array size:", size)
        map_of_possible_finds=dict()
        while i< size:
            find_in_remaining=target-nums[i]
            if find_in_remaining in map_of_possible_finds:
                return (i, map_of_possible_finds[find_in_remaining])
            map_of_possible_finds[nums[i]]= i
            i+=1
            
            

        return None
