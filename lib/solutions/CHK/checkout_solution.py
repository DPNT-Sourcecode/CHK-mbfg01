

# noinspection PyUnusedLocal
# skus = unicode string

#  greedy

# input string format? csv? or just like 1A2B3C ??
def checkout(skus):
    mapping = 

    #validate input
    l = len(skus)
    if l % 2:
        return -1
    for i in range(0, l, 2):
        if not skus[i].isdigit():
            return -1
        nb = 


