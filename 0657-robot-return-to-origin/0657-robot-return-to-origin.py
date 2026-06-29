class Solution(object):
    def judgeCircle(self, moves):
        a = [0,0]
        for ch in moves:
            if ch == "U":
                a[0] += 1
            elif ch == "D":
                a[0] -= 1
            elif ch == "L":
                a[1] += 1
            elif ch == "R":
                a[1] -= 1
            else:
                continue
        if a == [0,0]:
            return True
        else:
            return False
        
        """
        :type moves: str
        :rtype: bool
        """
        