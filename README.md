FTP Brute Force Tool with File Retrieval

This program is designed to perform brute force attacks on FTP servers to test the security of the system. It attempts to log in using combinations of usernames and passwords provided in separate text files. Additionally, it has the capability to retrieve files from the target FTP server. Written in Python3.

Usage:
1. Prepare two text files containing lists of usernames and passwords, respectively. Each username and password should be on a separate line.
2. Run the program and provide the IP address of the target FTP server when prompted.
3. The program will iterate through each combination of username and password, attempting to log in to the FTP server.
4. If a successful login is found, the program will try to retrieve the /etc/passwd file from the server and save it locally as "passwd.txt".
5. After completion, review the "passwd.txt" file to analyze the retrieved data.

Note:
- Use this program responsibly and only on systems you have explicit permission to test.
- Brute forcing FTP servers without authorization is illegal and unethical.
- Tested on vsftpd: version 3.0.3


Author:
Michał Botuliński
