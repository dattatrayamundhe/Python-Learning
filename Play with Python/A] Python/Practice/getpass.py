from getpass import *

username = getpass("Enter the username \n")
pwd = getpass("Enter the password \n")

if (username=="anu") and (pwd=="260696"):
	print("Username is ", username)
	print("Password is", pwd)
	print("Success")
else :
	print("Username annd Password is Invalid") 