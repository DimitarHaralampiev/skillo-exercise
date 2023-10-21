student_bank_accounts = {}


def assign_bank_account(student_id, bank_account_id):
    # Check if the student already has a bank account
    if student_id in student_bank_accounts:
        # If they do, append the new bank account ID to their list of accounts
        student_bank_accounts[student_id].append(bank_account_id)
    else:
        # If not, create a new list with the bank account ID
        student_bank_accounts[student_id] = [bank_account_id]


command = input('Please enter command (Add/Stop) ')

while command != 'Stop':

    if command == 'Add':
        student, bank_account = input('Please enter student name and bank account ').split()
        assign_bank_account(student, bank_account)
    else:
        print('Incorrect command')

    command = input('Please enter command (Add/Stop) ')

print(student_bank_accounts)
