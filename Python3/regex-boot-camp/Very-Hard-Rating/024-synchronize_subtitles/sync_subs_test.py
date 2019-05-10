import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from sync_subs import sync_subs

Test = EdabitTester()

Test.assert_equals(sync_subs(
"""708
00:44:50,006 --> 00:44:53,007
People are taking this festival extremely seriously.""", "00:03:30,550"),
"""708
00:48:20,556 --> 00:48:23,557
People are taking this festival extremely seriously.""")

Test.assert_equals(sync_subs(
"""729
00:45:55,704 --> 00:45:59,506
So we don't have to wait for it.""", "00:00:00,000"),
"""729
00:45:55,704 --> 00:45:59,506
So we don't have to wait for it.""")

Test.assert_equals(sync_subs(
"""735
00:46:24,967 --> 00:46:27,701
We've already won.
736
00:46:27,736 --> 00:46:30,637
[Crowd cheers]""", "01:21:00,211"),
"""735
02:07:25,178 --> 02:07:27,912
We've already won.
736
02:07:27,947 --> 02:07:30,848
[Crowd cheers]""")

Test.assert_equals(sync_subs(
"""722
00:45:34,483 --> 00:45:36,917
My mercy...""", "00:60:09,010"),
"There is a problem with the second argument")

Test.assert_equals(sync_subs(
"""722
00:45:34,483 --> 00:45:36,917
My mercy...""", "00:00:09.000"),
"There is a problem with the second argument")

Test.summary()
