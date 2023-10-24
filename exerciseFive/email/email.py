class Email:

    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

    def __ne__(self, other):
        return self.email != other.email


email_one = input('Please enter first email ')
email_two = input('Please enter second email ')
email_three = input('Please enter third email ')

email_first = Email(email_one)
email_second = Email(email_two)
email_third = Email(email_three)

print("Email one and Email two are equal:", email_one == email_two)  # True
print("Email one and Email three are equal:", email_first == email_third)  # False


print("Email one and Email two are not equal:", email_first != email_second)  # False
print("Email one and Email three are not equal:", email_first != email_third) # True