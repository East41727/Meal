import logging
from aiogram import Bot, Dispatcher, executor, types
from buttton import main_markup,menu,menu_s,menu_q,menu_ichimlik
meal = "6296479600:AAEbMiLIxo4cOkyPD46tofezvsIGuWGX0EY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=meal)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def d_start(message: types.Message):
   user=message.from_user.full_name
   await message.answer(f"Asosiy menyuga xush kelibsiz, {user}", reply_markup=main_markup)
   

@dp.callback_query_handler(text="prices")
async def cas(call: types.CallbackQuery):
   await call.message.answer(f"📕 Menyuga xush kelibsiz", reply_markup=menu)
   await call.message.delete()


@dp.callback_query_handler(text="suyuq")
async def fluid(call:types.CallbackQuery):
   await call.message.answer(f"Suyuq ovqatlar qismiga xush kelibsiz.",reply_markup=menu_s)


@dp.callback_query_handler(text="Baliq sho'rva")
async def fish(call:types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=a2549a222704ea5921a3d647a72759f7c05c8f46-9147529-images-thumbs&n=13", caption="Baliq sho'rva\n\n\n\nNarxi:21999")


@dp.callback_query_handler(text="Mastava")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=e33edfce70987cefc9f952fc1ad7a079cb301f6c-4156995-images-thumbs&n=13", caption="Mastava\n\n\n\nNarxi:15999")


@dp.callback_query_handler(text="Moshxo'rda")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=a093e6f49959ec5a3949c31c53667e71c76645eb-8710005-images-thumbs&n=13", caption="Mashxo'rda\n\n\n\nNarxi:12999")


@dp.callback_query_handler(text="Tovuq sho'rva")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=aacd9a437d85215dce6a36381c1fdb275953ba5a-8770658-images-thumbs&n=13", caption="Tovuq sho'rva\n\n\n\nNarxi:17999")


@dp.callback_query_handler(text="Lag'mon")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=02417e063db7cfe894952432ee658c46378f1412-9230514-images-thumbs&n=13", caption="Lag'mon\n\n\n\nNarxi:13999")


@dp.callback_query_handler(text="quyuq")
async def sluid(call: types.CallbackQuery):
   await call.message.answer(f"Quyuq  ovqatlar qismiga xush kelibsiz.", reply_markup=menu_q)

@dp.callback_query_handler(text="Manti")
async def manti(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=d83f22d64025bd1ba4fb0a9f7c07eb7d6b758e4c-9029424-images-thumbs&n=13", caption="Manti\n\n\n\nNarxi:10999")

@dp.callback_query_handler(text="Perashki")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=4f3c0bc74c09583b3ffb3f7646e6d6406b5aea47-8497871-images-thumbs&n=13", caption="Perashki\n\n\n\nNarxi:3999")
@dp.callback_query_handler(text="Cho'zma lagmon")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=f2a9e5c95d6a2f6bc0902c3bfdc4eec90006a929-8427500-images-thumbs&n=13", caption="Cho'zma lag'mon\n\n\n\nNarxi:12999")
@dp.callback_query_handler(text="Besh barmoq")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=a109071c5213c6440685c8890a2061e4ddee2355-4493789-images-thumbs&n=13", caption="Besh barmoq\n\n\n\nNarxi:19999")


@dp.callback_query_handler(text="Somsa")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1c2474a568ad91b5c027ef55e4db799d91587488-7265716-images-thumbs&n=13", caption="Somsa\n\n\n\nNarxi:7999")


@dp.callback_query_handler(text="Grechka")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=ef56e6380af6bf85d54f816babbb83d1f6cfbb14-8984683-images-thumbs&n=13", caption="Grechka\n\n\n\nNarxi:18999")


@dp.callback_query_handler(text="Palov")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://yandex.ru/images/search?pos=8&from=tabbar&img_url=https%3A%2F%2Fwebpulse.imgsmail.ru%2Fimgpreview%3Fmb%3Dwebpulse%26key%3Dpulse_cabinet-image-014ac91b-f251-4d1b-8a3b-f531c985e468&text=palov&rpt=simage&lr=193247", caption="Palov\n\n\n\nNarxi:29999")


@dp.callback_query_handler(text="Spagetti")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=3ccc933dd28e390f2df33e9db081d32f623acdb1-9051746-images-thumbs&n=13", caption="Spagetti\n\n\n\nNarxi:18999")


@dp.callback_query_handler(text="ichimlik")
async def sichim(call: types.CallbackQuery):
   await call.message.answer(f"Ichimliklar  qismiga xush kelibsiz.", reply_markup=menu_ichimlik)


@dp.callback_query_handler(text="Coco Cola")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=2ec931bef949dd17c7ab5283cf7495ea92ab60c4-4343452-images-thumbs&n=13", caption="Coca cola\n\n\n\nNarxi:10999")


@dp.callback_query_handler(text="Fanta")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=10f242097917c124b58fdf85830282f0f71a5965-9203641-images-thumbs&n=13", caption="Fanta\n\n\n\nNarxi:11999")


@dp.callback_query_handler(text="Sprite")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=df16f04a8b8794725677a9e2dfae1e23ddcb8065-8172990-images-thumbs&n=13", caption="Sprite\n\n\n\nNarxi:9999")


@dp.callback_query_handler(text="Pepsi")
async def mas(call: types.CallbackQuery):
   await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=3318d1c18507f195ae01ebac1e090c488a8e464e-8959338-images-thumbs&n=13", caption="Pepsi\n\n\n\nNarxi:10999")


@dp.callback_query_handler(text="locataion")
async def location(call: types.CallbackQuery):
   await call.message.answer("Bizning manzil: 🔽 ")
   await call.message.answer_location(latitude=41.695481, longitude=60.758504)


@dp.callback_query_handler(text="order")
async def order(call: types.CallbackQuery):

   await call.message.answer(f"Siz hali bizdan buyurtma bermadingiz, keling, bu tushunmovchilikni to'g'irlaylik")
   await call.message.answer("🤔")


@dp.callback_query_handler(text="back")
async def nback(call: types.CallbackQuery):

   await call.message.answer("Siz asosiy menyudasiz",reply_markup=main_markup)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
