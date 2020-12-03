str_expenses = open('input.txt', 'r').read().split('\n')
expenses = [int(str_expense)
            for str_expense in str_expenses if len(str_expense) > 0]

for expense in expenses:
    if 2020 - expense in expenses:
        print(expense * (2020 - expense))
        break
