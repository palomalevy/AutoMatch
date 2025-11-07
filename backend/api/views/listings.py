import json
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..helperFunctions.cache import prepCache, loadListings, getTotal

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PAGE_SIZE_DEFAULT = 12
PAGE_SIZE_MAX = 120

# returns all listings
def listingList(request):
    prepCache()

    # implements pagination
    page = int(request.GET.get("page", 1))
    pageSize = int(request.GET.get("page_size", PAGE_SIZE_DEFAULT))
    
    if page < 1:
        page = 1
    if pageSize < 1:
        pageSize = PAGE_SIZE_DEFAULT
    if pageSize > PAGE_SIZE_MAX:
        pageSize = PAGE_SIZE_MAX

    listings = loadListings()
    total = getTotal()

    start = (page - 1) * pageSize
    end = start + pageSize
    cars = listings[start:end]

    return JsonResponse({
        "cars": cars,
        "page": page,
        "pageSize": pageSize,
        "total": total,
        "hasMore": end < total,
    })

# returns a specific listing by ID
def listingDetail(request, listing_id):
    prepCache()

    listings = loadListings()
    listing = next((l for l in listings if str(l.get("id")) == str(listing_id)), None)
    
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