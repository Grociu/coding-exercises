"""This module is a simple tester for the Edabit website.

The problem: Edabit uses it's own test module instead of unittest I'm used to.
I want to import the Edabit tests to my own workspace with an easy copy&paste.
This module allows this.

Usage:
-------------------------
import sys
sys.path.append('{path for the edabit_tester module}')

from edabit_tester import EdabitTester
from {tested_module} import {tested_function}

Test = EdabitTester()

{Copy and paste the Edabit tests here}

Test.summary()
------------------------

Please mind the correct module names and directories for imported modules :)
"""


class EdabitTester(object):
    
    def __init__(self):
        self.succeses = 0
        self.failures = 0
        self.total = 0
    
    def assert_equals(self, statement_1, statement_2):
        """If statements are the same adds a success, otherwise failure.
        
        This also prints the number of test that was failed.
        """
        if statement_1 == statement_2:
            self.succeses += 1
            self.total += 1
            return True
        else:
            self.failures += 1
            self.total += 1
            print(f"FAILED TEST {self.total}: " \
                f"{statement_1} is not {statement_2}")
            return False
    
    def testing_result(self):
        """Returns an overall result of a test."""
        if self.total == 0:
            return "NO TESTS"
        elif self.failures > 0:
            return "FAILURE"
        else:
            return "SUCCESS"
    
    def summary(self):
        """Prints a summury of the testing process."""
        print(f"Testing results:\nTOTAL = {self.total}\n" \
            f"SUCCESS = {self.succeses} \nFAILURES = {self.failures}\n" \
            f"OVERALL {self.testing_result()}")
