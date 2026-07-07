class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        le =1
        re=x
        ans =0
        while le <=re:
            mid =(le+re)//2
            if mid*mid == x:
                return mid
            elif (mid*mid)< x:
                le =mid+1
                ans =mid
            else:
                re =mid-1
        return ans