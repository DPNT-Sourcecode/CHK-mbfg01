from collections import defaultdict
from xml.etree.ElementTree import QName

# noinspection PyUnusedLocal
# skus = unicode string

#  greedy
# still greedy algorithm

# input string format? csv? or just like 1A2B3C ??

# is empty basket as illegal input? it should return 0 instead of -1 I guess
def checkout(skus):
    catagory = defaultdict(lambda: 0)
    ALLOWED_CAT = ("A", "B", "C", "D", "E")
    # one pass to store
    # we can calculate initial pricing with E and remove free Bs from the dict
    for i in skus:
        if i not in ALLOWED_CAT:
            return -1
        catagory[i] += 1
    catagory["B"] -= catagory["E"] // 2

    #price mapping
    special_price = {
        "A": (3, 130),
        "B": (2, 45)
    }
    normal_price = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    }
    # fianl result
    # calculate E and remove it from the dict
    nb_e = catagory.pop("E", 0)
    res = nb_e * normal_price["E"]

    for cat ,nb in catagory.items():
        #invalid
        if cat not in normal_price:
            return -1
        if cat in special_price:
            div = nb // special_price[cat][0]
            res += special_price[cat][1] * div
            # reduce nb so it can be calculated together with products who dont have any special offer
            nb = nb % special_price[cat][0]
        # normal price
        res += nb * normal_price[cat]
    return res


