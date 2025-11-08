import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = ""  # Твой токен Бота


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Покажи котика"), KeyboardButton(text="Случайное число")],
        [KeyboardButton(text="Мое настроение"), KeyboardButton(text="Шар судьбы")],
    ],
    resize_keyboard=True,
)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "Привет! Я твой развлекательный бот! \n"
        "Выбери что-нибудь из меню ниже или напиши команду:\n"
        "/help - Показать помощь\n"
        "/fun - Случайная развлекательная команда"
    )
    await message.answer(welcome_text, reply_markup=main_menu)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать общение\n"
        "/help - Показать это сообщение\n"
        "/fun - Случайная развлекательная команда\n\n"
        "Или используй кнопки меню:\n"
        "Покажи котика - Милые котики!\n"
        "Случайное число - От 1 до 100\n"
        "Мое настроение - Угадаю твое настроение\n"
        "Шар судьбы - Ответ на любой вопрос"
    )
    await message.answer(help_text)


@dp.message(Command("fun"))
async def cmd_fun(message: types.Message):
    fun_actions = [
        "🎲 Бросил кубик: выпало " + str(random.randint(1, 6)),
        "🐱 Лови котика! https://cataas.com/cat",
        "Шар судьбы говорит: "
        + random.choice(["Да", "Нет", "Возможно", "Спроси позже"]),
        "Твое настроение: "
        + random.choice(["Отлично!", "Нормально", "Могло быть лучше..."]),
        "Сегодня будет хороший день!",
    ]
    await message.answer(random.choice(fun_actions))


@dp.message(lambda message: message.text == "🐱 Покажи котика")
async def show_cat(message: types.Message):
    cat_url = f"https://cataas.com/cat?t={random.random()}"
    await message.answer_photo(photo=cat_url, caption="Держи котика! 😺")


@dp.message(lambda message: message.text == "🎲 Случайное число")
async def random_number(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f"🎲 Твое число: {number}!")


@dp.message(lambda message: message.text == "Мое настроение")
async def guess_mood(message: types.Message):
    moods = [
        "Чувствую что у тебя хорошее настроение"
        "Чувствую что у тебя неплохое настроение"
        "Чувствую что у тебя не очень настроение..."
    ]
    await message.answer(random.choice(moods))


@dp.message(lambda message: message.text == "Шар судьбы")
async def magic_ball(message: types.Message):
    answers = ["Да!", "Спроси позже...", "Не очень..."]
    await message.answer(" " + random.choice(answers))


@dp.message()
async def echo(message: types.Message):
    if message.text not in [
        "🐱 Покажи котика",
        "🎲 Случайное число",
        "Мое настроение",
        "Шар судьбы",
        "iПомощь",
    ]:
        await message.answer("Используй меню или команды!", reply_markup=main_menu)


async def main():
    print("Развлекательный бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
