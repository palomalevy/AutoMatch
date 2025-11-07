from .features import FEATURE_ORDER

def createListingVector(listing):
    price = float(listing["price"])
    year = int(listing["year"])
    brand = (listing.get("manufacturer") or "").strip().lower().replace(" ", "-")

    # price and year are given value based on the range they fall into
    if price <= 15000:
        price_low, price_mid, price_high = 1, 0, 0
    elif price <= 35000:
        price_low, price_mid, price_high = 0, 1, 0
    else:
        price_low, price_mid, price_high = 0, 0, 1

    if year <= 2010:
        year_old, year_mid, year_new = 1, 0, 0
    elif year <= 2018:
        year_old, year_mid, year_new = 0, 1, 0
    else:
        year_old, year_mid, year_new = 0, 0, 1
    
    extraFeatures = {
        "price_low": price_low,
        "price_mid": price_mid,
        "price_high": price_high,
        "year_old": year_old,
        "year_mid": year_mid,
        "year_new": year_new,
    }

    # create the full feature vector
    vector = []
    for feature in FEATURE_ORDER:
        if feature in extraFeatures:
            vector.append(extraFeatures[feature])
        else:
            vector.append(1 if feature == formattedBrand else 0)

    return vector