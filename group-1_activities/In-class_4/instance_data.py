import json

def load_ec2_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Getting required information/values
def get_vcpu_memory(instance):
    vcpu_str = instance['vcpu'].split()[0] 
    memory_str = instance['memory'].split()[0]
    vcpu = int(vcpu_str)
    memory = float(memory_str)
    return vcpu, memory

# User input correction
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

# Main
def main():
    filename = 'M:\Git\Repositories\cosc-1104-scripting\group-1_activities\In-class_4\ec2_instance_types.json'
    ec2_data = load_ec2_data(filename)
    min_cpu = get_user_input("Enter minimum required CPU count: ",int)
    max_cpu = get_user_input("Enter maximum required CPU count: ", int)
    min_memory = get_user_input("Enter minimum required memory in GB: ", float)
    max_memory = get_user_input("Enter maximum required memory in GB: ",float)
    filtered_instances = filter_instances(ec2_data, min_cpu, max_cpu, min_memory, max_memory)
    print("\EC2 Instances available with aforementioned config:")
    print(f"{'Instance Name':<17}{'CPUs':<7}{'Memory(GB)':<18}")
    print("-" * 30)
    
    # Print instances in formatted style 
    for instance in filtered_instances:
        print(f"{instance['name']:<18}{instance['cpu']:<7}{instance['memory']:<15}")

if __name__ == "__main__":
    main()
