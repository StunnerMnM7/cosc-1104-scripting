'''
Assignment_1
Mihir Mane
100947380
'''

usernames = []
available_storage = []

def create_user(user_name, storage:float = 0):
    if user_name in usernames:
        print("Username already exists. Try choosing a different username")
        return False
    if not user_name.strip():
        print("Username cannot be blank")
        return False
    if storage <= 0:
        print("Storage must be a positive number.")
        return False
    usernames.append(user_name)
    available_storage.append(storage)
    print(f"User '{user_name}' created with {storage}GB of storage.")
    return True

def delete_user(user_name):
    if user_name not in usernames:
        print("Username not found.")
        return False
    index = usernames.index(user_name)
    usernames.pop(index)
    available_storage.pop(index)
    print(f"User '{user_name}' deleted successfully.")
    return True

# Upload user files in list format
def upload_file(user_name, filename, filesize:float = 0):
    if user_name not in usernames:
        print("Username not found.")
        return False
    uni = usernames.index(user_name)
    if filesize > available_storage[uni]:
        print(f"Not enough space to upload '{filename}'. You have {available_storage[uni]}GB available.")
        return False
    available_storage[uni] -= filesize
    print(f"'{filename}' uploaded successfully. Remaining storage: {available_storage[uni]}GB.")
    return True

# Display accounts in a list format
def display_accounts():
    if not usernames:
        print("No user accounts found.")
    else:
        print("User accounts and available storage:")
        for i in range(len(usernames)):
            print(f"Username: {usernames[i]}, Available Storage: {available_storage[i]}GB")

def positive_integer(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return float(value)
        print("Invalid input. Please enter a positive number.")

# Call funtions with flow
def main():
    while True:
        print("\nCloud Storage System Menu:")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. Upload File")
        print("4. Display All Accounts")
        print("5. Exit")
        
        choice = input("Enter your choice from 1-5: ")
        
        if choice == '1':
            username = input("Enter a username: ")
            storage = positive_integer("Enter the available storage in GB: ")
            create_user(username, storage)
        
        elif choice == '2':
            username = input("Enter the username to delete: ")
            delete_user(username)
        
        elif choice == '3':
            username = input("Enter your username: ")
            filename = input("Enter the filename: ")
            filesize = positive_integer("Enter the file size in GB: ")
            upload_file(username, filename, filesize)
        
        elif choice == '4':
            display_accounts()
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option 1-5.")

if __name__ == "__main__":
    main()
