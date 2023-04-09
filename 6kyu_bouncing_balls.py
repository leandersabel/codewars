# https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncing_ball(h, bounce, window):
    """
    A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level,
    h, is known.

    He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

    His mother looks out of a window 1.5 meters from the ground.

    How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

    Three conditions must be met for a valid experiment:
    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than h.
    If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

    Note:
    The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

    Examples:
    >>> bouncing_ball(3, 0.66, 1.5)
    3

    >>> bouncing_ball(3, 1, 1.5)
    -1

    >>> bouncing_ball(2, 0.5, 1)
    1

    >>> bouncing_ball(3, 0.66, 1.5)
    3

    >>> bouncing_ball(30, 0.66, 1.5)
    15

    >>> bouncing_ball(30, 0.75, 1.5)
    21

    >>> bouncing_ball(10, 0.75, 10)
    -1

    >>> bouncing_ball(30, 0, 1.5)
    -1
    """

    # Check starting conditions
    if h < 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    # Passing by the first time on the way down
    counter = 1

    while h > window:
        h *= bounce
        if h > window: counter += 2

    return counter


