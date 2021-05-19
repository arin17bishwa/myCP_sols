class FizzBuzz:
    def getNumbers(self, n):
        ans = []
        for i in range(1, n + 1):
            t = ''
            if i % 3 == 0:
                t += 'Fizz'
            if i % 5 == 0:
                t += 'Buzz'
            if t == '':
                t = str(i)
            ans.append(t)
        return ans
