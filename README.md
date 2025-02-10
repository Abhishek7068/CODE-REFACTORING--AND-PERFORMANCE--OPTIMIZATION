# CODE REFACTORING AND PERFORMANCE OPTIMIZATION

COMPANY NAME: CODDETECH IT SOLUTIONS

NAME: ABHISHEK MAURYA

INTERN ID: CT08NCA

DOMAIN: SOFTWARE DEVELOPMENT

DURATION: 1 MONTHS

MENTOR: NEELA SANTOSH

## DESCRIPTION
The BankAccount class is a well-structured Python implementation that encapsulates essential banking operations such as account creation, deposits, withdrawals, and balance retrieval. It adheres to the principles of object-oriented programming (OOP), particularly encapsulation and error handling, ensuring safe and controlled interactions with an account. Additionally, it employs logging for transaction tracking and debugging, making it a robust and maintainable solution.

### Class Definition and Constructor
The BankAccount class is initialized with two attributes:

1. _name: A private attribute storing the account holder’s name.
2. _balance: A private attribute maintaining the account balance, defaulting to zero.

The constructor method (__init__) initializes these attributes and sets up logging using:
. The logging level is set to INFO, meaning all deposit and withdrawal operations will be logged.
. The format includes a timestamp, which is useful for tracking transactions.

### Encapsulation and Property Methods
Encapsulation is implemented through getter methods (@property), ensuring controlled access to private attributes:

### Deposit Method
The deposit method allows users to add money to their account:
1. Validation: The deposit amount must be positive.
2. Logging: Each deposit is recorded, ensuring transaction history.
3. Balance Update: The deposited amount is added to _balance.

### Withdraw Method
The withdraw method allows users to withdraw funds while handling insufficient balances:
1. Validation: Ensures the withdrawal amount is positive.
2. Insufficient Funds Handling: If the withdrawal exceeds the available balance, a ValueError is raised, and a warning is logged.
3. Logging: The withdrawal and resulting balance are logged.

### String Representation (__str__)
The __str__ method provides a readable representation of the account: This ensures that print(account) displays meaningful information.

### Main Function Execution
The main() function demonstrates class usage:
1. Creates an account for “John Doe” with an initial balance of $1000.
2. Performs transactions (depositing $500, withdrawing $200).
3. Attempts to withdraw $2000, triggering an error due to insufficient funds.
4. Handles errors using try-except, ensuring the program does not crash.
5. Uses finally to display the final balance, ensuring execution even after an error.

### Benefits of the Code
✔ Encapsulation: Private attributes with property methods prevent direct modification.
✔ Error Handling: Prevents invalid transactions and warns about insufficient funds.
✔ Logging: Tracks all financial transactions for accountability.
✔ Maintainability: Clean, modular, and easy to extend.

### Conclusion
This BankAccount class is an optimized, refactored, and well-structured implementation that follows OOP principles, error handling best practices, and transaction logging. It ensures security, data integrity, and ease of maintenance, making it a reliable banking system component.

## OUTPUT

![Image](https://github.com/user-attachments/assets/191babd2-4949-4d1d-b7b7-23b792ae8403)
