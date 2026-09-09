import os, requests
token = os.getenv("TELEGRAM_TOKEN")
chat = os.getenv("CHAT_ID")
requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={"chat_id": chat, "text": "✅ Yeni bot bağlandı! Çalışıyor."}, timeout=15)
