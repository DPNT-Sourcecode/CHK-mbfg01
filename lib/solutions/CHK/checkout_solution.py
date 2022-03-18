

# noinspection PyUnusedLocal
# skus = unicode string

#  greedy

# input string format? csv? or just like 1A2B3C ??

# is empty basket as illegal input? it should return 0 instead of -1 I guess
def checkout(skus):
    #price mapping
    special_price = {
        "A": (3, 130),
        "B": (2, 45)
    }
    normal_price = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    # fianl result
    res = 0

    #validate input
    l = len(skus)
    if l % 2:
        return -1
    for i in range(0, l, 2):
        # invalid
        if not skus[i].isdigit():
            return -1
        nb = int(skus[i])
        cat = skus[i+1]
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





