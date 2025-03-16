# ATM-CONSOLE-BASED-PROJECT

## Overview
This is a simple ATM management system implemented in Python. The program allows users to perform various banking operations such as withdrawals, deposits, PIN generation, mini statements, balance inquiries, fund transfers, and PIN changes.

## Features
- **Withdrawal**: Users can withdraw money from their account after PIN authentication.
- **Deposit**: Users can deposit money into their account.
- **PIN Generation**: Users can set a new PIN for their account.
- **Mini Statement**: Displays the account holder's details and balance.
- **Check Balance**: Users can check their current account balance.
- **Fund Transfer**: Users can transfer funds to another account.
- **Change PIN**: Users can change their PIN after authentication.
- **Exit**: Allows users to exit the application safely.

## Requirements
- Python 3.x

## How to Run
1. Install Python 3.x if not already installed.
2. Clone this repository:
   ```sh
   git clone <repository_url>
   ```
3. Navigate to the project directory:
   ```sh
   cd ATM-Management-System
   ```
4. Run the script:
   ```sh
   python atm.py
   ```

## Usage
1. Run the script and follow the on-screen instructions.
2. Enter your account number and PIN for authentication.
3. Select an operation from the menu.
4. Follow the prompts to complete the transaction.
5. Choose 'Exit' when you are done.

## Account Data (Sample)
The program contains predefined accounts with the following format:
```
accounts = {
    1001: ["Deepak", "02-05-2004", 10000, 2304],
    1002: ["Aasrith", "03-01-2004", 20000, 2323],
    ...
}
```
Each account has:
- **Name**
- **Date of Birth**
- **Account Balance**
- **PIN**

## Disclaimer
This program is a basic simulation of an ATM system and should not be used for real financial transactions.

## License
This project is licensed under the MIT License.

