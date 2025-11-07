import json

def createUserVector(user):
    return list(user["preferences"].values())