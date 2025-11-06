import json
## Here you create user vector
## Should take in the paramenter of user id (to distinguish users)

## Vector (array) with 48 binary data points (42 cars, 3 price, 3 year)
## For each feature of "preferences", append a 1 if it is 1 and 0 if it is 0 (info in json ->)

## Function should work (meaning create accurate vector for any user id inputted)

## Remember to add safe guards in case an id does not exist or is not an int !!

## Okk let me know if u have any questions :)

def createUserVector(id):
    filepath = 'data/users.json'

    try:
        with open(filepath, 'r') as f:
            my_data_list = json.load(f)
        
        for user in my_data_list:
            
            if user['id'] == id:
                user_vector = []
                preferences = user['preferences']
                for key, value in preferences.items():
                    user_vector.append(value)
                return user_vector
        
        print(f"Error: User ID {id} not found.")
        return None    
    except FileNotFoundError:
        print(f"Error: the file {filepath} was not found")
        return None