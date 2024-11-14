'''
In-Class#4 Nov 1st, 2024
COSC 1104-01 Scripting
Mihir Mane: 100947380
Zuhaib Khan: 100935821
'''

import requests
import json

# Retrieve EC2 data from a URL or local file
def retrieve_ec2_data(url=None, file_path=None):
# file_path = '"M:\Git\Repositories\cosc-1104-scripting\group-1_activities\In-class_4\ec2_instance_types.json'
    try:
        if url:
            response = requests.get(url)
            response.raise_for_status()  
            return response.json()  
        elif file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            print("No data path specified.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check the file format.")
    except FileNotFoundError:
        print("Error: File not found. Ensure the file path is correct.")

# Extract vCPU and memory values from an instance
def get_vcpu_memory(instance):
    vcpu_str = instance['vcpu'].split()[0]
    memory_str = instance['memory'].split()[0]
    vcpu = int(vcpu_str)
    memory = float(memory_str)
    return vcpu, memory

# Get valid user input with data type validation
def get_user_input(prompt, data_type=int):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return None
        try:
            return data_type(user_input)
        except ValueError:
            print(f"Please enter a valid {data_type.__name__}.")

# Filter instances based on user criteria
def filter_instances(ec2_data, min_cpu=None, max_cpu=None, min_memory=None, max_memory=None):
    results = []
    for instance in ec2_data:
        cpu, memory = get_vcpu_memory(instance)
        if (min_cpu is None or cpu >= min_cpu) and \
           (max_cpu is None or cpu <= max_cpu) and \
           (min_memory is None or memory >= min_memory) and \
           (max_memory is None or memory <= max_memory):
            results.append({
                "name": instance["name"],
                "cpu": cpu,
                "memory": memory
            })
    return results

# Main function to run the program
def main():
    # Use the raw URL format for GitHub to access the JSON content directly
    url = "https://github.com/StunnerMnM7/cosc-1104-scripting/blob/main/ec2_instance_types.json"
    file_path = "M:/Git/Repositories/cosc-1104-scripting/ec2_instance_types.json"
    ec2_data = retrieve_ec2_data(url= url, file_path= file_path)
    # User input
    min_cpu = get_user_input("Enter minimum required CPU count: ", int)
    max_cpu = get_user_input("Enter maximum required CPU count: ", int)
    min_memory = get_user_input("Enter minimum required memory in GB: ", float)
    max_memory = get_user_input("Enter maximum required memory in GB: ", float)
    # Data filtring
    filtered_instances = filter_instances(ec2_data, min_cpu, max_cpu, min_memory, max_memory)
    print("\nEC2 Instances available with aforementioned config:")
    print(f"{'Instance Name':<17}{'CPUs':<7}{'Memory (GB)':<18}")
    print("-" * 34)
    
    # Display instances in formatted style
    for instance in filtered_instances:
        print(f"{instance['name']:<18}{instance['cpu']:<8}{instance['memory']:<15}")

if __name__ == "__main__":
    main()
