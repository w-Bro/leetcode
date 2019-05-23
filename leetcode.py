
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for index1, i in enumerate(nums):
            for index2, j in enumerate(nums):
                if i + j == target and index1 != index2:
                    return [index1, index2]

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x >= 0 else -1 * int(str(x).split('-')[1][::-1])
        if x >= 2 ** 31 or x < -1 * (2 ** 31):
            x = 0
        return x

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_normal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        roman_unnormal = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        sum = 0
        while s != '':
            for roman in roman_unnormal.keys():
                if roman in s:
                    sum += roman_unnormal[roman]
                    s = s.replace(roman, '', 1)
                    
            for roman in roman_normal.keys():
                if roman in s:
                    sum += roman_normal[roman]
                    s = s.replace(roman, '', 1)
        return sum

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or strs == []:
            return ""
        shortest_str = strs[[len(_str) for _str in strs].index(min([len(_str) for _str in strs]))]
        while shortest_str != '':
            flag = True
            for _str in strs:
                if not _str.startswith(shortest_str):
                    shortest_str = shortest_str[:-1]
                    flag = False
                    break
            if flag:
                return shortest_str
        return shortest_str

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '([{'
        right = ')]}'
        if s is None or s == '':
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for _s in s:
            if _s in left:
                stack.append(_s)
            else:
                if len(stack) == 0:
                    return False
                left_s = stack.pop()
                if left.index(left_s) != right.index(_s):
                    return False
        if len(stack) == 0:
            return True
        return False
    
    
if __name__ == '__main__':
    solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9))
    # print(solution.reverse(1534236469))
    # print(solution.isPalindrome(121))
    # print(solution.romanToInt('MCMXCIV'))
    # print(solution.longestCommonPrefix(["abab","aba","abc"]))
    print(solution.isValid('(('))