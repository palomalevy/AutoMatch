import csv, json
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_CSV = BASE_DIR / "data" / "vehicles.csv"

PAGE_SIZE_DEFAULT = 12
PAGE_SIZE_MAX = 120

REQUIRED_COLS = ("id", "manufacturer", "price", "year")

# in-memory cache
_cacheReady = False
_cachedListings = []   # all non-empty listings go here
_total = 0

# determines if a listing is empty/incomplete
def isEmptyListing(listing):
    manufacturerName = (listing.get("manufacturer") or "").strip()
    year = int(listing.get("year") or 0)
    return (manufacturerName == "Unknown" or year == 0)

def _rowToListing(row):
    manufacturerName = (row.get("manufacturer") or "").strip()
    priceStr = (row.get("price") or "").replace(",", "").strip()
    yearStr  = (row.get("year") or "").strip()

    price = float(priceStr) if priceStr else 0.0
    year  = int(yearStr) if yearStr.isdigit() else 0

    return {
        "id": row.get("id") or row.get("vin") or row.get("url"),
        "manufacturer": manufacturerName,
        "price": price,
        "year": year,
    }

# prepares the in-memory cache for first and only run
def _prepCache():
    global _cacheReady, _cachedListings, _total
    if _cacheReady:
        return

    listings = []
    with open(DATA_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            listings.append(_rowToListing(row))

    # filter out incomplete listings
    _cachedListings = [l for l in listings if not isEmptyListing(l)]
    _total = len(_cachedListings)
    _cacheReady = True


# loads all listings from CSV
def loadListings():
    _prepCache()
    return _cachedListings

# returns all listings
def listingList(request):
    _prepCache()

    # implements pagination
    page = int(request.GET.get("page", 1))
    pageSize = int(request.GET.get("page_size", PAGE_SIZE_DEFAULT))

    if page < 1: page = 1
    if pageSize < 1: pageSize = PAGE_SIZE_DEFAULT
    if pageSize > PAGE_SIZE_MAX: pageSize = PAGE_SIZE_MAX
    
    start = (page - 1) * pageSize
    end = start + pageSize
    cars = _cachedListings[start:end]

    return JsonResponse({
        "cars": cars,
        "page": page,
        "pageSize": pageSize,
        "total": _total,
        "hasMore": end < _total,
    })

# returns a specific listing by ID
def listingDetail(request, listing_id):
    _prepareCacheOnce()
    listing = next((l for l in _cachedListings if str(l.get("id")) == str(listing_id)), None)
    
    if request.method == "GET":
        return JsonResponse(listing)

    if request.method == "PUT":
        body = json.loads(request.body or b"{}")
    
        return JsonResponse({
            "persisted": False,
            "listing_id": listing_id,
            "received": body,
            "stored_listing": listing
        })