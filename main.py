from vkbottle.bot import Bot, Message
import os
from dotenv import load_dotenv

load_dotenv()

# сохраняем токен в переменную в виде строки
TOKEN = os.getenv('VK_API')
# создаём бота и передаём токен доступа
bot = Bot(token=TOKEN)


# декоратор указывает, какая функция обрабатывает входящие сообщения
@bot.on.message()
# функция для обработки сообщений пользователя
async def repeat_user_message(message: Message):
    # в параметр message приходит объект класса vkbottle.bot.Message
    # он содержит в себе всю информацию о диалоге, пользователе и сообщении
    await message.answer(message.text)


print('Сервер запущен.')
# запуск бесконечного опроса серверов VK на предмет новых событий
bot.run()