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
    normal_price = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }
    # one pass to store
    # we can calculate initial pricing with E and remove free Bs from the dict
    for i in skus:
        if i not in normal_price:
            return -1
        catagory[i] += 1

    buy_get_free_mapping = {
        ("E", 2): ("B", 1),
        ("F", 3): ("F", 1),
        ("N", 3): ("M", 1),
        ("R", 3): ("Q", 1),
        ("U", 4): ("Q", 1),
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
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 150)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3)]
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

