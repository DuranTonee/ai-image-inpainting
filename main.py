from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from image_gen import main_function
import os

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message=types.Message):
    await message.answer("Send me an image.")


@dp.message_handler(content_types=["photo"])
async def get_photo(message=types.Message):
    await message.photo[-1].download("original_image.jpg")
    await message.answer("Got it! Hold on just a sec... maybe a little more...")
    main_function(400)
    with open("downloaded_image.png", "rb") as file:
        await bot.send_document(message.chat.id, file)
    os.remove("downloaded_image.png")


@dp.message_handler(content_types=["document"])
async def get_document_photo(message=types.Message):
    extensions = ["jpg", "jpeg", "png", "bmp", "JPG", "JPEG", "PNG", "BMP", "HEIC"]
    document = message.document
    extension = document.file_name.split('.')[-1]
    if extension in extensions:
        await message.document.download("original_image.jpg")
        await message.answer("Got it! Hold on just a sec... maybe a little more...")
        main_function(400)
        with open("downloaded_image.png", "rb") as file:
            await bot.send_document(message.chat.id, file)
        os.remove("downloaded_image.png")
    else:
        await message.answer(f"Please, send an image. You sent .{extension}")

executor.start_polling(dp)