import csv, json
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_CSV = BASE_DIR / "data" / "vehicles.csv"

PAGE_SIZE_DEFAULT = 15
PAGE_SIZE_MAX = 60

REQUIRED_COLS = ("id", "manufacturer", "price", "year")

def loadListings():
    listings = []
    with open(DATA_CSV, "r") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            manufacturerName = (row.get("manufacturer") or "").strip()
            priceStr = (row.get("price") or "").replace(",", "").strip()
            yearStr  = (row.get("year") or "").strip()

            price = float(priceStr) if priceStr else 0.0
            year  = int(yearStr) if yearStr.isdigit() else 0

            listings.append({
                "id": row.get("id") or row.get("vin") or row.get("url"),
                "manufacturer": manufacturerName,
                "price": price,
                "year": year,
            })
        return listings

def isEmptyListing(listing):
    manufacturerName = (listing.get("manufacturer") or "").strip()
    year = int(listing.get("year") or 0)
    return (manufacturerName == "Unknown" or year == 0)


# returns all listings
def listingList(request):
    data = loadListings()

    # filter out incomplete listings
    nonEmpty = [l for l in data if not isEmptyListing(l)]
    empty = [l for l in data if isEmptyListing(l)]
    orderedData = nonEmpty + empty

    # implements pagination
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", PAGE_SIZE_DEFAULT))

    if page < 1:
        page = 1

    if page_size < 1:
        page_size = PAGE_SIZE_DEFAULT

    if page_size > PAGE_SIZE_MAX:
        page_size = PAGE_SIZE_MAX
    
    total = len(orderedData)
    start = (page - 1) * page_size
    end = start + page_size
    cars = orderedData[start:end]

    return JsonResponse({
        "cars": cars,
        "page": page,
        "pageSize": page_size,
        "total": total,
        "totalNonEmpty": len(nonEmpty),
        "totalEmpty": len(empty),
        "hasMore": end < total,
    })

# returns a specific listing by ID
def listingDetail(request, listing_id):
    listings = loadListings()
    listing = next((l for l in listings if str(l.get("id")) == str(listing_id)), None)
    
    if request.method == "GET":
        return JsonResponse(listing)

    if request.method == "PUT":
        body = json.loads(request.body or b"{}")
    
        return JsonResponse({
            "persisted": False,
            "listing_id": listingID,
            "received": body,
            "stored_listing": listing
        })

    return JsonResponse({"error": "Method not allowed"}, status=405)