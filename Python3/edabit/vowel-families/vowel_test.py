import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from vowel import same_vowel_group

Test = EdabitTester()

Test.assert_equals(
    same_vowel_group(["hoops", "chuff", "bot", "bottom"]),
    ["hoops", "bot", "bottom"]
    )
Test.assert_equals(
    same_vowel_group(["crop", "nomnom", "bolo", "yodeller"]),
    ["crop", "nomnom", "bolo"]
    )
Test.assert_equals(
    same_vowel_group(
        ["semantic", "aimless", "beautiful", "meatless icecream"]
        ),
    ["semantic", "aimless", "meatless icecream"]
    )
Test.assert_equals(
    same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]),
    ["many"]
    )
Test.assert_equals(
    same_vowel_group(["toe", "ocelot", "maniac"]),
    ["toe", "ocelot"]
    )
Test.assert_equals(
    same_vowel_group(["a", "apple", "flat", "map", "shark"]),
    ["a", "flat", "map", "shark"]
    )
Test.assert_equals(
    same_vowel_group(["a", "aa", "ab", "abc", "aaac", "abe"]),
    ["a", "aa", "ab", "abc", "aaac"]
    )

Test.summary()
