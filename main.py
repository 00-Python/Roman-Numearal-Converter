class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        doubles = {'IV':-1, 'IX':-1, 'XL':-10, 'XC':-10, 'CD':-100, 'CM':-100}
        broke_down = [*s]  # make a list
        total = []
        length = len(broke_down)

        for num in broke_down:
            if num in nums:
                total.append(nums[num])
            else:
                break


        for x in range(0, length):
            if x < length-1:
                if broke_down[x] == 'I' and broke_down[x + 1] == 'V' or broke_down[x] == 'I' and broke_down[x + 1] == 'X':
                    total.append(-1)
                    total.remove(1)
                elif broke_down[x] == 'X' and broke_down[x + 1] == 'L' or broke_down[x] == 'X' and broke_down[x + 1] == 'C':
                    total.append(-10)
                    total.remove(10)
                elif broke_down[x] == 'C' and broke_down[x + 1] == 'D' or broke_down[x] == 'C' and broke_down[x + 1] == 'M':
                    total.append(-100)
                    total.remove(100)
        
        return sum(total)


s = 'MCMXCIV'
x = Solution()
conversion = x.romanToInt(s)

print(conversion)
