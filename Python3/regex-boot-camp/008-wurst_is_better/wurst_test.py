import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')

from edabit_tester import EdabitTester
from wurst import wurst_is_better

Test = EdabitTester()

Test.assert_equals(wurst_is_better(
    "Sausage fests are like salami fests"),
    "Wurst fests are like Wurst fests")
Test.assert_equals(wurst_is_better(
    "Add the kielbasa and the reserved potatoes and stir through"),
    "Add the Wurst and the reserved potatoes and stir through")
Test.assert_equals(wurst_is_better(
    "Salami sandwiches, salami and cheese, salami on crackers - I couldn't get enough of the salty, spicy sausage"),
    "Wurst sandwiches, Wurst and cheese, Wurst on crackers - I couldn't get enough of the salty, spicy Wurst")
Test.assert_equals(wurst_is_better(
    "sich die Wurst vom Brot nehmen lassen"),
    "sich die Wurst vom Brot nehmen lassen")
Test.assert_equals(wurst_is_better(
    "Bratwurst and Rostbratwurst is a sausage made from finely minced pork and beef and usually grilled and served with sweet German mustard and a piece of bread or hard roll. It can be sliced and made into Currywurst by slathering it in a catchup-curry sauce."),
    "Bratwurst and Rostbratwurst is a Wurst made from finely minced pork and beef and usually grilled and served with sweet German mustard and a piece of bread or hard roll. It can be sliced and made into Currywurst by slathering it in a catchup-curry sauce.")
Test.assert_equals(wurst_is_better(
    "Naem is a common way of preserving pork meat in several Southeast Asian countries, including Thailand, Laos, Cambodia and Vietnam"),
    "Wurst is a common way of preserving pork meat in several Southeast Asian countries, including Thailand, Laos, Cambodia and Vietnam")
Test.assert_equals(wurst_is_better(
    "The chipper group over at Orangatang recently dropped another wheel sensation; the Moronga"),
    "The chipper group over at Orangatang recently dropped another wheel sensation; the Wurst")

Test.summary()