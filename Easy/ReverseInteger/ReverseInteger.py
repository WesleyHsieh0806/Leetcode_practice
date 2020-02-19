class Solution:
    def reverse(self, x: int) -> int:
        try:
            divisor = 10
            output = []
            answer = 0
            if x > 0:
                while x != 0:
                    remainder = x % divisor
                    x -= remainder
                    output.append(int(remainder/(divisor/10)))
                    divisor *= 10
                for i in range(0, len(output)):
                    answer += output[i]*(10**(len(output)-1-i))
                if answer <= 2**31-1:
                    return answer
                else:
                    return 0
            elif x < 0:
                x = -x
                while x != 0:
                    remainder = x % divisor
                    x -= remainder
                    output.append(int(remainder/(divisor/10)))
                    divisor *= 10
                for i in range(0, len(output)):
                    answer += output[i]*(10**(len(output)-1-i))
                if answer <= 2**31:
                    return (0-answer)
                else:
                    return 0
            elif x == 0:
                return 0

        except:
            # return的數字有誤的時候 會跑到except
            return 0
