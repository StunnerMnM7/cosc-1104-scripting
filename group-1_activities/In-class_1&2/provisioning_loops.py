''''
Course(1108-01): Scripting
Group: 01 , Date: 09/27/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
# Description: This script is a provisioning system with loops, it allowing users to request CPU cores and memory and stores their information.
'''

#Total Resources and constants
total_cpu = 16
total_memory = 32.0
allocated_resources = []
pending_requests = []
used_cores = 0
used_mem = 0

print(f"Total CPU cores: {total_cpu}")
print(f"Total memory in GB: {total_memory}")

while True:
    #user details and resources required
    username = input("Enter your username: ")
    required_cpu = int(input("Enter number of CPUs required: "))
    required_mem = float(input("Enter amount of memory requred in GB: "))
   
    if required_cpu <= 0 or required_mem <= 0:
        print("Invalid resource request. Resource request cannot be negative.")
        break
    
    if (required_cpu + used_cores <= total_cpu) and (required_mem + used_mem <= total_memory):
        #resources are available; allocate them
        allocated_resources.append([username, required_cpu, required_mem])
        used_cores += required_cpu
        used_mem += required_mem
        print(f"Resources allocated to {username}: {required_cpu} CPU cores and {required_mem} GB memory.\n")

    else:
        #resources added to pending requests
        pending_requests.append([username, required_cpu, required_mem])
        print(f"Request from {username} is pending due to insufficient resources.\n")
        
    another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
    if another_request != 'yes':
        break


#display Output
#available resources
print("\nAllocated Resources:")
print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<12}")
print("-" * 37)
for allocation in allocated_resources:
    print(f"{allocation[0]:<15}{allocation[1]:<10}{allocation[2]:<12}")
#pending requests
if pending_requests:
    print("\nPending Requests:")
    print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<12}")
    print("-" * 37)
    for request in pending_requests:
        print(f"{request[0]:<15}{request[1]:<10}{request[2]:<12}")
else:
    print("\nNo pending requests.")
