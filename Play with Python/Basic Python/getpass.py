from getpass import *

username = getpass("Enter the username \n")
pwd = getpass("Enter the password \n")

if (username=="kamal") and (pwd=="sir"):
	print("Username is ", username)
	print("Password is", pwd)
	print("Success")
else :
	print("Username annd Password is Invalid") 