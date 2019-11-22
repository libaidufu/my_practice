from collections import Iterable, Iterator

'''
callatz猜想的三种实现
简单循环的方法
迭代器版本
生成器版本
迭代器的__iter__方法一个具有__next__方法的对象，且该__next__方法必须以StopIteration为结束时的异常
从迭代器可以看出while循环和for循环的本质区别
'''

# 普通循环的方法
def collatz1(n):
    sequence = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence
#
# for x in collatz1(7):
#     print(x)

# 迭代器的版本
# for循环本质是先调用可迭代对象的__iter__方法得到一个迭代器对象，之后不断调用该可迭代对象
# 即不断调用可迭代对象的__iter__方法返回的迭代器对象的__next__方法，知道产生StopIteration异常。
# for循环使用的是一个可迭代对象。
class Collatz2(object):
    def __init__(self, start):
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == 1:
            raise StopIteration()
        elif self.value % 2 == 0:
            self.value = self.value / 2
        else:
            self.value = 3 * self.value + 1
        return self.value

b = Collatz2(7)
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
# for x in Collatz2(7):
#     print(x)


# 生成器的版本
def collatz3(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        yield n
#
# for x in collatz3(7):
#     print(x)

