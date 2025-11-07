from telethon import TelegramClient, events
import re
import os
import logging
logging.basicConfig(level=logging.INFO)


api_id = 27229540
api_hash = '3f01b9db72409849e0b3c1ae316298e2'
bot_username = '@cardXabarBot'
target_chat = '-4905804995'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(from_users=bot_username))
async def handler(event):
    text = event.message.message or ""

    # 1️⃣ Faqat “Kartaga o'tkazma” so‘zi bilan boshlansa
    if text.strip().startswith("🟢 Kartaga o'tkazma") or text.strip().startswith("Kartaga o'tkazma"):
        # 2️⃣ Ixtiyoriy: xabarni tekshirish uchun regex bilan summani topamiz
        match = re.search(r"([\+\-]?\s?\d[\d\s]*\.\d{2})\s*UZS", text)
        if match:
            amount = match.group(1).strip()
            print(f"✅ Yangi to‘lov: {amount}")
        else:
            print("✅ Yangi karta o'tkazmasi aniqlandi (summa topilmadi).")

        await client.forward_messages(target_chat, event.message)

    else:
        print("❌ Bu oddiy xabar, o'tkazildi.")

print("🔎 'Kartaga o'tkazma' xabarlarini kuzatish boshlandi...")
client.start()
print("Listening for messages...")
client.run_until_disconnected()
