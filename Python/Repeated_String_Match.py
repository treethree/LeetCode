# Approach #1: Ad-Hoc [Accepted]
# Intuition
#
# The question can be summarized as "What is the smallest k for which B is a substring of A * k?" We can just try every k.
#
# Algorithm
#
# Imagine we wrote S = A+A+A+.... If B is to be a substring of S,
# we only need to check whether some S[0:], S[1:], ..., S[len(A) - 1:] starts with B,
# as S is long enough to contain B, and S has period at most len(A).
#
# Now, suppose q is the least number for which len(B) <= len(A * q).
# We only need to check whether B is a substring of A * q or A * (q+1).
# If we try k < q, then B has larger length than A * q and therefore can't be a substring.
# When k = q+1, A * k is already big enough to try all positions for B; namely, A[i:i+len(B)] == B for i = 0, 1, ..., len(A) - 1.
# 
# if len(B) % len(A) == 0:
#     q = len(B) // len(A)
# else:
#     q = (len(B) // len(A)) + 1
# is same as: q = (len(B) - 1) // len(A) + 1

class Solution(object):
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1

# Complexity Analysis:
# Time Complexity: O(N*(N+M)), where M, N are the lengths of strings A, B. We create two strings A * q, A * (q+1) which have length at most O(M+N). When checking whether B is a substring of A, this check takes naively the product of their lengths.
# Space complexity: As justified above, we created strings that used O(M+N) space.
