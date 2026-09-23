#                                                                              Type checking:
#                                       Write a function that takes an object and prints its type using `type()`.


def check_type(value):
    return type(value).__name__

print(check_type(42))
print(check_type(3.5678))
print(check_type("Welcome!"))
print(check_type([1, 2, 3]))
print(check_type((1, 22.56, "QA") ))
print(check_type({'Ivan': 89132227789, 'city': "Tomsk"}))
print(check_type(True))
print(check_type(None))









