
def distributeCandies(candyType):
    count = len(candyType)
    dif_types = len(set(candyType))
    return min(count // 2, dif_types)

candyType = [6,6,6,6]
print(distributeCandies(candyType))