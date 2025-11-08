import numpy as np
from .cache import prepCache, getIds
from .createUserVector import createUserVector
from .cosineSimilarity import cosineSimilarity

def scoreListingsCosine(user):
    prepCache()
    
    userVec = np.asarray(createUserVector(user), dtype=np.float32)

    scores = cosineSimilarity(userVec)

    carIDs = getIds()
    scoredListings = {str(carIDs[i]): float(scores[i]) for i in range(len(carIDs))}
    
    return scoredListings