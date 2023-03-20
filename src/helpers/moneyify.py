# helper function to coerce a value into a 2 decimal place float
def moneyify(value: any) -> str:
    """
    This function takes a value of any type and returns a string representation of a float with 2 decimal places.
    """
    if value is None:
        return 0.00
    return "{:.2f}".format(float(value))
