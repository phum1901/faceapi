from scipy.spatial import distance

def compare_cos(vector1,vector2):
    cossim = 1 - distance.cosine(vector1, vector2)
    return cossim

def compare_dis(vector1,vector2):
    eucdis = distance.euclidean(vector1, vector2)
    return eucdis