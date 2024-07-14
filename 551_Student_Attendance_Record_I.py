class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lates = 0
        absents = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absents += 1
                lates = 0
            elif s[i] == 'L':
                lates += 1
            else:
                lates = 0
            if lates == 3 or absents == 2:
                return False
        return True