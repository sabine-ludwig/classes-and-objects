class Person:
    
    def __init__(self, name, passed_in_amount):
        self.name = name
        self.passed_in_amount = passed_in_amount

# Method #1 Remove money from the account balance by subtracting the total amount by an amount 
# passed in via a parameter

    def send_transfer(self, amount):
        if amount > self.passed_in_amount:
            print("Insuffiecient funds available.")
        else:
            self.passed_in_amount -= amount 
            print(f"Your new total is ${self.passed_in_amount}.")
            return self.passed_in_amount

# Method #2: Add money to the account balance of the current object.

    def receive_transfer(self, name, amount):
        self.passed_in_amount += amount
        print(f"Transfer from {name.title()} successful. Your new balance is ${self.passed_in_amount}.")
        return self.passed_in_amount