
Between 3 Question Marks

Create a function that takes a string, which will contain numbers, letters, and question marks.

    Check for 3 question marks between every pair of two numbers that add up to 10.
    If so, return True, otherwise return False.
    If there aren't any two numbers that add up to 10, return False.

In other words, if your input is "arrb6???4xxbl5???eee5", you should return True because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples

question_marks("arrb6???4xxbl5???eee5") ➞ True

question_marks("arrb6???7xxbl5???eee5") ➞ True

question_marks("arrb6???7xxbl5??eee5") ➞ False

question_marks("arrb3???7xxbl???3??eee5") ➞ True

Notes

N/A
