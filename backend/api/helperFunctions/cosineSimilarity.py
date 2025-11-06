import numpy as np
# use cosine similarity to compare vectors

def calculate_cosine_similarity(vec_a, vec_b):
    #Calculates de cosine similarity between two non-zero vectors

    #first convert both vectors to numpy
    vec_a = np.asarray(vec_a)
    vec_b = np.asarray(vec_b)

    #calculate the dot product
    dot_product = np.dot(vec_a, vec_b)

    #calculate the magnitudes
    mag_a = np.linalg.norm(vec_a)
    mag_b = np.linalg.norm(vec_b)

    #calculate similarity (check to avoid division by zero)
    if mag_a == 0 or mag_b == 0:
        return 0.0
    else:
        return dot_product/(mag_a * mag_b)