def is_square(n):
    import math
    return "false" if n < 0 else "true" if math.sqrt(n).is_integer() else "false"