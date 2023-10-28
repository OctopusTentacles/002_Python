# Exercise 2
# Write a generator f range, which behaves like range but accepts float values.

def frange(*args):
    """  dfgdg """
    startval = 0
    stepsize = 1    
    if len(args) == 1:
        endval = args[0]
    elif len(args) == 2:
        startval, endval = args 
    elif len(args) == 3:
        startval, endval, stepsize = args
    else:
        txt = "range expected at most 3 arguments, got " + len(args)
        raise TypeError(txt)
    
    value = startval
    factor = -1 if stepsize < 0 else 1
    while (value - endval) * (factor) < 0:
        yield value
        value += stepsize
        
# Using frange may llok like this:

for i in frange(5.6):
    print(i, end=", ")
print()
for i in frange(0.3, 5.6):
    print(i, end=", ")
print()
for i in frange(0.3, 5.6, 0.8):
    print(i, end=", ")
print()