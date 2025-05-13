correct_username="admin"
correct_password="12345"

attempts=1
max_attempts=3

while attempts<=max_attempts:
    username=input("Enter username:")
    password=input("Enter password:")
    if username==correct_username and password==correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials. Try again")
        attempts+=1

print("attempts:",attempts)
if attempts>=max_attempts:
    print("Too many failed attempts. Access denied...")