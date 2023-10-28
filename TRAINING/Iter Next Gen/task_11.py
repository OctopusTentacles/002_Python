# Exercise 1
# Write a generator which computes the running average.

def running_average():
    total = 0.0
    counter = 0
    average = None
    while True:
        term = yield average
        total += term
        counter += 1
        average = total / counter


ra = running_average()      # initialize the coroutine
next(ra)                    # we have to start the coroutine

for value in [7, 13, 17, 231, 12, 8, 3]:

    print("sent: {val:3d}, new average: {avg:6.2f}".format(
        val=value, avg=ra.send(value)))
