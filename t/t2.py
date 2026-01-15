student_profiles={}
student_id=1

while True:
    name=input("Enter the student's name:")
    name_components=name.split()
    name_components=[comp.capitalize() for comp in name_components]
    name=" ".join(name_components)

    
    math_score=int(input("Enter the student's math marks:"))
    while math_score<0 or math_score>100:
        print("The inputed score is invalid. Please input the marks again.")
        math_score=int(input("Enter the math masks :"))
        
    science_score=int(input("Enter the student's science marks:"))
    while science_score<0 or science_score>100:
        print("The inputed score is invalid. Please input the marks again.")
        science_score=int(input("Enter the science masks :"))
        
    percentage=(math_score+science_score)/2

    student_profiles[student_id]={
    "name": name,
    "math_score": math_score,
    "science_score": science_score,
    "percentage": percentage
    }
    
    student_id+=1
    
    input_continuity_command=input(' Enter "q" to finish entering data: ')
    if input_continuity_command=="q":
        break
    
sorted_profiles = {k: v for k, v in sorted(student_profiles.items(), 
                                          key=lambda x: x[1]["percentage"], 
                                          reverse=True)}


rank=0
science_summation=0
math_summation=0
percentage_summation=0
for std_id, profile in sorted_profiles.items():
    print("----------------------------")
    rank+=1
    print(f'Rank :{rank}')
    for key, value in profile.items():
        if key=="name":
            print(f"Name: {value}")
        elif key=="math_score":
            math_summation+=value
            if value<32:
                print(f"Math Score: {value}*------",end=" ")
            else:
                print(f"Math Score: {value}------",end=" ")
            
        elif key=="science_score":
            science_summation+=value
            if value<32:
                print(f"Science Score: {value}*------")
            else:
                print(f"Science Score: {value}------")
        else:
            percentage_summation+=value
            if value<32:
                print(f"Percentage: {value}%")
                print("The student failed!!!")
            else:
                print(f"Percentage: {value}%")   
                print("The student passed!")

no_of_students=len(student_profiles)
avg_math_score=math_summation/no_of_students
avg_science_score=science_summation/no_of_students
avg_percentage=percentage_summation/no_of_students

print(f"The average score of class in math is {avg_math_score}")
print(f"The average score of class in science is {avg_science_score}")
print(f"The average percentage of class is {avg_percentage}")