S=[[],[],[],[],[],[],[],[],[]]

def put(S:list, name:str):
    bucket = 0
    for bucket in range(len(name)):
        bucket += ord(name[bucket])
    bucket = bucket % 10
    S[bucket].append(name)
    return 0

def isin(S:list, name:str) -> bool:
    bucket = 0
    for bucket in range(len(name)):
        bucket += ord(name[bucket])
    bucket = bucket % 10
    index = len(S[bucket]) - 1
    while index >= 0:
        if S[bucket][index] == name:
            return True
        index -= 1
    return False

