total_balance = 105246054   #fixed my balance
class InsufficientException(Exception):
    pass

class InvalidAmountException(Exception):
    pass

class CustomizedException:
    def __init__(self, total_balance):   #function 1
        self.total_balance = total_balance   #105246054

    def _check_balance(self):         #function 2
        return self.total_balance     #105246054(while checking balance the number will be return)

    def _withdraw_amount(self, withdraw_amt):
        try:
            if withdraw_amt <= 0:
                raise InvalidAmountException
            if withdraw_amt > self.total_balance:
                raise InsufficientException
            
            self.total_balance -= withdraw_amt
            return withdraw_amt
        
        except InvalidAmountException:
            print("Invalid amount. Please enter a positive value.")
        except InsufficientException:
            print("Insufficient balance.")
            
    def deposit(self,deposit_amt):     #function 3
        self.deposit_amt=deposit_amt
        print( " Amount deposited Successfully")
    def atm_simulation(self):          #function 4  (checking center) 
        
        while True:
            print("Select the purpose:")
            print("1. Balance Check")
            print("2. Withdrawal")
            print("3. Deposit")
            print("4. Exit")
            
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Current balance:", self._check_balance())
            elif choice == 2:
                withdraw_amt = int(input("Enter the withdrawal amount: "))
                self._withdraw_amount(withdraw_amt)
            elif choice == 3:
                deposit_amt = int(input("Enter the deposit amount: "))
                self.deposit(deposit_amt)
            elif choice==4:
                break
            else:
                print("Invalid choice. Please try again.")


atm_simulator = CustomizedException(total_balance)
atm_simulator.atm_simulation()
