from aiogram.types import Message, FSInputFile
from time import sleep

async def sendPhotoHint(message: Message):
    photo_path_textDoc = 'photoes\\textHint.jpg'
    photo_textDoc = FSInputFile(photo_path_textDoc)
    sleep(1)
    await message.answer_photo(photo_textDoc, caption='Пример как должен выглядеть текстовый документ')

    photo_path_aloneCode = 'photoes\\AloneCode.jpg'
    photo_alone = FSInputFile(photo_path_aloneCode)
    sleep(1)
    await message.answer_photo(photo_alone, caption='Пример как посылать один арктикул')