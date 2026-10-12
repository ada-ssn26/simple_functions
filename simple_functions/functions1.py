from functools import cache


__all__ = ['my_sum', 'factorial', 'sin_function']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    """Return n! (n factorial) for a non-negative integer n."""
    return n * factorial(n-1) if n else 1


def sin_function(x):
    """
    Calculates the sine of an angle (in degrees) without using pi
    or math libraries. Uses Bhaskara I's approximation formula.
    """
    # 1. Normalize angle to stay within 0 to 360 degrees
    x = x % 360

    # 2. Map angles in the 3rd and 4th quadrants (180 to 360) to the
    # 1st and 2nd and invert the sign, since sin(x + 180) = -sin(x)
    sign = 1
    if x > 180:
        x -= 180
        sign = -1

    # 3. Apply Bhaskara I's formula for domain [0, 180]
    numerator = 4 * x * (180 - x)
    denominator = 40500 - (x * (180 - x))

    return sign * (numerator / denominator)
