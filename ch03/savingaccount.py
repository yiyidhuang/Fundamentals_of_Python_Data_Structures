class SavingAccount(object):
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    def __init__(self, name, pin, balance=0.0):
        self._name = name
        self._pin = pin
        self_balance = balance

    def __lt__(self, other):
        return self._name < other._name

    # Other methods, including __eq__
    