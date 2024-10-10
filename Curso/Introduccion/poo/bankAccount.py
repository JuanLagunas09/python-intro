class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Depósito de {amount} realizado con éxito")
            print(f"Nuevo saldo: {self.balance}")
        else:
            print("Cuenta inactiva, consulta a tu banco")
    
    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Retiro de {amount} realizado con éxito")
                print(f"Nuevo saldo: {self.balance}")
            else:
                print("Saldo insuficiente")
        else:
            print("Cuenta inactiva, consulta a tu banco")

    def deactivate_account(self):
        self.is_active = False
        print("Cuenta desactivada")
    
    def activate_account(self):
        self.is_active = True
        print("Cuenta activada")
        
    def check_balance(self):
        if self.is_active:
            print(f"Saldo actual: {self.balance}")
        else:
            print("Cuenta inactiva, consulta a tu banco")
            
account_1 = BankAccount("Juan", 1000)
account_2 = BankAccount("Maria", 2000)

account_1.check_balance()
account_1.deposit(500)
account_1.withdraw(200)
account_1.deactivate_account()
account_1.withdraw(500)
print("--------------------")
account_2.check_balance()
account_2.deposit(1000)
account_2.withdraw(500)
account_2.check_balance()

            