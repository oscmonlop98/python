def mating_pairs(males: set, females: set):

    pairs_set = set()
    num = len(males)

    for i in range(num):
        pair_male = males.pop()
        pair_female = females.pop()
        pairs_set.add((pair_male,pair_female),)

    return(pairs_set)


malesSet = {'oscar','marcos','juan'}
femalesSet = {'ana','carla','juana'}

print(mating_pairs(malesSet,femalesSet))