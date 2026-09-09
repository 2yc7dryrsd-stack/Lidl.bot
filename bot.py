import os, requests, json
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}, timeout=15)

if not TOKEN or not CHAT_ID:
    print("Token yok")
    exit()

# Test mesajı
send("✅ <b>Lidl Bot yeniden kuruldu!</b>\nTest başarılı. Her sabah 08:00'de kontrol edecek.")

print("Bot çalıştı ve mesaj gönderdi")
