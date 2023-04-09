const TelegramBot = require("node-telegram-bot-api");
const kb = require("./keyboard");
const rate = require("./messageAnalys");

const token = "6195636497:AAEfAnC9YThZvuanb11r4zexbLB_jQLvk94";
const bot = new TelegramBot(token, { polling: true });

// Обработка команды Старт
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;

  bot.sendMessage(
    chatId,
    `Привет! Я могу проконсультировать тебя по любому вопросу. Просто спроси!`,
    {
      reply_markup: JSON.stringify({
        keyboard: kb.mainKb
      }),
    }
  );
});

// Обработка кнопок
bot.onText(/FAQ/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId,'Просто напишите мне "Вопрос: ваш вопрос" и я постараюсь найти на него ответ или задайте его напрямую приемной комиссии по форме',     
  {
    reply_markup: JSON.stringify({
      inline_keyboard: kb.formKb
    })
  });
});

bot.onText(/Полезная информация/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'Выберете интересующую вас тему',     
  {
    reply_markup: JSON.stringify({
      inline_keyboard: kb.helpKb
    })
  });
});

bot.onText(/Тест на профориентацию/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'Тест на профориентацию в разработке');
});

bot.onText(/Вопрос: (.+)/, (msg, match) =>{
  const chatId = msg.chat.id;
  const textMsg = match[1];

  result = rate.rateAnswer(textMsg);
 
  bot.sendMessage(chatId, result,     
    {
    reply_markup: JSON.stringify({
      inline_keyboard: kb.formKb
    })
  })
});

// Обработка Callback'ов от inline-кнопок
bot.on("callback_query", msg => {
  const chatId = msg.message.chat.id;
  if (msg.data == 'Declaration'){
    bot.sendMessage(chatId, 'Выберите уровень образования:',     
    {
      reply_markup: JSON.stringify({
        inline_keyboard: kb.declarationKb
      })
    });
  } else if (msg.data == 'Consert'){
    bot.sendMessage(chatId, 'Выберите уровень образования:',     
    {
      reply_markup: JSON.stringify({
        inline_keyboard: kb.consertKb
      })
    });
  };
});

bot.on('polling_error', (err) => console.log(err));