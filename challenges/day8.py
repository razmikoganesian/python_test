import random
import string
import getpass

# password = input("Please enter a password").strip()

def check_password(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short password, minumum 8 symbols")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter") 
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing cpecial character")
    return issues
     
def reccomend_new_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    # r = random.choice(chars)
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter a password: ")
issues = check_password(password)

if not issues:
    print("You choose strong password!")
else: 
    print("You chose weak password")
    for issue in issues:
        print(f"- {issue}")

suggestion = reccomend_new_password()
print("\n suggenting you a strong password")
print(suggestion)