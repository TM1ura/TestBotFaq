import logging
import asyncio
import sqlite3
import codecs
from os import path
from aiogram import Bot, Dispatcher
from tgBot.config import TOKEN
from tgBot.filtres.buttons import FaqFilter, HelpFilter, TestFilter, CalculatorFilter
from tgBot.filtres.callbacks import YesCallbackFilter, NoCallbackFilter, DeclarationFilter, ConsertFilter, ExamFilter, BackToHelpFilter
from tgBot.handlers.buttons import register_buttons
from tgBot.handlers.questions import register_question
from tgBot.handlers.commands import register_commands
from tgBot.handlers.callbacks import register_callbacks

bot = Bot(token=TOKEN,
          parse_mode='HTML')

dp = Dispatcher(bot)
logger = logging.getLogger(__name__)

# Регистрация фильтров
async def register_all_filtres():
    # фильтры текста
    dp.filters_factory.bind(callback=FaqFilter,
                            event_handlers=[dp.message_handlers])
    dp.filters_factory.bind(callback=HelpFilter,
                            event_handlers=[dp.message_handlers])
    dp.filters_factory.bind(callback=TestFilter,
                            event_handlers=[dp.message_handlers])
    dp.filters_factory.bind(callback=CalculatorFilter,
                            event_handlers=[dp.message_handlers])

    # фильтры callback'ов
    dp.filters_factory.bind(callback=YesCallbackFilter,
                            event_handlers=[dp.callback_query_handlers])
    dp.filters_factory.bind(callback=NoCallbackFilter,
                            event_handlers=[dp.callback_query_handlers])
    dp.filters_factory.bind(callback=DeclarationFilter,
                            event_handlers=[dp.callback_query_handlers])
    dp.filters_factory.bind(callback=ConsertFilter,
                            event_handlers=[dp.callback_query_handlers])
    dp.filters_factory.bind(callback=BackToHelpFilter,
                            event_handlers=[dp.callback_query_handlers])
    dp.filters_factory.bind(callback=ExamFilter,
                            event_handlers=[dp.callback_query_handlers])

# Регистрация хендлеров
async def register_all_handlers():
    register_buttons(dispatcher=dp)
    register_commands(dispatcher=dp)
    register_question(dispatcher=dp)
    register_callbacks(dispatcher=dp)

# Проверка существует ли БД
async def check_db():
    if path.isfile('exams.db'):
        logger.info('exams.db already initiated')
    else:
        logger.info('Initialization exams.db')
        db = sqlite3.connect('exams.db')
        init = codecs.open('tgBot/services/db_init.sql', encoding='utf-8', mode='r')
        insert = codecs.open('tgBot/services/db_input.sql', encoding='utf-8', mode='r')

        query = "".join(init.readlines())
        db.executescript(query)
        init.close()

        query = "".join(insert.readlines())
        db.executescript(query)
        insert.close()

        db.close()
        logger.info('exams.db initiated')
async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')

    logger.info(f"Starting bot: {(await bot.get_me()).full_name}[{(await bot.get_me()).username}]")

    await check_db()
    await register_all_filtres()
    await register_all_handlers()

    try:
        await dp.start_polling()

    except ConnectionError as conError:
        logger.error('Connection error:', conError)

    except Exception as error:
        logger.error(error)
    finally:
        # Закрытие сессии
        await (await bot.get_session()).close()
        logger.info("Stop bot")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
