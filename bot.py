import os, requests
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print(f"TOKEN var mi: {bool(TOKEN)}")
print(f"CHAT_ID var mi: {bool(CHAT_ID)}")
print(f"CHAT_ID: {CHAT_ID}")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": "✅ Test OK - Bot yeniden kuruldu!", "parse_mode": "HTML"}
r = requests.post(url, json=data, timeout=20)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")

if r.status_code != 200:
    print("HATA: Telegram mesaj gönderemedi! CHAT_ID veya TOKEN yanlis")
else:
    print("BASARILI!")
