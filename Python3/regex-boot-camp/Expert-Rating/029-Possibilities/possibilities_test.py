import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from possibilities import unravel

Test = EdabitTester()

Test.assert_equals(unravel("abc"), ["abc"])
Test.assert_equals(unravel("a[b|c]"), ["ab", "ac"])
Test.assert_equals(unravel("a[b|c|d]e"), ["abe", "ace", "ade"])
Test.assert_equals(unravel("a[b|cd]ef"), ["abef", "acdef"])
Test.assert_equals(
    unravel("a[b|c]def[g]"), ["abdefg", "acdefg"])
Test.assert_equals(
    unravel("a[b|c]de[f|g]"), ["abdef", "abdeg", "acdef", "acdeg"])
Test.assert_equals(
    unravel("a[b]c[d]"), ["abcd"])
Test.assert_equals(
    unravel("[a][b][c][d]"), ["abcd"])
Test.assert_equals(unravel("[a][b][c]d[e]"), ["abcde"])
Test.assert_equals(
    unravel("[a][b][c]d[e|f|g]"), ["abcde", "abcdf", "abcdg"])
Test.assert_equals(
    unravel("[a|b][c|d][e|f]"),
    ["ace", "acf", "ade", "adf", "bce", "bcf", "bde", "bdf"])
Test.assert_equals(
    unravel("[a][b|c|d][e][f|g]"),
    ["abef", "abeg", "acef", "aceg", "adef", "adeg"])
Test.assert_equals(
    unravel("apple [pear|grape]"), ["apple grape", "apple pear"])
Test.assert_equals(
    unravel("apple [pear|grape] [persimmon|mango] [cherry|apricot]"), 
    ["apple grape mango apricot",
    "apple grape mango cherry",
    "apple grape persimmon apricot",
    "apple grape persimmon cherry",
    "apple pear mango apricot",
    "apple pear mango cherry",
    "apple pear persimmon apricot",
    "apple pear persimmon cherry"])
Test.assert_equals(
    unravel("Let's do [Friday|Wednesday|Saturday] at [4|5|7] for the [concert|movies]?"), 
["Let's do Friday at 4 for the concert?",
 "Let's do Friday at 4 for the movies?",
 "Let's do Friday at 5 for the concert?",
 "Let's do Friday at 5 for the movies?",
 "Let's do Friday at 7 for the concert?",
 "Let's do Friday at 7 for the movies?",
 "Let's do Saturday at 4 for the concert?",
 "Let's do Saturday at 4 for the movies?",
 "Let's do Saturday at 5 for the concert?",
 "Let's do Saturday at 5 for the movies?",
 "Let's do Saturday at 7 for the concert?",
 "Let's do Saturday at 7 for the movies?",
 "Let's do Wednesday at 4 for the concert?",
 "Let's do Wednesday at 4 for the movies?",
 "Let's do Wednesday at 5 for the concert?",
 "Let's do Wednesday at 5 for the movies?",
 "Let's do Wednesday at 7 for the concert?",
 "Let's do Wednesday at 7 for the movies?"])

Test.summary()
