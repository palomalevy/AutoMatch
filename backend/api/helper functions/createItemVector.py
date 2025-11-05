import numpy as np
# create binary vectors for users and car listings here

MANUFACTURERS = [
    'ford', 'honda', 'toyota', 'chevrolet', 'nissan', 'bmw', 'mercedes-benz', 
    'subaru', 'volkswagen', 'jeep'
] #this is gonna change (right, Palo? :))

PRICE_RANGE = (1000.0, 150000.0)
YEAR_RANGE = (1990.0, 2025.0)

def create_feature_vector(data):
    
    #Creates a feature vector from either a Listing model object or a user's dictionary
    
    
    # Use .get() for dicts (user prefs) and getattr() for objects (if we use the API directly)
    is_object = not isinstance(data, dict)
    
    def get_val(field_name):
        if is_object: #if it is an object, then use the getattr
            return getattr(data, field_name, None)
        else: #if it is a dictionary
            return data.get(field_name, None)

    final_vector = []
    
    # 1. Normalize Price
    price = get_val('price')
    norm_price = _normalize(price, PRICE_RANGE)
    final_vector.append(norm_price)
    
    # 2. Normalize Year
    year = get_val('year')
    norm_year = _normalize(year, YEAR_RANGE)
    final_vector.append(norm_year)
    
    # 3. One-hot encode Manufacturer
    manufacturer = get_val('manufacturer')
    manu_vector = _one_hot(manufacturer, MANUFACTURERS)
    final_vector.extend(manu_vector)
    
    
    # we need to add more here!
    
    return np.array(final_vector)


# --- HELPER FUNCTIONS ---

def _normalize(value, min_max_range):
    #scales a numerical value to be between 0 and 1.
    if value is None:
        return 0.0  # Default for missing data
    
    min_val, max_val = min_max_range
    #clamp the value and make sure it is within the range
    value = max(min_val, min(value, max_val))
    
    #perform min-max scaling between 0.0 and 1.0
    return (value - min_val) / (max_val - min_val)

def _one_hot(value, known_categories):
    #creates an encoded vector with all the non numerical attributes like the mode, make or price :)
    vector = [0.0] * len(known_categories)
    if value in known_categories:
        index = known_categories.index(value)
        vector[index] = 1.0
    return vector