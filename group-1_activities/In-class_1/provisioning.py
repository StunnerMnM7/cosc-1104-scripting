'''
Course(1108-01): Scripting
Group: 01 , Date: 09/27/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
# Description: This script is a provisioning system, allowing users to request CPU cores and memory.
'''
#Total Resources
total_cpu = 32
total_memory = 64
required_cpu = int(input("Enter number of CPUs required: "))
required_mem = float(input("Enter amount of memory requred in GB: "))
available_cpu = 0
available_mem = 0

while True:
    if required_cpu <= 0 or required_mem <= 0:
        print("Invalid resource request. Resource request cannot be negative.")y
        break
        
    elif required_cpu > total_cpu or required_mem > total_memory:
        print("Resources exceeds availability limit.\n")
        print(f"Available Resources: CPU cores - {total_cpu} | Memory - {total_memory}\n")
        break
            
    elif required_cpu <= total_cpu and required_mem <= total_memory: 
        available_cpu = total_cpu - required_cpu
        available_mem = float(total_memory - required_mem)
        print(f"CPU cores alloted: {required_cpu} Memory alloted: {required_mem}\n")
        print(f"Available Resources: CPU cores - {available_cpu} | Memory - {available_mem}\n")   
        break
    
