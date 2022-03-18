from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

#  greedy
# still greedy algorithm

# input string format? csv? or just like 1A2B3C ??

# is empty basket as illegal input? it should return 0 instead of -1 I guess
# Maybe I didn't save? the test cases seems fine but shows error after deployment

def checkout(skus):
    catagory = defaultdict(lambda: 0)
    ALLOWED_CAT = ("A", "B", "C", "D", "E", "F", "G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z")
    # one pass to store
    # we can calculate initial pricing with E and remove free Bs from the dict
    for i in skus:
        if i not in ALLOWED_CAT:
            return -1
        catagory[i] += 1

    buy_get_free_mapping = {
        ("E", 2): ("B", 1),
        ("F", 3): ("F", 1)
    }

    for k, v in buy_get_free_mapping.items():
        cat_from, nb_from = k
        cat_to, nb_to = v
        if catagory[cat_from] < nb_from:
            continue
        if cat_to in catagory:
            catagory[cat_to] -= (catagory[cat_from] // nb_from) * nb_to

    #price mapping
    # ordered 
    special_price = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)]
    }
    normal_price = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 50,
        "H": 30,
        "I": 20,
        "J": 15,
        "K": 40,
        "L": 10,
        "M": 50,
        "N": 30,
        "O": 20,
        "P": 15,
        "Q": 40,
        "R": 10,
        "S": 50,
        "T": 30,
        "U": 20,
        "V": 15,
        "W": 40,
        "X": 10,
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }
    # fianl result
    # calculate E and remove it from the dict
    res = 0
    for k, _ in buy_get_free_mapping:
        nb_e = catagory.pop(k, 0)
        res += nb_e * normal_price[k]

    for cat ,nb in catagory.items():
        #invalid
        if cat not in normal_price:
            return -1
        if cat in special_price:
            for offer in special_price[cat]:
                div = nb // offer[0]
                res += offer[1] * div
                # reduce nb so it can be calculated together with products who dont have any special offer
                nb = nb % offer[0]
        # normal price
        res += nb * normal_price[cat]
    return res








