# name="GibHon ADhiKArI"

# print(name.capitalize())

student_profiles = {
    "std_001": {
        "name": "Alex",
        "math_score": 85,
        "science_score": 90,
        "percentage": 87.5
    },
    "std_002": {
        "name": "Jordan",
        "math_score": 78,
        "science_score": 82,
        "percentage": 80.0
    },
    "std_003": {
        "name": "Sam",
        "math_score": 92,
        "science_score": 88,
        "percentage": 90.0
    }
}
sorted_profiles = {k: v for k, v in sorted(student_profiles.items(), 
                                          key=lambda x: x[1]["percentage"], 
                                          reverse=True)}


rank=0
for std_id, profile in sorted_profiles.items():
    print("----------------------------")
    rank+=1
    print(f'Rank :{rank}')
    for key, value in profile.items():
        if key=="name":
            print(f"Name: {value}")
        elif key=="math_score":
            print(f"Math Score: {value}")
        elif key=="science_score":
            print(f"Science Score: {value}")
        else:
            print(f"Percentage: {value}%")    
