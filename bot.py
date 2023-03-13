import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tgBot.config import TOKEN
from tgBot.filtres import FaqFilter, HelpFilter, TestFilter, CalculatorFilter, YesCallbackFilter, NoCallbackFilter, DeclarationFilter, ConsertFilter, ExamFilter, BackToHelpFilter, BackToMainFilter
from tgBot.handlers import register_buttons, register_question, register_commands, register_callbacks, register_exams_scores
from tgBot.services import check_db

bot = Bot(token=TOKEN,
          parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()

dp = Dispatcher(bot,
                storage=storage)
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
    dp.filters_factory.bind(callback=BackToMainFilter,
                            event_handlers=[dp.callback_query_handlers])

# Регистрация хендлеров
async def register_all_handlers():
    register_buttons(dispatcher=dp)
    register_commands(dispatcher=dp)
    register_question(dispatcher=dp)
    register_callbacks(dispatcher=dp)
    register_exams_scores(dispatcher=dp)

async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')

    logger.info(f"Starting bot: {(await bot.get_me()).full_name}[{(await bot.get_me()).username}]")

    await check_db(logger=logger)
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
