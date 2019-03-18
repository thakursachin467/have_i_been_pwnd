import hashlib
import requests
user_exit = True


def make_pwnd_call(password, hashed_password):
    url = f'https://api.pwnedpasswords.com/range/{password}'
    found = False
    response = requests.get(url=url)
    data = response.text
    pwnd_array = data.split("\r\n")
    for pwnd_pwd in pwnd_array:
        if pwnd_pwd[0:35] == hashed_password.upper():
            print(
                f'this password appeard {pwnd_pwd[36:]} times in our database')
            found = True
    if found != True:
        print("hurray this password is not in our database")

def password_lookup():
  password = input()
  digest = hashlib.sha1(password.encode())
  hashed_password = digest.hexdigest()
  pwnd_password = hashed_password[0:5]
  make_pwnd_call(pwnd_password, hashed_password[5:])

while user_exit:
    print("1) For password lookup")
    print("2) Exit")
    user_input = input()
    if user_input == "1":
        password_lookup()
    elif user_input == "2":
        user_exit = False
