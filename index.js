const TelegramBot = require("node-telegram-bot-api");
const similarity = require("string-similarity")
const data = require("./data");

const token = "5815919263:AAETy0dty_fBQOloBHKVSfs_BOuikFOkHGo";
const priemUrl = "https://www.masu.edu.ru/abit/reception/";
const timeUrl = "https://www.masu.edu.ru/abit/rules/application/"
const otherDocUrl = "https://www.masu.edu.ru/abit/admission/apply/"
const bot = new TelegramBot(token, { polling: true });
const FAQ = data.FAQ;

// Обработка команды Старт
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;

  bot.sendMessage(
    chatId,
    `Привет! Я могу проконсультировать тебя по любому вопросу
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
    parse_mode: 'markdown',
    reply_markup: JSON.stringify({
      inline_keyboard: [
        [
          {
            text: "Сроки и правила подачи заявлений",
            web_app: {
              url: timeUrl,
            }
          }
        ],
        [
          {
            text: "Заявление на поступление",
            callback_data: "Declaration"
          }
        ],
        [
          {
            text: "Согласие на зачисление",
            callback_data: "Consert"
          }
        ],
        [
          {
            text: "Другие документы",
            web_app: {
              url: otherDocUrl,
            },
          },
        ],
      ]
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

// Обработка Callback'ов от inline-кнопок
bot.on("callback_query", msg => {
  const chatId = msg.message.chat.id;
  if (msg.data == 'Declaration'){
    bot.sendMessage(chatId, 'Выберите уровень образования:',     
    {
      reply_markup: JSON.stringify({
        inline_keyboard: [
          [
            {
              text: "Бакалавриат и специалитет",
              url: "https://www.masu.edu.ru/upload/iblock/baf/5e4gwvoan7c3e46fb8lomy6s97myrwot/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%B1%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82%20%D0%B8%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%82%D0%B5%D1%82.doc"
            },
          ],
          [
            {
              text: "Магистратура",
              url: "https://www.masu.edu.ru/upload/iblock/18c/gpzyizrek88rllpv2q4u9lwn1n6k4xqu/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B2%20%D0%BC%D0%B0%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D1%83%D1%80%D1%83%20%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9.doc"
            }
          ],
          [
            {
              text: "Аспирантура",
              url: "https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc"
            }
          ],
          [
            {
              text: "Среднее Профессиональное Образование",
              url: "https://www.masu.edu.ru/upload/iblock/4ca/yh97z6hlfbyqf809gy50uiic4kwjb58l/zayavlenie-o-prieme-spo.pdf"
            }
          ]
        ],
      })
    });
  } else if (msg.data == 'Consert'){
    bot.sendMessage(chatId, 'Выберите уровень образования:',     
    {
      reply_markup: JSON.stringify({
        inline_keyboard: [
          [
            {
              text: "Бакалавриат, специалитет, магистратура",
              url: "https://www.masu.edu.ru/upload/iblock/5d1/pto9140kxmogqh5ibmqyoivvynlas2tf/%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(1).doc"
            },
          ],
          [
            {
              text: "Аспирантура",
              url: "https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc"
            }
          ]
        ],
      })
    });
  };
});

bot.on('polling_error', (err) => console.log(err));