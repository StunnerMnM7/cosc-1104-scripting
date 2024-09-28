'''
Course(1108-01): Scripting
Group: 01 , Date: 09/27/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
# Description: This script is a provisioning system, allowing users to request CPU cores and memory.
'''
#Total Resources
total_cpu = 8
total_memory = 32
required_cpu = int(input("Enter number of CPUs required: "))
required_mem = float(input("Enter amount of memory requred in GB: "))
available_cpu = 0
available_mem = 0

while True:
    if required_cpu <= 0 or required_mem <= 0:
        print("Invalid resource request. Resource request cannot be negative.")
        
    elif required_cpu > total_cpu or required_mem > total_memory:
        print("Resources exceeds availability limit.\n")
        print(f"Available Resources: CPU cores - {total_cpu} | Memory - {total_memory}\n")
            
    elif required_cpu <= total_cpu and required_mem <= total_memory: 
        available_cpu = total_cpu - required_cpu
        available_mem = float(total_memory - required_mem)
        print(f"CPU cores alloted: {required_cpu} Memory alloted: {required_mem}\n")
        print(f"Available Resources: CPU cores - {available_cpu} | Memory - {available_mem}\n")   
        break
    
    
    

'''
# provisioning.py
# Author: Mihir Mane
# Date: [Insert Date]

# Constants
TOTAL_CPU_CORES = 8  # Total number of CPU cores available
TOTAL_MEMORY_GB = 32.0  # Total amount of memory available in gigabytes (GB)

# User input
required_cpu_cores = int(input("Enter the number of required CPU cores: "))
required_memory_gb = float(input("Enter the amount of required memory in GB: "))

# Input validation
if required_cpu_cores < 0 or required_memory_gb < 0:
    print("Error: Resource requests cannot be negative.")
else:
    # Resource availability check
    if (required_cpu_cores <= TOTAL_CPU_CORES) and (required_memory_gb <= TOTAL_MEMORY_GB):
        print("Resources provisioned successfully.")
    else:
        print("Resource request exceeds capacity. Provisioning failed.")

    # Calculate remaining resources
    remaining_cpu_cores = TOTAL_CPU_CORES - required_cpu_cores if required_cpu_cores <= TOTAL_CPU_CORES else TOTAL_CPU_CORES
    remaining_memory_gb = TOTAL_MEMORY_GB - required_memory_gb if required_memory_gb <= TOTAL_MEMORY_GB else TOTAL_MEMORY_GB

    # Display remaining resources
    print(f"Remaining CPU cores: {remaining_cpu_cores}")
    print(f"Remaining memory: {remaining_memory_gb} GB")

'''