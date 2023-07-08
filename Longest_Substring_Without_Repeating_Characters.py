# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#passes 250 test cases
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=""
        l=set()
        a=0
        def f(a,l,s,s1):
            for i in range(a,len(s)):
                if s1.count(s[i] )==0:
                    s1=s1+s[i]
                    if i==len(s)-1:
                        l.add(len(s1))
                        break
                elif s1.count(s[i])>0:
                    if len(l)!=0:
                        if max(l)<len(s1):
                            l.add(len(s1))
                    elif len(l)==0:
                        l.add(len(s1))
                    if a<len(s)-1:
                        a+=1
                        s1=""
                        f(a,l,s,s1)
                    else:
                        break

            return max(l)
        if len(l)==0 and len(s)!=0:
            z=f(a,l,s,s1)
        elif len(s)==0:
            z=0
        return z
obj=Solution()
print(obj.lengthOfLongestSubstring("dsgfga"))