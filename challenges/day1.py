import datetime

name = input("Enter your name?  ").strip()
age = input("How old are you?  ").strip()
city = input("City where you are living?  ").strip()
profession = input("What is your profession?  ").strip()
hobby = input("Do you have a hobby? Please indicated which one  ").strip()
current_date = datetime.date.today().isoformat()


intro_message = (
    f"Hello! Me name is {name}, I'm {age} years old and I live in {city}"
    f"I am {profession} and my hobby is {hobby}"
)

intro_message = intro_message + f"\n Loggen on :{current_date}"

border = "*" * 40
final_output = f"{border}\n{intro_message}\n{border}"
print(final_output)