import csv
import numpy as np
from .createListingVector import createListingVector

DATA_CSV = "data/vehicles.csv"

# in-memory cache
cacheReady = False
cachedListings = []   # all non-empty listings
totalListings = 0

# cosine data
listingIds = None 
cosineMatrix = None


def isEmptyListing(listing):
    manufacturerName = (listing.get("manufacturer") or "").strip()
    year = int(listing.get("year") or 0)
    return (manufacturerName == "" or year <= 0)


def rowToListing(row):
    manufacturerName = (row.get("manufacturer") or row.get("make") or "").strip().lower()
    priceStr = (row.get("price") or "").replace(",", "").strip()
    yearStr = (row.get("year") or "").strip()

    price = float(priceStr) if priceStr else 0.0
    year = int(yearStr) if yearStr.isdigit() else 0

    return {
        "id": row.get("id") or row.get("vin") or row.get("url"),
        "manufacturer": manufacturerName,
        "price": price,
        "year": year,
    }


def normalizeVectors(matrix):
    rowLengths = np.linalg.norm(matrix, axis=1, keepdims=True)
    rowLengths[rowLengths == 0] = 1.0
    return matrix / rowLengths


def prepCache():
    global cacheReady, cachedListings, totalListings, listingIds, cosineMatrix
    if cacheReady:
        return

    listings = []
    with open(DATA_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            listings.append(rowToListing(row))

    # filter out incomplete listings
    cachedListings = [l for l in listings if not isEmptyListing(l)]
    totalListings = len(cachedListings)

    # create cosine similarity vectors && normalize them
    vectors = [createListingVector(l) for l in cachedListings]
    X = np.asarray(vectors, dtype=np.float32) # matrix of all car vectors

    cosineMatrix = normalizeVectors(X) #normalized vectors matrix for cosine sim
    listingIds = np.asarray([l["id"] for l in cachedListings])

    cacheReady = True

def getIds():
    return listingIds


def getCosineMatrix():
    return cosineMatrix


def loadListings():
    return cachedListings


def getTotal():
    return totalListings
