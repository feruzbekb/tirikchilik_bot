from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Asosiy menyu tugmalari (4 ta tugma)
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🔥 Mahsulotlar",
                web_app=WebAppInfo(url="https://tirikchilik.uz")
            ),
            KeyboardButton(text="🛒 Savat")
        ],
        [
            KeyboardButton(text="🤝 Hamkorlik"),
            KeyboardButton(text="ℹ️ Ma'lumot")
        ]
    ],
    resize_keyboard=True
)

# Ma'lumot bo'limi ichki menyusi
info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Izoh qoldirish")
        ],
        [
            KeyboardButton(text="🚀 Yetkazib berish shartlari"),
            KeyboardButton(text="☎️ Kontaktlar")
        ],
        [
            KeyboardButton(text="🏠 Bosh menyu")
        ]
    ],
    resize_keyboard=True
)