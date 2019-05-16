import re


def question_marks(txt):
    nums = list(re.finditer(r'[0-9\-\.]+', txt))
    tens = 0
    for i in range(len(nums[:-1])):
        if int(nums[i].group()) + int(nums[i+1].group()) == 10:
            tens += 1
            if not re.search(r'\?{3}', txt[nums[i].start():nums[i+1].end()]):
                return False
        else: continue
    return tens > 0
