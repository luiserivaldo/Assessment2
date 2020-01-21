"""
Assessment 2
by Luise Rivaldo
Movie class
"""


class Movie:
    """Represent a Movie object."""

    def __init__(self, name=""):
        """Initialise a Movie instance."""
        self.name = name

    def __str__(self):
        """Return a string representation of a Movie object."""
        return "{} is a movie".format(self.name)
