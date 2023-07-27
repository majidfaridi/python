
def findindex(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i

    print("The traget element you are searching is not exist inside the list!")
    return -1 

