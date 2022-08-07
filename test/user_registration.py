import requests


for i in range(1000000):
    res = requests.post("http://localhost:5000/users", 
        {
            "first_name": f"Roberto{i+1}", 
    	    "last_name": "Medina", 
    	    "age": 23, 
    	    "e_mail": f"rm{i+1}@gmail.com", 
            "balance": 849942994, 
    	    "nif": f"525434345{i+1}", 
    	    "user_password": "1234"
        }
    )
    print(f"user - {i+1}")