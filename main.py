def palindrom(slowo):
    for letter in slowo:
        if slowo[0]==slowo[-1]:
            pass
        else:
            return False
    return True
test="kobylamamalybok"
print(palindrom(test))