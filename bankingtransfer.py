"""
This is a banking script that should automatically transfer $200 from the savings
to the checking account if the checking is at or below $50
"""


#User's expenses in a dict
expenseType = ["Food", "Auto Loan", "TV/Cable", "CellPhone"]
amount = [500, 250, 100, 100]

#Zip function to merge lists into a dictionary
monthlyExpenses = dict(zip(expenseType, amount))


#Function for the checking account
def checkingAccount():

    #Constant variables for money in the checking and savings account
    SAVINGS = 15000
    CHECKING = 2000
    savingsWithdrawal = []

    #Sentinel variable to start the program
    startProgram = 0

    #start the program and use an if/else statement to ask the user how much they want to withdraw
    while startProgram < 1:
        print("Your current balance is ${}".format(CHECKING))
        withdraw = int(input("How much would you like to withdraw from your account? $"))
        expense = input("Which monthly expense would you like to check? ")
        if withdraw <= CHECKING:
            CHECKING -= withdraw
            print(str(expense), "expense is $", monthlyExpenses[expense])


            #If their balance gets to $50 or below, transfer money from the savings to the checking account
            while CHECKING <= 50 and SAVINGS >= 200:
                print("You currently have ${} in your account.  Transferring from Savings.".format(CHECKING))
                SAVINGS = SAVINGS - 200
                savingsWithdrawal.append(200)
                CHECKING += 200
                print("Your new balance is {}".format(CHECKING))
        else:
            print("Sorry! You cannot withdraw anymore as your current balance is ${}.".format(CHECKING))


print(checkingAccount())
