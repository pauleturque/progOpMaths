from prodedures import *

choice = "Z"
while choice != "Q" and choice != "q":
    print("50 prime multiples..........1")
    print("Number's prime factors......2")
    print("50 prime numbers............3")
    print("Quit........................Q")
    choice = input("Choix : ")

    if choice == "1":
        nb = int(input("Please enter a number : "))
        nbOfMultiples = int(input("Please enter the number of multiples : "))
        multiples(nb, nbOfMultiples)
    elif choice == "2":
        nb = int(input("Please enter a number : "))
        primeFactors(nb)
    elif choice == "3":
        primeNumbers(50)
