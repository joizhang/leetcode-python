# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            ans = 7 * (rand7() - 1) + rand7()
            if ans <= 40:
                break
        return (ans-1) % 10 + 1