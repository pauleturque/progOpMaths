import math

def multiples(nb, nbOfMultiples):
    multiplesArray = []
    for k in range(2, nbOfMultiples):
        result = nb * k
        multiplesArray.append(result)
    print("The ", nbOfMultiples, " multiples of ", nb, " are :", multiplesArray)


def primeFactors(nb):
    div = 2
    factors = []
    while div <= nb:
        if nb % div == 0:
            factors.append(div)
            nb = nb // div
        else:
            div += 1
    print(factors)


def primeNumbers(lim):
    nb = 3
    firsts = []
    firsts.append(2)
    while nb < lim:
        k = 0
        while math.pow(firsts[k], 2) < nb and (nb % firsts[k]) != 0:
            k += 1
        if nb % firsts[k] == 0:
            firsts.append(nb)
        nb += 1
    print(firsts)
