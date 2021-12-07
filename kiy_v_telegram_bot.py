import json

from aiogram import Bot, Dispatcher, executor, types
from configure import config

bot = Bot(config['token'])
dp = Dispatcher(bot)

PC_PRODUCTS_JSON = 'kiy_v_json/pc_products.json'

# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.reply('hi')

@dp.message_handler(commands='all_products')
async def get_all_products(message: types.Message):
    with open(PC_PRODUCTS_JSON) as file:
        products = json.load(file)

        for value in products:
            information = f"{value['Name product']}\n" \
                        f"{value['URL product']}\n" \
                        f"{value['Price product']}"        

            await message.answer(information)

executor.start_polling(dp)