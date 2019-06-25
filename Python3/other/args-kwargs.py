""" Exercises to train the use of *args and **kwargs. """

# Example 1

""" Using *args to pass the variable length arguments to the function"""

# a) simple sum

def simple_sum(*nums):
    #return sum(nums)
    result = 0
    for num in nums:
        result += num
    return result

# print(simple_sum(1, 4, 5, 6, 4, 3, 2, 2)) 
# print(simple_sum(4, 5))
# print(simple_sum(1))
# print(simple_sum(1, 4, 5, 6))
# print(simple_sum(1, 4, 5, 0))

# b) sum of squares if even, cubes if odd

def sum_of_powers(*nums):
    elements = [num ** 2 if num % 2 == 0 else num ** 3 for num in nums]
    return sum(elements)

# print(sum_of_powers(1,4,5,6,4,4,3,2,2,2))
# print(sum_of_powers(4,5))
# print(sum_of_powers(1))
# print(sum_of_powers(1,4,5,6))
# print(sum_of_powers(1,4,5,0))

# Example 2 - Print name and e--mail from a database:

data = [
    {'name' : 'John', 'e-mail': 'john@domain.com', 'nickname': 'Small'},
    {'name': 'Robin', 'e-mail': 'robin.in.hood@domain.com', 'weapon': 'Bow'},
    {'name': 'Tuck', 'e-mail': 'godisgreat@domain.com', 'drink': True},
    {'name': 'Will', 'e-mail': 'daggerdaggerdagger@domain.com', 'color': 'Red'}
    ]

def get_name_and_email(**user_data):
    print(f'{user_data["name"]} can be reached at {user_data["e-mail"]}')

for entry in data:
    get_name_and_email(**entry)