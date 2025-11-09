import numpy as np
from .features import FEATURE_ORDER
from .cache import getCosineMatrix
from .createUserVector import createUserVector

# use jaccard similarity to compare vectors and assign scores
def jaccardCalculation(userVec, listingVec):
    intersection = np.sum(np.logical_and(userVec, listingVec))
    union = np.sum(np.logical_or(userVec, listingVec))
    
    if union == 0:
        return 0.0
    
    return intersection / union

# computes scores for all car listings
def jaccardSimilarity(userVec):
    X = getCosineMatrix()

    binaryUserVec = (userVec > 0)

    # iterate and calculate jaccard similarity scores
    numItems = X.shape[0]
    scores = np.zeros(numItems, dtype=np.float32)

    for i in range(numItems):
        binaryListingVec = (X[i] > 0) 
        scores[i] = jaccardCalculation(binaryUserVec, binaryListingVec)
    
    return scores