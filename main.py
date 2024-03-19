#enter value of all variables

Employees_name = input("Enter the name of the employee: ")
Number_shifts = int(input("Enter the number of shifts: "))
Number_transactions = int(input("Enter the number of transactions: "))
Dollar_value = float(input("Enter the dollar value of each transaction: "))

#figuring out the productivity score of an employee
Productivity_score = (Dollar_value / Number_transactions) / Number_shifts
bonuses = float(0)


if Productivity_score <= 30:
  bonuses = 50
else:
  if Productivity_score >= 31 and Productivity_score <= 69:
    bonuses = 75
  else:
    if Productivity_score >= 70 and Productivity_score <= 199:
      bonuses = 100
    else:
      if Productivity_score >= 200:
        bonuses = 200
      else:
        print("No Bonuses this week")

#printing the results
print("                                                   ")
print("Employee Name: ", Employees_name)
print("Employee Bonus: $", bonuses)

