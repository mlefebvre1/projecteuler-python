def rotate_left(a):
    nb_digits = len(a)
    rot = [""] * nb_digits
    for digit in range(nb_digits):
        if digit == (nb_digits - 1):
            rot[digit] = a[0]
        else:
            rot[digit] = a[digit + 1]
    return "".join(rot)


def rotate_right(a):
    nb_digits = len(a)
    rot = [""] * nb_digits
    for digit in range(nb_digits):
        if digit == 0:
            rot[digit] = a[nb_digits - 1]
        else:
            rot[digit] = a[digit - 1]
    return "".join(rot)


def rotations(a, direction="left"):
    """
    a : number to apply rotation
    direction : "left" or "right"
    """
    nb_rotations = len(a)
    b = a
    yield b
    for rotation in range(nb_rotations - 1):
        if direction == "left":
            b = rotate_left(b)
        else:
            b = rotate_right(b)
        yield b
