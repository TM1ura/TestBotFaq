const TelegramBot = require("node-telegram-bot-api");
const Morphy = require("phpmorphy");
const similarity = require("string-similarity")
const data = require("./data");

const token = "5815919263:AAETy0dty_fBQOloBHKVSfs_BOuikFOkHGo";
const priemUrl = "https://www.masu.edu.ru/abit/reception/";
const abitUrl = "https://www.masu.edu.ru/abit/";
const timeUrl = "https://www.masu.edu.ru/abit/rules/application/"
const bot = new TelegramBot(token, { polling: true });
const morph = new Morphy('ru', {
  // nojo: false,
  storage: Morphy.STORAGE_MEM,
  predict_by_suffix: true,
  predict_by_db: true,
  graminfo_as_text: true,
  use_ancodes_cache: false,
  resolve_ancodes: Morphy.RESOLVE_ANCODES_AS_TEXT,
});
const FAQ = data.FAQ;

// Обработка команды Старт
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;

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

// Обработка кнопок
bot.onText(/FAQ/, (msg) =>{
  const chatId = msg.chat.id;

  bot.sendMessage(chatId,'Просто напишите мне "Вопрос: ваш вопрос" и я постараюсь найти на него ответ или задайте его напрямую приемной комиссии по форме',     
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

// Обработка Callback'ов от inline-кнопок
bot.on('callback_query', (msg, callback_query) => {
  const chatId = msg.chat.id;


})

bot.onText(/Вопрос: (.+)/, (msg, match) =>{
  const chatId = msg.chat.id;
  const textMsg = match[1];

  var questions = new Array();
  for (let i = 0; i < FAQ.length; i += 1){ 
    questions.push(FAQ[i].question);
  };

  result = similarity.findBestMatch(textMsg, questions);

  console.log(result['bestMatch']['rating']);

  if(result['bestMatch']['rating'] >= 0.5){  
  bot.sendMessage(chatId, FAQ[result['bestMatchIndex']].answer + '\n\nЕсли я не ответил на ваш вопрос, то вы можете задать вопрос напрямую приемной комиссии по форме:',     
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
  } else if(result['bestMatch']['rating'] >= 0.2){
    bot.sendMessage(chatId, 'Возможно вас устроит этот ответ, в ином случае попробуйте уточнить ваш вопрос или задайте его напрямую приемной комиссии\n\n' + FAQ[result['bestMatchIndex']].answer,     
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
  }else{
    bot.sendMessage(chatId, 'Я не нашел ответ на ваш вопрос, но вы можете задать вопрос напрямую приемной комиссии по форме:',     
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
  };
});