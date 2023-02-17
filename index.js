const TelegramBot = require("node-telegram-bot-api");

const token = "5815919263:AAETy0dty_fBQOloBHKVSfs_BOuikFOkHGo";
const priemUrl = "https://www.masu.edu.ru/abit/reception/";
const bot = new TelegramBot(token, { polling: true });

bot.on("message", (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;

  if (text === "/start") {
    bot.sendMessage(
      chatId,
      `Привет! Я могу проконсультировать тебя по любому вопросу
      Например:
      // - 
      // - 
      // - 
      // и т.д.
      Просто спроси! Или задай вопрос по форме ниже`,
      {
        reply_markup: JSON.stringify({
          inline_keyboard: [
            [
              {
                text: "Заполнить форму",
                web_app: {
                  url: priemUrl,
                },
              },
            ],
          ],
        }),
      }
    );
  }
});
