*\
Grades:
85<A
70<B
60<C 
45<D 
45>F  
*\
    

    
num_subjects = int(input("Enter the number of subjects: "))    
grades_list = []

# Loop to iterate through the number of subjects
for i in range(num_subjects)

# Calculate avg Grade
avg = calculate_grade(grades_list)

# Get the letter grade of the average
letter_grade = get_letter_grade(avg)

# Display the results 
print(f"The average grade is: {avg:.2f}")
print(f"The grade is: {}") 