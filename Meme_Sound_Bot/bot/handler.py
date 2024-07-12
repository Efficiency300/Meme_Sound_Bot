from aiogram import F, Router
from  aiogram.filters import CommandStart , Command
from  aiogram.types import Message ,InlineKeyboardMarkup, InlineKeyboardButton ,, CallbackQuery


router = Router()



@router.message(Command("start"))
async def send_welcome(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Option 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Option 2", callback_data="option_2")],
        [InlineKeyboardButton(text="Option 3", callback_data="option_3")],
    ])
    await message.answer("Choose an option:", reply_markup=keyboard)

# Обработчик нажатий на кнопки
@router.callback_query(lambda c: c.data.startswith("option_"))
async def process_callback(callback_query: CallbackQuery):
    code = callback_query.data
    if code == "option_1":
        await callback_query.message.answer("You chose Option 1")
    elif code == "option_2":
        await callback_query.message.answer("You chose Option 2")
    elif code == "option_3":
        await callback_query.message.answer("You chose Option 3")
    await callback_query.answer()
