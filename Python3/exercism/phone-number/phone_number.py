class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.clean_number = self.clean_up()
        self.number = self.is_valid()
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:]

    def clean_up(self):
        """ Remove everything except digits.  """
        return "".join(d for d in self.phone_number if d.isdigit())
        
    def is_valid(self):
        """ Checks if the number is a valid number.  """
        tester = self.clean_number
        # Count digits.  
        if len(tester) not in [10,11]:
            self.bad_number()
        if len(tester) == 11:
            if tester[0] == '1':
                tester = tester[1:]
            else:
                self.bad_number()
        # At this point tester should be 10 digits long.
        # Check for valid area code and exchange code.
        if int(tester[0]) in range(2,10) and int(tester[3]) in range(2,10):
            return tester
        else:
            self.bad_number()

    def bad_number(self):
        raise ValueError("Invalid number entered")

    def pretty(self):
        """ Returns the number in a (000) 000-0000 format.  """
        return f"({self.area_code}) {self.exchange_code[0:3]}-{self.exchange_code[3:]}"