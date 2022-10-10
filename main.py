class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        broke_down = [*s] # make a list

        nn = []
        for num in broke_down:
            print(num)
            if num in nums:
                nn.append(nums[num])
        nn_length = int(len(nn))
                 
        total = 0 
        print(nn)
        for x in range(0, nn_length):
            if x < len(nn)-1:
                
                if nn[x] == 1 and nn[x + 1] == 5 or nn[x] == 1 and nn[x + 1] == 10:
                    nn.append(-1)
                elif nn[x] == 10 and nn[x + 1] == 50 or nn[x] == 10 and nn[x + 1] == 100:
                    nn.append(-10)
                elif nn[x] == 100 and nn[x + 1] == 500 or nn[x] == 100 and nn[x + 1] == 1000:
                    nn.append(-100)
        
        print(nn)
                
            
s = 'MCMXCIV'        
x = Solution()
conversion = x.romanToInt(s)

print(conversion)
