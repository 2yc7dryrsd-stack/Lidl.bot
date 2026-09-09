import os, requests
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print(f"CHAT_ID: {CHAT_ID}")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": "✅ TEST OK - Lante bot calisiyor!"}
r = requests.post(url, json=data, timeout=20)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")
