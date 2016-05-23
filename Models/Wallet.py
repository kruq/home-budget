from datetime import datetime
from Models import Operation


class Wallet:

    operations = []
    total = 0

    def deposit(self, user, value):
        self.operations.append(Operation(user, value))
        self.total = self.total + value

    def withdraw(self, user, value):
        self.operations.append(Operation(user, -1 * value))
        self.total = self.total - value

    def show_total(self):
        print("[" + datetime.now().strftime("%d/%m/%Y %H:%M") + "] W porfelu: " + str(self.total))

    def show_operations(self):
        for o in self.operations:
            print("[" + datetime.now().strftime("%d/%m/%Y %H:%M") + "] " + o.user.name + ", kwota: " + str(o.value))
