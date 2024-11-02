'''
Mihir Mane - 100947380
MidTerm Test - 10/15/2024
This program is similar to an account counter for servers,
where max constants are pre defined. 

'''
# Predefined Constants and Inputs from user.
total_servers = 3
max_total_accounts = 50
accounts_server_1 = int((input("Enter number of account to be allocated to Server 1: ")))
accounts_server_2 = int((input("Enter number of account to be allocated to Server 2: ")))
accounts_created = accounts_server_1 + accounts_server_2
remaining_accounts = max_total_accounts - accounts_created

# Iterations
if accounts_created >= 50:
    print("You have exceeded the maximum allowable accounts.")
    remaining_accounts = 0
    accounts_created = 50
elif accounts_created == 50:
    print("There are no additional accounts allowed.")
else: 
    print(f"There are {remaining_accounts} accounts still available.")
print(f"Server 1 has {accounts_server_1} and Server 2 has {accounts_server_2}.\nThere are {accounts_created} accounts created in total and extras are discarded. \nRemaining accounts available for Server 3 are {remaining_accounts}")
end = input("To exit the program press 'x'")
if end == "x":
    print("Exiting the program.")
