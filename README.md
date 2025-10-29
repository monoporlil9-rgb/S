# S - Telegram Bot

บอทเทเลแกรมอย่างง่ายที่ใช้ aiogram framework

## การติดตั้ง

1. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

2. ตั้งค่า environment variable:
```bash
export BOT_TOKEN="your_telegram_bot_token_here"
```

หรือสร้างไฟล์ `.env` (คัดลอกจาก `.env.example`)

## การรันบอท

```bash
python quickstart_bot.py
```

## คำสั่งที่รองรับ

- `/start` - เริ่มต้นใช้งานบอท
- `/echo <ข้อความ>` - ทวนข้อความที่ส่งมา
- ส่งข้อความธรรมดา - บอทจะตอบกลับ "รับทราบ: <ข้อความ>"