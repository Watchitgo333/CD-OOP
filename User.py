class User:
    bank_name = "Kitty Kredit Union"
    motto = "Put your 'dough' in paws you trust!"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, User, amount):
        self.account_balance -= amount
        User.account_balance += amount
        print(f"Transfer successful. {self.name} New Balance: ${self.account_balance}")
        print(f"{User.name} New Balance: ${User.account_balance}")


print(User.bank_name, "|", User.motto)

nigel = User("Nigel 'Nidew' Brusky", "Nididgeridoo@gmail.com")
phillip = User("Phillip 'Mr. Pips' Brusky", "SweetPea@gmail.com")
marcus = User("Marcus 'Chief Beef' Brusky", "ChairmanBarron@gmail.com")

nigel.make_deposit(300)
nigel.make_deposit(150)
nigel.make_deposit(50)
nigel.make_withdrawal(100)
nigel.display_user_balance()

phillip.make_deposit(240)
phillip.make_deposit(260)
phillip.make_withdrawal(250)
phillip.make_withdrawal(200)
phillip.display_user_balance()

marcus.make_deposit(10000)
marcus.make_withdrawal(400)
marcus.make_withdrawal(100)
marcus.display_user_balance()

nigel.transfer_money(marcus, 100)