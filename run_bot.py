#!/usr/bin/env python3
"""
รันสคริปต์นี้เพื่อทดสอบบอท
ต้องตั้งค่า BOT_TOKEN ก่อน:
  export BOT_TOKEN="your_bot_token_here"
หรือสร้างไฟล์ .env ที่มี:
  BOT_TOKEN=your_bot_token_here
"""
import sys
import os

# ตรวจสอบว่ามี BOT_TOKEN หรือไม่
token = os.getenv("BOT_TOKEN", "").strip()

if not token:
    print("❌ ไม่พบ BOT_TOKEN")
    print("\nวิธีตั้งค่า:")
    print("1. ใช้ environment variable:")
    print("   export BOT_TOKEN=\"your_bot_token_here\"")
    print("\n2. หรือสร้างไฟล์ .env:")
    print("   echo 'BOT_TOKEN=your_bot_token_here' > .env")
    print("\nจากนั้นรันอีกครั้ง:")
    print("   python quickstart_bot.py")
    sys.exit(1)

print("✅ พบ BOT_TOKEN")
print("🤖 กำลังรันบอท...")
print("\nกด Ctrl+C เพื่อหยุดบอท")

# ถ้ามี token ให้รันบอท
import quickstart_bot
