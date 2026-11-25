import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import main_menu, info_menu

# BotFather'dan olingan tokenni shu yerga qo'ying
BOT_TOKEN = "8795119314:AAHCRU8xzpS5cifl43wc4Trt2QL4xnydtbg"

# Izoh qoldirish holati (FSM)
class FeedbackState(StatesGroup):
    waiting_for_feedback = State()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# /start buyrug'i
@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user_name = message.from_user.first_name
    text = (
        f"Assalomu Alaykum, {user_name}!\n\n"
        "Ijodimizga qiziqish bildirganingiz uchun tashakkur!\n\n"
        "Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. "
        "Yaqin orada tanlovni kengaytiramiz. Aytganday, istalgan turdagi kiyim buyurtma "
        "berganlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)\n\n"
        "Toshkent bo'yicha yetkazib berish: 1-3 ish kuni\n"
        "O'zbekiston bo'yicha yetkazib berish: 3-7 ish kuni\n"
        "O'zbekiston bo'yicha jo'natmalar seshanba va juma kunlari amalga oshiriladi\n\n"
        "450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!\n\n"
        "Agar bu shartlar sizni qoniqtirsa, \"🔥 Mahsulotlar\" bo'limiga o'tish orqali "
        "buyurtma berishni boshlashingiz mumkin."
    )
    await message.answer(text, reply_markup=main_menu)


# 🛒 Savat tugmasi
@dp.message(F.text == "🛒 Savat")
async def show_cart(message: Message):
    await message.answer("Sizning savatingiz hozircha bo'sh 🛒")


# 🤝 Hamkorlik tugmasi
@dp.message(F.text == "🤝 Hamkorlik")
async def show_partnership(message: Message):
    text = (
        "Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning "
        "buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni "
        "tayyorlashimiz mumkin.\n\n"
        "Biz bilan hamkorlik qilish va takliflar uchun:\n"
        "👤 Menejer: @ziynatovic\n"
        "📞 Telefon: +998 94 896 73 77"
    )
    await message.answer(text)


# ℹ️ Ma'lumot tugmasi (ichki menyuni ochish)
@dp.message(F.text == "ℹ️ Ma'lumot")
async def show_info_menu(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=info_menu)


# 🏠 Bosh menyu tugmasi
@dp.message(F.text == "🏠 Bosh menyu")
async def back_to_main(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bosh menyuga qaytdingiz 👇", reply_markup=main_menu)


# 🚀 Yetkazib berish shartlari tugmasi
@dp.message(F.text == "🚀 Yetkazib berish shartlari")
async def show_delivery_terms(message: Message):
    text = (
        "🚚 <b>Yetkazib berish shartlari:</b>\n\n"
        "📍 <b>Toshkent shahri bo'ylab:</b>\n"
        "• Muddat: 1–3 ish kuni ichida kuryer orqali yetkazib beriladi.\n"
        "• Narxi: 30 000 so'm.\n\n"
        "🇺🇿 <b>O'zbekistonning barcha viloyatlari bo'ylab:</b>\n"
        "• Muddat: 3–7 ish kuni ichida pochta/kuryerlik xizmati orqali yetkaziladi.\n"
        "• Jo'natish kunlari: Har hafta <b>seshanba</b> va <b>juma</b> kunlari.\n"
        "• Narxi: 40 000 so'm.\n\n"
        "🎁 <b>Maxsus taklif:</b> 450 000 so'mdan yuqori bo'lgan barcha buyurtmalar "
        "O'zbekiston bo'ylab <b>MUTLAQO BEPUL</b> yetkazib beriladi!"
    )
    await message.answer(text, parse_mode="HTML")


# ☎️ Kontaktlar tugmasi
@dp.message(F.text == "☎️ Kontaktlar")
async def show_contacts(message: Message):
    text = (
        "📞 <b>Aloqa markazi (Call-markaz):</b>\n\n"
        "☎️ Qisqa raqam: <b>1234</b>\n"
        "📱 Telefon raqamlar:\n"
        "• +998 71 200 00 00\n"
        "• +998 90 123 45 67\n\n"
        "🕘 Ish vaqti: Dushanba – Shanba, 09:00 dan 20:00 gacha."
    )
    await message.answer(text, parse_mode="HTML")


# ✍️ Izoh qoldirish tugmasi
@dp.message(F.text == "✍️ Izoh qoldirish")
async def ask_feedback(message: Message, state: FSMContext):
    await state.set_state(FeedbackState.waiting_for_feedback)
    await message.answer("Izoh:")


# Foydalanuvchi yuborgan izohni qabul qilish
@dp.message(FeedbackState.waiting_for_feedback)
async def receive_feedback(message: Message, state: FSMContext):
    user_feedback = message.text
    await state.clear()
    await message.answer(
        f"✅ Rahmat! Sizning izohingiz qabul qilindi:\n\n<i>«{user_feedback}»</i>",
        parse_mode="HTML",
        reply_markup=info_menu
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())