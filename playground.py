# def add(*args):
#     return print(sum(args))
#     # type(args) = tuple
#
# add(1, 35, 7)

# def calculate(n, **kwargs):
#     print(kwargs)
#     # type(kwargs) = dict
#     # for (key, value) in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n
#
#
# print(calculate(5, add=4, multiply=3))

# creating a class with keyword arguments **kwargs
# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.colour = kwargs.get("colour")
#         self.seats = kwargs.get("seats")
#         # get() method will return None if that key is not available in that dictionary.
#         # using [] will give you the value of the but will return error if that key is not available.
#
#
# my_car = Car(make="Nissan", model="GT-R")
# print( my_car.make, my_car.model)


