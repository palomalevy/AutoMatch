# assign similarity scores to car listings here

from .cosineSimilarity import calculate_cosine_similarity
from .createItemVector import create_feature_vector

#import the Django database model. We have to set this up!
from ..models import Listing 

def find_similar_listings(user_preference_vector, top_n=20):
    #finds the 'top_n' most similar car listings from the database based on the user's preference vector
    
    #get all listings from the database
    # This is the "linear scan" that we mentioned (hopefully does not take 10,000 years)
    all_listings = Listing.objects.all()
    
    scored_listings = []
    
    #loops, converts, and scores every listing
    for listing in all_listings:
        
        #converts the database listing into a vector
        listing_vector = create_feature_vector(listing)
        
        #uses the function to get the score
        score = calculate_cosine_similarity(user_preference_vector, listing_vector)
        
        #adds the (database_object, score) to our list
        if score > 0: #This is optional to filter out non-matches. (We can change this)
            scored_listings.append((listing, score))

    #sorts the list by score (highest first)
    scored_listings.sort(key=lambda x: x[1], reverse=True)
    
    #returns the top N results
    return scored_listings[:top_n]