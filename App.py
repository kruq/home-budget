from Models import Wallet, User

wallet = Wallet()

adam = User("Adam")
kasia = User("Kasia")

wallet.deposit(adam, 500)
wallet.deposit(kasia, 500)
wallet.withdraw(kasia, 200)
wallet.show_total()
wallet.show_operations()