def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print(multiply(6, 4))

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(is_even(8))

def get_largest(a, b, c):

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(get_largest(2, 8, 0))   


def calculate_area(length, width):
    return length * width

print(calculate_area(7, 9))

def upper_case(text):
    return text.upper()

print(upper_case("hello"))
