import csv, json
from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_JSON = BASE_DIR / "data" / "users.json"

def loadUsers():
    with open(DATA_JSON, "r") as f:
        return json.load(f)

def userList(request):
    users = loadUsers()
    return JsonResponse(users, safe=False)

def userDetail(request, user_id):
    userID = int(user_id)
    users = loadUsers()
    user = next((u for u in users if u["id"] == userID), None)

    if request.method == "GET":
        return JsonResponse(user)

    elif request.method == "PUT":
        body = json.loads(request.body or b"{}")
    
        return JsonResponse({
            "persisted": False,
            "user_id": userID,
            "received": body,
            "stored_user": user
        })

def usersJSON(request, user_id):
    users = loadUsers()
    user = next((u for u in users if u['id'] == user_id), None)
    return JsonResponse(user)
