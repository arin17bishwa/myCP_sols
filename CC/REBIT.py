def modularExponentiation(x, n, m):
    result = 1
    while n > 0:
        if n & 1:
            result = (result * x) % m
        x = (x * x) % m
        n = n // 2
    return result


def modInverse(a, m):
    return modularExponentiation(a, m - 2, m)


k = 998244353


def modularmultiplication(a, b):
    return ((a % k) * (b % k)) % k


class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'&': 1, '|': 1, '^': 1}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if i == '#':
                self.output.append('1')
            elif i == '(':
                self.push(i)
            elif i == ')':
                while ((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        return ("".join(self.output))


def printing(zero, one, a, den):
    q = modInverse(den, k)
    z = modularmultiplication(zero, q)
    o = modularmultiplication(one, q)
    A = modularmultiplication(a, q)
    print(z, o, A, A)  # ,'(',zero,one,a,a,')')


def proband0(zeros, ones):
    return (modularmultiplication(zeros[0], zeros[1]) + modularmultiplication(zeros[0],
                                                                              ones[1]) + modularmultiplication(ones[0],
                                                                                                               zeros[
                                                                                                                   1])) % k


def proband1(zeros, ones):
    return (modularmultiplication(ones[0], ones[1]))


def probor0(zeros, ones):
    return (modularmultiplication(zeros[0], zeros[1]))


def probor1(zeros, ones):
    return (modularmultiplication(ones[0], ones[1]) + modularmultiplication(zeros[0], ones[1]) + modularmultiplication(
        ones[0], zeros[1])) % k


def probxor0(zeros, ones):
    return (modularmultiplication(ones[0], ones[1]) + modularmultiplication(zeros[0], zeros[1])) % k


def probxor1(zeros, ones):
    return (modularmultiplication(zeros[0], ones[1]) + modularmultiplication(ones[0], zeros[1])) % k


def func(s):
    obj = Conversion(len(s))
    s = list(obj.infixToPostfix(s))
    # print(s)
    ones = []
    zeros = []
    c = 0
    for i in s:
        # print(zeros,ones)
        if i == '&':
            one = proband1(zeros[-2:], ones[-2:])
            zero = proband0(zeros[-2:], ones[-2:])
            ones = ones[:-2]
            ones.append(one)
            zeros = zeros[:-2]
            zeros.append(zero)
        elif i == '|':
            one = probor1(zeros[-2:], ones[-2:])
            zero = probor0(zeros[-2:], ones[-2:])
            ones = ones[:-2]
            ones.append(one)
            zeros = zeros[:-2]
            zeros.append(zero)
        elif i == '^':
            one = probxor1(zeros[-2:], ones[-2:])
            zero = probxor0(zeros[-2:], ones[-2:])
            ones = ones[:-2]
            ones.append(one)
            zeros = zeros[:-2]
            zeros.append(zero)
        else:
            ones.append(int(i))
            zeros.append(int(i))
            c += 1

    zero, one = int(zeros[0]), int(ones[0])
    a = (zero * one) % k
    zero = modularExponentiation(zero, 2, k)
    one = modularExponentiation(one, 2, k)
    den = modularExponentiation(2, 2 * c, k)
    printing(zero, one, a, den)


for _ in range(int(input())):
    s = input()
    func(s)
