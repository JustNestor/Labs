from random import randint


polindromes = []


def is_polindrome(integer):
    intg = list(str(integer))
    for num in range(len(intg)):
        if not intg[num] == intg[len(intg)-num-1]:
            return False
    return True


for i in range(1000):
    rint = randint(1, 1000)
    # print(f"Число {rint}, є поліндромом - {is_polindrome(rint)}")
    if is_polindrome(rint): polindromes.append(rint)


polindromes.sort()
print(polindromes)
print(f"Мінімальне: {min(polindromes)}")
print(f"Максимальне: {max(polindromes)}")

