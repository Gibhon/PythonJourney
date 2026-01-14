Info=[
    {"name":"Gibhon Adhikari",
     "first_name": "Gibhon",
     "last_name": "Adhikari",
     "age":17
     }
]



for i in range(len(Info)):
    if(Info[i]["age"]>=18 and Info[i]["age"]<=100):
        print(f"Hey {Info[0]["name"]}. We welcome you to our software")
    else:
        print(f"Hey {Info[0]["name"]}. You can unfortunately not access this content because you are just {Info[0]["age"]}")
        
