from datetime import datetime


class Wallet:

    total = 0

    def deposit(self, amount):
        self.total = self.total + amount

    def withdraw(self, amount):
        self.total = self.total - amount

    def show_total(self):
        print("["+datetime.now().strftime("%d/%m/%Y %H:%M") + "] W porfelu: " + str(self.total))
