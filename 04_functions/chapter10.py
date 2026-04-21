# BUILD-IN FUNCTIONS
def tea_flavour(flavour="Green tea"):
    """Return the flavour of tea"""
    tea = 'Black tea'
    return flavour

# DUNDER DOC
print(tea_flavour.__doc__) #  ONLY VERY FIRST LINE
print(tea_flavour.__name__)

def generate_bill(tea=0, samosa=0):
    """
    Calculate the totatl bill for tea and samosa
    :param tea: Number of cups
    :param samosa: Number of sammosa
    :return: (total amount, thank you man!)
    """

    total = tea * 10 + samosa*15
    return total, "Thanks you for purchase"
