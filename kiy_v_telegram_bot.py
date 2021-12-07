import json

from aiogram import Bot, Dispatcher, executor, types
from configure import config

bot = Bot(config['token'])
dp = Dispatcher(bot)

PC_PRODUCTS_JSON = 'kiy_v_json/pc_products.json'

@dp.message_handler(commands='thermal_equipments')
async def get_all_products(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Печі і Пароконвектомати",
        "Плити промислові",
        "Розтоєчні шафи",
        "Промислові сковороди",
        "Котли харчоварильні",
        "Лінії роздачі",
        "Грилі для фаст фуду",
        "Поверхні для смаження"
    ]

    keyboard.add(*buttons)

    await message.answer("Теплове обладнання", reply_markup=keyboard)

@dp.message_handler(content_types=['text'])
async def answers(message: types.Message):
    if message.text == "Печі і Пароконвектомати":
        await message.answer('В розробці')

    elif message.text == "Плити промислові":
        await message.answer('В розробці')

    elif message.text == "Розтоєчні шафи":
        with open(PC_PRODUCTS_JSON) as file:
            products = json.load(file)

            for value in products:
                information = f"{value['Name product']}\n" \
                            f"{value['URL product']}\n" \
                            f"{value['Price product']}"        

                await message.answer(information)

    elif message.text == "Промислові сковороди":
        await message.answer('В розробці')

    elif message.text == "Котли харчоварильні":
        await message.answer('В розробці')

    elif message.text == "Промислові сковороди":
        await message.answer('В розробці')

    elif message.text == "Лінії роздачі":
        await message.answer('В розробці')

    elif message.text == "Грилі для фаст фуду":
        await message.answer('В розробці')

    elif message.text == "Поверхні для смаження":
        await message.answer('В розробці')


executor.start_polling(dp)