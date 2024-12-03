from bank_accounts import *

Dave = BankAccount (1000, "Dave")
Sarah = BankAccount (2000, "Sarah")


Dave.getBalance()
Sarah.getBalance()

Sarah.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(1000, Sarah)
Dave.transfer(100, Sarah)

Jim = InterestRewardAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sarah)