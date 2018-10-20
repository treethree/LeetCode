 # The natural way to represent the time is as an integer t in the range 0 <= t < 24 * 60.
 # Then the hours are t / 60, the minutes are t % 60,
 # and each digit of the hours and minutes can be found by hours / 10, hours % 10 etc.

class Solution(object):
    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))
