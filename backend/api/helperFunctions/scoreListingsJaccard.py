import numpy as np
from .cache import prepCache, getIds
from .createUserVector import createUserVector
from .jaccardSimilarity import jaccardSimilarity

def scoreListingsJaccard(user):
    prepCache()
    
    userVec = np.asarray(createUserVector(user), dtype=np.float32)

    scores = jaccardSimilarity(userVec)

    carIDs = getIds()
    scoredListings = {str(carIDs[i]): float(scores[i]) for i in range(len(carIDs))}
    
    return scoredListings