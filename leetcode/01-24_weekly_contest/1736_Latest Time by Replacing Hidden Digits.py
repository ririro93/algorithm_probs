"""
:type time: str
:rtype: str
"""
class Solution(object):
    def maximumTime(self, time):
        result = ''
        for i, c in enumerate(time):
            if c == '?':
                if i == 0:
                    if time[1] == '?':
                        result += '2'
                    elif int(time[1]) >= 4:
                        result += '1'
                    else:
                        result += '2'
                elif i == 1:
                    if result[0] == '2':
                        result += '3'
                    else:
                        result += '9'
                elif i == 3:
                    result += '5'
                elif i == 4:
                    result += '9'
            else:
                result += c
        return result
        