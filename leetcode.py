
class Solution(object):
    """
    1. 数之和
    """
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
    
    """
    7. 整数反转
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x >= 0 else -1 * int(str(x).split('-')[1][::-1])
        if x >= 2 ** 31 or x < -1 * (2 ** 31):
            x = 0
        return x
    
    """
    9. 回文数
    """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    """
    13. 罗马数字转整数
    """
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
    
    """
    14. 最长公共前缀
    """
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
    
    """
    20. 有效的括号
    """
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
    
    """
    21. 合并两个有序链表, 注意给了ListNode的定义
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    """

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass
    
    """
    26. 删除排序数组中的重复项
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        for num in nums:
            if num != nums[j-1]:
                nums[j] = num
                j += 1
                
        return j
    
    """
    27. 移除元素
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
                
        return j
    
    """
    28. 实现strStr()
    """
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle) if needle != '' else 0
    
    """
    35. 搜索插入位置
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
    
    """
    38. 报数
    """
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ['1', '11', '21', '1211', '111221']
        if n < 6:
            return result[n-1]
        for index in range(5, n):
            _str = result[index-1]
            result_str = ''
            count = 0
            last_index = 0
            for i in range(1, len(_str)):
                if _str[i] != _str[i-1]:
                    count = i - last_index
                    result_str += str(count) + _str[i-1]
                    last_index = i
            result_str += str(len(_str)-last_index) + _str[-1]
                
            result.append(result_str)
            
        return result[-1]

    """
    53. 最大子序和
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 要为小于0的数，保证只有一个数时不会比这个数大
        sum = -1
        result = nums[0]
        for num in nums:
            # 一遍循环的原因是如果sum<0，加上num之后必定小于num，故会从当前的num开始计算
            sum = max(num, sum+num)
            print(sum)
            result = max(result, sum)
        return result
    
    """
    58. 最后一个单词的长度
    """

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])
    
    """
    66. 加一
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        num = 0
        for digit in digits:
            num += digit * (10 ** i)
            i -= 1
        num += 1
        result = []
        while num > 0:
            result.append(num % 10)
            num = num // 10
        result.reverse()
        return result
    
    """
    67. 二进制求和
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        l = len(a)
        b = '0' * (l - len(b)) + b
        result = [0]
        for i in range(l):
            result[i] += int(a[- i - 1]) + int(b[- i - 1])
            if result[i] >= 2:
                result[i] -= 2
                result.append(1)
            else:
                result.append(0)
        
        if result[l] == 0:
            result.pop()
            
        result.reverse()
        return ''.join(list(map(lambda x: str(x), result)))
    
    """
    69. x 的平方根
    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i, j = 0, x // 2 + 1
        while i <= j:
            mid = (i + j) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                j = mid - 1
            else:
                i = mid + 1
        return j
    
    """
    70. 爬楼梯
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2, ]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]
    
        
if __name__ == '__main__':
    solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9))
    # print(solution.reverse(1534236469))
    # print(solution.isPalindrome(121))
    # print(solution.romanToInt('MCMXCIV'))
    # print(solution.longestCommonPrefix(["abab","aba","abc"]))
    # print(solution.isValid('(('))
    # print(solution.mergeTwoLists([1, 2, 4], []))
    # print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 4]))
    # print(solution.removeElement([0, 1, 2, 4], 2))
    # print(solution.strStr('aaa', 'bl'))
    # print(solution.searchInsert([1, 3], 2))
    # print(solution.countAndSay(5))
    # print(solution.maxSubArray([2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print('=' * 20)
    # print(solution.maxSubArray([212]))
    # print(solution.lengthOfLastWord(" hello  "))
    # print(solution.plusOne([0, ]))
    # print(solution.addBinary('11', '10'))
    # print(solution.mySqrt(2147395599))
    print(solution.climbStairs(5))