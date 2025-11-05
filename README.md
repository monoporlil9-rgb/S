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

## Agent-o-rama

โปรเจกต์นี้รวม Agent-o-rama library จาก Red Planet Labs ไว้ใน directory `agent-o-rama/`

Agent-o-rama เป็น library สำหรับสร้าง scalable และ stateful LLM agents บน JVM รองรับทั้ง Java และ Clojure APIs

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Agent-o-rama ดูได้ที่:
- [Agent-o-rama README](agent-o-rama/README.md)
- [Agent-o-rama GitHub Repository](https://github.com/redplanetlabs/agent-o-rama)