""""""

TEXT_MONTH = 0
MONTH_FIRST = 1
YEAR_FIRST = 2

MONTHS = {"Jan": 1,
          "Feb": 2,
          "Mar": 3,
          "Apr": 4,
          "May": 5,
          "Jun": 6,
          "Jul": 7,
          "Aug": 8,
          "Sep": 9,
          "Oct": 10,
          "Nov": 11,
          "Dec": 12}


class Date():
    """"""
    def __init__():
        """"""
        pass


class DateSet():
    """DateSet manages a set of Dates for the program.

    Attributes:
        _date_dict is the dictionary of dates(key is the canonic date representation)

    Methods:
        __init__ constructor.
        add      adds a date to _date_dict
    """

    def __init__(self, filename):
        """Constructor for DateSet.

        Parameters:filename is a string of the file for input.
        Returns: an instance of DateSet.
        Pre-conditions: filename must be a file.
        Post-conditions: A new DateSet is born or an error
        is thrown and the program quits.
        """
        assert type(filename) == str
        try:
            f = open(filename)
        except FileNotFoundError:
            print("ERROR: Could not open file " + filename)
            exit()
        input_line = 1
        for line in f:
            line = line.split()
            try:
                assert line[0] == "I" or line[0] == "R"
            except AssertionError:
                print("ERROR: Illegal operation on line " + str(input_line))
                exit()
            input_line += 1
            line[1] = line.strip(":")
            date_format = _reason_date_format(line[1])
            date = _convert_date_to_canonical(line[1], date_format)

            self._date_dict = {}
            if line[0] == "I":
                pass
            self.add(date)

    def add(self, date):
        """Adds the date to _date_dict.
        Parameters: date is a string in canonical form.
        Returns: None
        Pre-conditions: date is in canonical form.
        Post-conditions: A date object is updated.
        """
        if date not in self._date_dict:
            self._date_dict[date] = Date(date)
def _convert_date_to_canonical(date, date_format):
    """Conversion function from date to cononical form.

    Parameters: date is the string to convert.
    Returns: string
    Pre-conditions: date is non-empty.
    Post-conditions: string is returned.
    """
    if date_format == TEXT_MONTH:
        date = date.split()
        month = MONTHS[date[0]]
        day = date[1]
        year = date[2]
    elif date_format == MONTH_FIRST:
        date = date.split("/")
        month = date[0]
        day = date[1]
        year = date[2]
    else:
        return date
    return "{:d}-{:d}-{:d}".format(int(year), int(month), int(day))




def _reason_date_format(date):
    """Helper function to reason what the date format is.

    Parameters: date is a string of the date to be reasoned about.
    Returns: Constant representing the date format.
    Pre-conditions: date is not empty.
    Post-conditions: A Constant value is returned.
    """
    if "-" in date:
        return YEAR_FIRST
    elif "/" in date:
        return MONTH_FIRST
    else:
        return TEXT_MONTH


def main():
    filename = input()

main()
