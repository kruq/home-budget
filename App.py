from Models.Wallet import *

wallet = Wallet()

wallet.deposit(100)
wallet.show_total()
wallet.deposit(150)
wallet.show_total()
wallet.deposit(70)
wallet.show_total()
wallet.withdraw(30)
wallet.show_total()

