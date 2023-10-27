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