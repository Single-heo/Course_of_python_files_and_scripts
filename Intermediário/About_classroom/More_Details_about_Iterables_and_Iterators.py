import sys
iterable = ['I', 'hi', '__iter__']
iterator = iterable.__iter__() # or iter(iterable) // __iter__ and __next__
# print(next(iterator)) # 1st is 'I'
# print(next(iterator)) # 2nd is 'hi'
# print(next(iterator)) # 3rd is '__iter__'
# 'next' ever jumps to the next element in an iterable, in this case the iterable is a list( it would be a 'for' manually)
#_____________________________________________________________________________________________
#                       Generator expression, iterables and iterators in python

# it is used when a variable is very big : x = [x for x in range(100000)]
# this is bad, all values in variable are stored in RAM, causing lag :(
# the generator, make me ask 1 value at time, for comparison we will use sys, with this, it can show the size

variable = [n for n in range(10000)] # he has 85176 bytes 🙁
generator_best = (n for n in range(10000))# While he has 104 bytes 🤯
print(sys.getsizeof(variable))
print(sys.getsizeof(generator_best))

for n in generator_best:
    print(n)
