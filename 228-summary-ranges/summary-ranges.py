class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        n=len(nums)
        if n==0:
            return res
        a=nums[0]
        for i in range(n):
            if i==n-1 or nums[i+1]!=nums[i]+1:
                if nums[i]!=a:
                    res.append(str(a)+"->"+str(nums[i]))
                else:
                    res.append(str(a))
                if i!=n-1:
                    a=nums[i+1]
        return res