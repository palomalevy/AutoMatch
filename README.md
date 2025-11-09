# Setup && Testing

Follow to set up the backend locally.
Files to edit are in backend/api/helper functions

---

## STEP 1: Clone the Repository
```bash
git clone https://github.com/palomalevy/automatch.git
cd automatch/backend
```

## STEP 2: Create a Virtual Environment
```bash
python -m venv .venv

macOS: source .venv/bin/activate
Windows: .venv\Scripts\Activate.ps1
```

## STEP 3: Install dependencies
```bash
pip install -r requirements.txt
```

## STEP 4: Run backend
```bash
python manage.py runserver
```

## TESTING: JACCARD
```bash
curl -X POST \                                          
  -H "Content-Type: application/json" \
  -d @test_user.json \
  http://127.0.0.1:8000/api/feed/jaccard/
```
- Since there are so many data points (~400,000), you can try changing the line 83 in listings.py to change results from descending to ascending and see the top scores in the terminal.
- Here is the new line that should go there:
```bash
sortedScores = sorted(scores.items(), key=lambda kv: kv[1], reverse=False)
```
  

## TESTING: COSINE
```bash
curl -X POST \                                          
  -H "Content-Type: application/json" \
  -d @test_user.json \
  http://127.0.0.1:8000/api/feed/cosine/
```
- Same goes for the cosine test. By changing line 72 in listings.py to change results from descending to ascending and see the top scores in the terminal.
- Here is the new line that should go there:
```bash
sortedScores = sorted(scores.items(), key=lambda kv: kv[1], reverse=False)
```
