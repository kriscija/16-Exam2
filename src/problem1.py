"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Joe Krisciunas.  April 2018.
"""  # Done


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


###############################################################################
# Done
#
#   Once you are confident that you understand the  Rect  class and its code,
#   change the TO-DO for this problem to DONE.
#
#   If you do NOT understand the  Rect  class and its code,
#   talk to your instructor to see how to proceed.
###############################################################################
class Rect(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height


def run_test_problem1():
    """ Tests the   problem1   function. """
    # -------------------------------------------------------------------------
    # Done
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')
    l1 = [Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
    l2 = [Rect(25, 4),
                Rect(4, 4),
                Rect(100, 10)]
    #test 1
    actual1 = problem1(l1)
    print('expected = 762')
    print('actual:', actual1)

    # test 2
    actual2 = problem1(l2)
    print('expected = 1116')
    print('actual:', actual2)


def problem1(rectangles):



    """
    What comes in:  A sequence of  Rect  objects.
    What goes out:  Returns the sum of the areas of the given  Rect  objects.
    Side effects:   None.
    Example:
      problem1([Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
         returns 50 + 12 + 700, which is 762

    Type hints:
    :param rectangles: [Rect]
    :return: int
    """
    sum = 0
    for k in range(len(rectangles)):

        test = rectangles[k]
        sum = sum + (test.w * test.h)
    return sum

    # -------------------------------------------------------------------------
    # Done
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()