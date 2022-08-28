def palindrom(slowo):
    for i in range(len(slowo)):
        if slowo[i]==slowo[-i-1]:
            pass
        else:
            return False
    return True
test="kobylamamalybok"
print(palindrom(test))