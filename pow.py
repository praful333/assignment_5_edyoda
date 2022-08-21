class Solution(object):
   def myPow(self, x, n):
      power = abs(n)
      res = 1.0
      while power:
         if power & 1:
            res*=x
         x*=x
         power>>=1
      if n<0:
         return 1/res
      return res
ob1 = Solution()
print(ob1.myPow(45, -2))
print(ob1.myPow(21, 3))