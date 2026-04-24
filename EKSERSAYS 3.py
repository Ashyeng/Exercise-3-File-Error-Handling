
try:

    username = input("Enter username: ")
    age = int(input("Enter age: "))

     
    file = open("users.txt", "a")
    file.write(username + " - " + str(age) + "\n")
    file.close()

    
    print("\nSaved Users:")
    file = open("users.txt", "r")
    for line in file:
        print(line.strip())
    file.close()

except ValueError:
    print("Error: Age must be a number.")

except Exception as e:
    print("Error:", e)

finally:
    print("\nSystem complete.")