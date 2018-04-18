"""
Exam 2, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Joe Krisciunas.  April 2018.
"""  # Done


###############################################################################
# Done
#   In this problem, you will go through the methods of the  Person  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write whatever code you want in  main  to test your code.
#            We wrote SOME testing code in  main  just to get you started.
#
###############################################################################

def main():
    """ Tests the  Person  class. """
    # -------------------------------------------------------------------------
    # Here is some simple code for testing a small part of the  Person  class:
    # -------------------------------------------------------------------------

    # Test get_age:
    p1 = Person(9)
    print(p1.get_age())  # Should print 9

    # person init test
    print(p1.age)

    # birthday test
    p1.celebrate_birthday()
    print(p1.age)
    # birthdays test
    p1.celebrate_birthdays(5)
    print(p1.age)

    # older person test
    nuperson = p1.older_person()
    print(nuperson.age)

    # -------------------------------------------------------------------------
    # WRITE MORE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Person  class.  You are graded only on your implementation of
    #   the  Person  class, NOT on the quality or quantity of these tests
    #   that you write here. So KEEP IT SIMPLE here in main.
    # -------------------------------------------------------------------------


class Person(object):
    def __init__(self, age):
        self.age = age

        """
        What comes in:  The Person's age.
        Side effects: Sets instance variables as needed by the other methods.
        """
        # Done

    def get_age(self):
        return self.age
        """ Returns this Person's age. """
        # Done

    def celebrate_birthday(self):
        self.age = self.age + 1
        print('Happy Birthday')
        """
        Increments this Person's age.
        ALso prints 'Happy birthday!'.
        """
        # Done

    def celebrate_birthdays(self, n):
        for k in range(n):
         self.celebrate_birthday()


        """
        What comes in: A non-negative integer n.
        Side effects:  Calls the  celebrate_birthday  method  n  times.
        """
        # Done

    def older_person(self):
        nuage = self.age * 2
        return Person(nuage)

        """
        Returns a new Person whose age is twice this Person's age.
        """
        # Done


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()