from scipy.spatial import distance

def compare(vector1,vector2):
    cossim = 1 - distance.cosine(vector1, vector2)
    eucdis = distance.euclidean(vector1, vector2)
    return cossim,eucdis