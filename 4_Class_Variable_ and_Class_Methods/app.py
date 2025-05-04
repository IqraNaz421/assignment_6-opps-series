 
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    # Class variable
    bank_name = "Default Bank"

    # Class method to change the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Create two instances of the Bank class
account1 = Bank()
account2 = Bank()

# Access class variable from both instances
print("Before changing bank name:")
print("Account1 Bank:", account1.bank_name)
print("Account2 Bank:", account2.bank_name)

# Change the bank name using the class method
Bank.change_bank_name("National Trust Bank")

# Access class variable again from both instances
print("\nAfter changing bank name:")
print("Account1 Bank:", account1.bank_name)
print("Account2 Bank:", account2.bank_name)
