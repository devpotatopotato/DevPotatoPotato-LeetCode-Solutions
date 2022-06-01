class Solution:
    def my_sol(self, dividend: int, divisor: int) -> int:
        # time limit excceded
        if dividend == 0:
            return 0

        isPositive = True

        if dividend < 0:
            isPositive = not isPositive
            dividend = abs(dividend)
        
        if divisor < 0:
            isPositive = not isPositive
            divisor = abs(divisor)
        

        count = 0

        while dividend >= divisor:
            dividend -= divisor
            count += 1
        
        return count if isPositive else -count
    
    def sol1(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                print(temp)
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
            print(f"res: {i}")
            print(f"dividend: {dividend}")
            print("_________________")
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)