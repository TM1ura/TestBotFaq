const TelegramBot = require("node-telegram-bot-api");

const token = "5815919263:AAETy0dty_fBQOloBHKVSfs_BOuikFOkHGo";
const priemUrl = "https://www.masu.edu.ru/abit/reception/";
const abitUrl = "https://www.masu.edu.ru/abit/";
const timeUrl = "https://www.masu.edu.ru/abit/rules/application/"
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;

  //bot.setChatMenuButton(chatId, {web_app:{url:priemUrl}}) - проверить

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
        keyboard: [
          ['FAQ'],
          ['Полезная информация'],
          ['Тест на профориентацию']
        ],
      }),
    }
  );
});

bot.onText(/FAQ/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'FAQ в разработке',     
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
    })
  });
});

bot.onText(/Полезная информация/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'Выберете интересующую вас тему',     
  {
    reply_markup: JSON.stringify({
      inline_keyboard: [
        [
          {
            text: "Сроки и правила подачи заявлений",
            web_app: {
              url: timeUrl,
            },
          },
        ],
      ],
    })
  });
});

bot.onText(/Тест на профориентацию/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'Тест на профориентацию в разработке');
});
