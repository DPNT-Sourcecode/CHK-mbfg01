

# noinspection PyUnusedLocal
# skus = unicode string

#  greedy

# input string format? csv? or just like 1A2B3C ??
def checkout(skus):
    #price mapping
    special_price = {
        "A": 130,
        "B": 45
    }
    normal_price = {
        "A": 50,
        "B": 30,
        "A": 20,
        "B": 15
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
        if cat in special_price
