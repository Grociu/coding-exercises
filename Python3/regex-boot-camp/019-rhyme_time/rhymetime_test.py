import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from rhymetime import does_rhyme

Test = EdabitTester()

Test.assert_equals(
    does_rhyme('Sam I am!', 'Green eggs and ham.'), True,
    'Should work with punctuation.')
Test.assert_equals(
    does_rhyme('Sam I am!', 'Green eggs and HAM.'), True,
    'Should work with uppercase/punctuation.')
Test.assert_equals(
    does_rhyme('head straight to town', 'give me not a frown'), True)
Test.assert_equals(
    does_rhyme('with an unpleasant bump', 'in a slump'), True)
Test.assert_equals(
    does_rhyme('your elbow and chin!', 'how much can you win?'), True,
    'Should work with punctuation.')
Test.assert_equals(
    does_rhyme('you will start to race', 'the waiting Place'), True,
    'Should work with upper case letters.')
Test.assert_equals(
    does_rhyme('All that waiting and staying.', 'where the band are playing.'),
    True, 'Should work with punctuation.')
Test.assert_equals(
    does_rhyme('You are off to the races', 'a splendid day.'), False)
Test.assert_equals(
    does_rhyme('and frequently do?', 'you gotta move.'), False)
Test.assert_equals(
    does_rhyme('down by the bay', 'where the watermelons grow'), False)
Test.assert_equals(
    does_rhyme('back to my home', 'i dare not go'), False)

Test.summary()
