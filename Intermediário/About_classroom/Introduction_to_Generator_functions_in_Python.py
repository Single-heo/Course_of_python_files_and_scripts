# about : create a generator function
# We make pauses in a function with 'yield'

def generator():
    yield  # he pauses, It will only start again when we give a next then it pauses until it finds another yield
    print('continuing....')
    yield
gen = generator()
print(next(gen)) # in 1st yield
# execute the print in the function
print(next(gen)) # stop on 2nd yield