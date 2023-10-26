def city_generator():
    yield "Hamburg"
    yield "Konstanz"
    yield "Berlin"
    yield "Zurich"
    yield "Schaffhausen"
    yield "Stuttgart" 

city = city_generator()
print(next(city))
print(next(city))
print(next(city))
