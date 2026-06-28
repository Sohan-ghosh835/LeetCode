class Solution(object):
    def plusOne(self, digits):
        l = [0]*(len(digits)-1)
        l.append(1)
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += l[i]
            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i - 1] += 1
        return digits
        

            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        