import numpy as np
from .features import FEATURE_ORDER
from .cache import getCosineMatrix
from .createUserVector import createUserVector

# use cosine similarity to compare vectors and assign scores
# normalizes user vector
def normalizeUsereVector(userVec):
    norm = np.linalg.norm(userVec)
    return userVec / norm if norm > 0 else userVec

# adds weights to certain feature groups
def featureWeights(userVec):
    weightedVec = userVec.copy()
    
    yearWeight = 1.5
    brandWeight = 2

    weightedVec[3:6] *= yearWeight
    weightedVec[6:] *= brandWeight

    return weightedVec

    
# computes scores for all car listings
def cosineSimilarity(userVec):
    X = getCosineMatrix()
    userVec = applyGroupWeights(userVec)
    normUserVec = normalizeVector(userVec)
    scores = np.dot(X, normUserVec)

    return scores


