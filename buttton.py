from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,WebAppInfo,ReplyKeyboardMarkup,KeyboardButton


main_markup=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📕 Menu", callback_data="prices")],

    [InlineKeyboardButton(text=" 🆕 So'ngi yangiliklar",  web_app=WebAppInfo(url="https://www.restaurant.com/?sitetype=mainsite"))],
    [InlineKeyboardButton(text=" 🛒 Buyurtma berish",callback_data="order")],
    [InlineKeyboardButton(text=" 📍 Bizning manzil",  callback_data="locataion")]
   ])


fluid_meal=InlineKeyboardButton(text="Suyuq ovqatlar qismi",callback_data="suyuq")
solid_meal=InlineKeyboardButton(text="Quyuq ovqatlar qismi",callback_data="quyuq")
drinks=InlineKeyboardButton(text="Ichimliklar qismi",callback_data="ichimlik")
back=InlineKeyboardButton(text="orqaga",callback_data="back")
menu=InlineKeyboardMarkup(row_width=3)
menu.row(fluid_meal,solid_meal,drinks)
menu.row(back)



# contact=KeyboardButton(text="Raqamni ulashish")
# location=KeyboardButton(text="Joylashuvni ulashish")
# data=ReplyKeyboardMarkup(resize_keyboard=True)
# data.row(contact,location)




suyuq_meal=["Moshxo'rda","Baliq sho'rva","Mastava","Lag'mon","Tovuq sho'rva"]
menu_s=InlineKeyboardMarkup(row_width=2)
for meal in suyuq_meal:
    menu_s.insert(InlineKeyboardButton(text=meal,callback_data=meal))



quyuq_meal=["Manti","Somsa","Perashki","Grechka","Besh barmoq","Palov","Cho'zma lag'mon","Spagetti"]
menu_q=InlineKeyboardMarkup(row_width=2)
for quy in quyuq_meal:
    menu_q.insert(InlineKeyboardButton(text=quy,callback_data=quy))


ichimliks=["Coca Cola","Sprite","Fanta","Pepsi"]
menu_ichimlik=InlineKeyboardMarkup(row_width=2)
for ichim in ichimliks:


   menu_ichimlik.insert(InlineKeyboardButton(text=ichim,callback_data=ichim))