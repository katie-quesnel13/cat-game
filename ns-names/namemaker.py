import random
from prefixes import *
from suffixes import *


def prefix():
    return random.choice(prefix_list)


def suffix(pre):
    suf = pre
    while str.lower(suf) == str.lower(pre):
        suf = random.choice(suffix_list)
    return suf


prefix_list = []
prefix_list.extend(birds_list)
prefix_list.extend(plants_list)
prefix_list.extend(sealife_list)
prefix_list.extend(wildlife_list)
prefix_list.extend(bugs_list)

for i in range(10):
    p = prefix()
    s = suffix(p)
    print(f"{p}{s}")
