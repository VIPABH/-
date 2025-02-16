from telethon import TelegramClient, events

# ضع معلومات تسجيل الدخول الخاصة بك
API_ID = 12046418823456  # استبدل هذا بمعرف API الخاص بك
API_HASH = "91f0d1ea99e43f18d239c6c7af21c40f"  # استبدل هذا بـ API Hash الخاص بك

# إنشاء الجلسة
client = TelegramClient("userbot", API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r"\.مطور"))
async def developer_info(event):
    "رد بسيط عند كتابة .مطور"
    await event.reply("👨‍💻 هذا البوت من تطوير @Username")

@client.on(events.NewMessage(pattern=r"\.بايو"))
async def get_bio(event):
    "إظهار البايو الخاص بك"
    user = await event.client.get_me()
    await event.reply(f"📌 البايو الحالي: {user.bio}")

@client.on(events.NewMessage)
async def logger(event):
    "يسجل كل رسالة تستلمها"
    print(f"📩 رسالة من {event.sender_id}: {event.text}")

# تشغيل البوت
print("🚀 UserBot يعمل الآن!")
client.start()
client.run_until_disconnected()
