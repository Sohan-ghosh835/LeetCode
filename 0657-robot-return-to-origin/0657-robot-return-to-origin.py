class Solution(object):
    def judgeCircle(self, moves):
        lr= moves.count("R") - moves.count("L")         #etar time
        ud= moves.count("U") - moves.count("D")
        if lr==0 and ud==0:
            return True
        return False
        # a = [0,0]
        # for ch in moves:
        #     if ch == "U":
        #         a[0] += 1
        #     elif ch == "D":
        #         a[0] -= 1
        #     elif ch == "L":              memory bhalo etar
        #         a[1] += 1
        #     elif ch == "R":
        #         a[1] -= 1
        #     else:
        #         continue
        # return a == [0,0]
        """
        :type moves: str
        :rtype: bool
        """
        