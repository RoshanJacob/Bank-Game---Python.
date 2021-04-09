
class Bank(object):
    def __init__(self, cardNumber, pinNumber, balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balanceLeft = balance

    def verifyPerson(self):
        print(self.cardNumber)
        print(self.pinNumber)
        if(self.cardNumber == 3248):
            if(self.pinNumber == 2394):
                return True
        else:
            return False

    def withdrawMoney(self, amountToTake):
        if(self.amountToTake > self.balanceLeft):
            print("Oh no! It seems you have tried to withdraw more money than is left!")
        else:
            return self.balanceLeft - self.amountToTake


def main():
    # cardNumber = int(12498)
    # pinNumber = int(19384)

    card = int(input("Write your card number here! : "))
    pin = int(input("Write your pin number here! : ")


    amountRemaining=110398

    testPerson=Bank(card, pin, amountRemaining)

    if(testPerson.verifyPerson() == True):
        withdraw=int(input("How much do you want to take? :"))
        print("You have" + " " + str(testPerson.withdrawMoney(withdraw)) +
              " " + "left in your account")
    else:
        print("Oh! You have entered the wrong pin or card number!")


main()
