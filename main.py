# import asyncio
# import os
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto, InputMedia
# from aiogram.filters import Command
#
# API_TOKEN = "6564031591:AAFNzi8P6fUPGBoNGZIkn96I3nMTKV124pc"  # Tokenni o'zgartiring
#
# bot = Bot(API_TOKEN)
# dp = Dispatcher()
#
# # Store user language
# user_lang = {}
#
# # 1. LANGUAGE SELECTION MENU
# lang_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🇺🇿 O'zbek")],
#         [KeyboardButton(text="🇷🇺 Русский")],
#         [KeyboardButton(text="🇬🇧 English")],
#         [KeyboardButton(text="🇹🇷 Türkçe")],
#         [KeyboardButton(text="🇸🇦 العربية")]
#     ],
#     resize_keyboard=True
# )
#
# # Main menus for different languages
# menus = {
#     "uz": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📱 Ijtimoiy Tarmoqlar")],
#             [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="📞 Kontakt")],
#             [KeyboardButton(text="🌍 Tilni o'zgartirish")]
#         ],
#         resize_keyboard=True
#     ),
#     "ru": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📱 Соцсети")],
#             [KeyboardButton(text="ℹ️ О нас"), KeyboardButton(text="📞 Контакты")],
#             [KeyboardButton(text="🌍 Изменить язык")]
#         ],
#         resize_keyboard=True
#     ),
#     "en": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📱 Social Media")],
#             [KeyboardButton(text="ℹ️ About"), KeyboardButton(text="📞 Contact")],
#             [KeyboardButton(text="🌍 Change language")]
#         ],
#         resize_keyboard=True
#     ),
#     "tr": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📱 Sosyal Medya")],
#             [KeyboardButton(text="ℹ️ Hakkımızda"), KeyboardButton(text="📞 İletişim")],
#             [KeyboardButton(text="🌍 Dil değiştir")]
#         ],
#         resize_keyboard=True
#     ),
#     "ar": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📱 وسائل التواصل الاجتماعي")],
#             [KeyboardButton(text="ℹ️ عن الشركة"), KeyboardButton(text="📞 الاتصال")],
#             [KeyboardButton(text="🌍 تغيير اللغة")]
#         ],
#         resize_keyboard=True
#     ),
# }
#
# # 3. SOCIAL MEDIA TUGMALARI
# social_kb = {
#     "uz": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
#             [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
#             [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
#             [KeyboardButton(text="⬅️ Orqaga")]
#         ],
#         resize_keyboard=True
#     ),
#     "ru": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
#             [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
#             [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
#             [KeyboardButton(text="⬅️ Назад")]
#         ],
#         resize_keyboard=True
#     ),
#     "en": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
#             [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
#             [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
#             [KeyboardButton(text="⬅️ Back")]
#         ],
#         resize_keyboard=True
#     ),
#     "tr": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
#             [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
#             [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
#             [KeyboardButton(text="⬅️ Geri")]
#         ],
#         resize_keyboard=True
#     ),
#     "ar": ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
#             [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
#             [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
#             [KeyboardButton(text="⬅️ العودة")]
#         ],
#         resize_keyboard=True
#     )
# }
#
# # ============================
# # 4. SOCIAL MEDIA MAʼLUMOTLARI
# # ============================
# links = {
#     "instagram": "https://www.instagram.com/hl309.hotel?igsh=OGptZjBlNHJkeDg=",
#     "facebook": "https://www.facebook.com/share/1ANcayRW58/",
#     "tiktok": "https://www.tiktok.com/@hlhotel.uz?_r=1&_t=ZM-91gzTyn1lDE",
#     "youtube": "https://www.youtube.com/@HL309",
#     "rutube": "https://rutube.ru/channel/31606755/",
#     "vk": "https://vk.com/hl309"
# }
#
# text_trans = {
#     "uz": {
#         "instagram": "📸 Instagram sahifamiz:\n",
#         "facebook": "📘 Facebook sahifamiz:\n",
#         "tiktok": "🎵 TikTok sahifamiz:\n",
#         "youtube": "▶️ YouTube kanalimiz:\n",
#         "rutube": "🎥 RuTube kanalimiz:\n",
#         "vk": "🟦 VK sahifamiz:\n"
#     },
#     "ru": {
#         "instagram": "📸 Наша страница Instagram:\n",
#         "facebook": "📘 Наша страница Facebook:\n",
#         "tiktok": "🎵 Наш TikTok:\n",
#         "youtube": "▶️ Наш YouTube канал:\n",
#         "rutube": "🎥 Наш RuTube канал:\n",
#         "vk": "🟦 Наша страница VK:\n"
#     },
#     "en": {
#         "instagram": "📸 Our Instagram page:\n",
#         "facebook": "📘 Our Facebook page:\n",
#         "tiktok": "🎵 Our TikTok page:\n",
#         "youtube": "▶️ Our YouTube channel:\n",
#         "rutube": "🎥 Our RuTube channel:\n",
#         "vk": "🟦 Our VK page:\n"
#     },
#     "tr": {
#         "instagram": "📸 Instagram sayfamız:\n",
#         "facebook": "📘 Facebook sayfamız:\n",
#         "tiktok": "🎵 TikTok sayfamız:\n",
#         "youtube": "▶️ YouTube kanalımız:\n",
#         "rutube": "🎥 RuTube kanalımız:\n",
#         "vk": "🟦 VK sayfamız:\n"
#     },
#     "ar": {
#         "instagram": "📸 صفحتنا على إنستغرام:\n",
#         "facebook": "📘 صفحتنا على فيسبوك:\n",
#         "tiktok": "🎵 صفحتنا على تيك توك:\n",
#         "youtube": "▶️ قناتنا على يوتيوب:\n",
#         "rutube": "🎥 قناتنا على روتيوب:\n",
#         "vk": "🟦 صفحتنا على فكونتاكتي:\n"
#     }
# }
#
# # Contact details
# contact_text = {
#     "uz": "📞 *Kontaktlar*\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
#     "ru": "📞 *Контакты*\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
#     "en": "📞 *Contact*\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
#     "tr": "📞 *İletişim*\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
#     "ar": "📞 *الاتصال*\n📱 +998998897776\n📧 sharqhotel2023@gmail.com"
# }
#
# # ABOUT section info
# about_info = {
#     "uz": "ℹ️ *Biz haqimizda*\nZamonaviy, 4 yulduzli mehmonxona - Toshkent shahrida joylashgan. Biz mijozlarimizga qulaylik va yuqori darajadagi xizmatni taqdim etamiz.",
#     "ru": "ℹ️ *О нас*\nСовременный отель в Ташкенте с 4 звездами. Мы предлагаем комфорт и высокий уровень обслуживания для наших клиентов.",
#     "en": "ℹ️ *About us*\nA modern 4-star hotel located in Tashkent. We provide comfort and high-level service to our clients.",
#     "tr": "ℹ️ *Hakkımızda*\nTaşkent'te bulunan modern, 4 yıldızlı bir otel. Müşterilerimize konfor ve yüksek seviyede hizmet sunuyoruz.",
#     "ar": "ℹ️ *عن الشركة*\nفندق حديث من فئة 4 نجوم في طشقند. نحن نقدم الراحة وخدمة عالية المستوى لعملائنا."
# }
#
# # Location information
# location_info = {
#     "uz": "📍 *Manzil*\nToshkent shahri, Yunusobod tumani\n📍 *GPS:* 41.3310° N, 69.2805° E",
#     "ru": "📍 *Локация*\nг. Ташкент, Юнусабадский район\n📍 *GPS:* 41.3310° N, 69.2805° E",
#     "en": "📍 *Location*\nTashkent city, Yunusabad district\n📍 *GPS:* 41.3310° N, 69.2805° E",
#     "tr": "📍 *Konum*\nTaşkent şehri, Yunusabad ilçesi\n📍 *GPS:* 41.3310° N, 69.2805° E",
#     "ar": "📍 *الموقع*\nمدينة طشقند، حي يونوس آباد\n📍 *GPS:* 41.3310° N, 69.2805° E"
# }
#
# # ABOUT submenus
# about_submenus = {
#     "uz": {
#         "info": "📑 Ma'lumotlar",
#         "images": "🖼️ Rasmlar",
#         "location": "📍 Manzil",
#         "back": "🔙 Orqaga"
#     },
#     "ru": {
#         "info": "📑 Информация",
#         "images": "🖼️ Изображения",
#         "location": "📍 Локация",
#         "back": "🔙 Назад"
#     },
#     "en": {
#         "info": "📑 Information",
#         "images": "🖼️ Images",
#         "location": "📍 Location",
#         "back": "🔙 Back"
#     },
#     "tr": {
#         "info": "📑 Bilgiler",
#         "images": "🖼️ Görseller",
#         "location": "📍 Konum",
#         "back": "🔙 Geri"
#     },
#     "ar": {
#         "info": "📑 المعلومات",
#         "images": "🖼️ الصور",
#         "location": "📍 الموقع",
#         "back": "🔙 العودة"
#     }
# }
#
# # Language selection confirmation messages
# lang_confirmation = {
#     "uz": "🇺🇿 O'zbek tili tanlandi!",
#     "ru": "🇷🇺 Русский язык выбран!",
#     "en": "🇬🇧 English language chosen!",
#     "tr": "🇹🇷 Türkçe dili seçildi!",
#     "ar": "🇸🇦 العربية اللغة المختارة!"
# }
#
#
# # START COMMAND
# @dp.message(Command("start"))
# async def start_handler(message: Message):
#     await message.answer(
#         "Tilni tanlang / Choose language / Выберите язык / Dilinizi seçin / اختر اللغة 👇",
#         reply_markup=lang_kb
#     )
#
#
# # 1. LANGUAGE SELECTION HANDLER
# @dp.message(F.text.in_({"🇺🇿 O'zbek", "🇷🇺 Русский", "🇬🇧 English", "🇹🇷 Türkçe", "🇸🇦 العربية"}))
# async def choose_lang(message: Message):
#     user = message.from_user.id
#     lang = None
#     if message.text == "🇺🇿 O'zbek":
#         lang = "uz"
#     elif message.text == "🇷🇺 Русский":
#         lang = "ru"
#     elif message.text == "🇬🇧 English":
#         lang = "en"
#     elif message.text == "🇹🇷 Türkçe":
#         lang = "tr"
#     elif message.text == "🇸🇦 العربية":
#         lang = "ar"
#
#     if lang:
#         user_lang[user] = lang
#         await message.answer(lang_confirmation[lang], reply_markup=menus[lang])
#
#
# # 2. SOCIAL MEDIA MENYUSI
# @dp.message(
#     F.text.in_({"📱 Ijtimoiy Tarmoqlar", "📱 Соцсети", "📱 Social Media", "📱 Sosyal Medya", "📱 وسائل التواصل الاجتماعي"}))
# async def social_media_handler(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#     social_text = {
#         "uz": "Ijtimoiy tarmoqlarimiz:\n",
#         "ru": "Наши соцсети:\n",
#         "en": "Our social media:\n",
#         "tr": "Sosyal medya hesaplarımız:\n",
#         "ar": "وسائل التواصل الاجتماعي الخاصة بنا:\n"
#     }
#     await message.answer(social_text[lang], reply_markup=social_kb[lang])
#
#
# # 3. ORQAGA TUGMASI (Social media menyusidan asosiy menyuga)
# @dp.message(F.text.in_({"⬅️ Orqaga", "⬅️ Назад", "⬅️ Back", "⬅️ Geri", "⬅️ العودة"}))
# async def back_handler_social(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#     back_text = {
#         "uz": "Orqaga qaytildi",
#         "ru": "Назад",
#         "en": "Back",
#         "tr": "Geri",
#         "ar": "العودة"
#     }
#     await message.answer(back_text[lang], reply_markup=menus[lang])
#
#
# # SOCIAL MEDIA LINKLARI
# soc_map = {
#     "📸 Instagram": "instagram",
#     "📘 Facebook": "facebook",
#     "🎵 TikTok": "tiktok",
#     "▶️ YouTube": "youtube",
#     "🎥 RuTube": "rutube",
#     "🟦 VK": "vk"
# }
#
#
# @dp.message(F.text.in_(soc_map.keys()))
# async def social_media_links(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#     txt = message.text
#
#     key = soc_map.get(txt)
#     if key:
#         if lang in text_trans and key in text_trans[lang]:
#             await message.answer(
#                 f"{text_trans[lang][key]} {links[key]}",
#                 parse_mode="Markdown"
#             )
#         else:
#             await message.answer(
#                 f"{text_trans['en'][key]} {links[key]}",
#                 parse_mode="Markdown"
#             )
#
#
# # CONTACT HANDLER
# @dp.message(F.text.in_({"📞 Kontakt", "📞 Контакты", "📞 Contact", "📞 İletişim", "📞 الاتصال"}))
# async def contact_handler(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#     await message.answer(contact_text[lang], parse_mode="Markdown", reply_markup=menus[lang])
#
#
# # 4. ABOUT HANDLER (Main Menu) - FAKAT MENYU KO'RSATSIN
# @dp.message(F.text.in_({"ℹ️ Biz haqimizda", "ℹ️ О нас", "ℹ️ About", "ℹ️ Hakkımızda", "ℹ️ عن الشركة"}))
# async def about_handler(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#     submenu = about_submenus[lang]
#
#     # Menyu matni - FAKAT "Tanlang"
#     choose_text = {
#         "uz": "ℹ️ Tanlang:",
#         "ru": "ℹ️ Выберите:",
#         "en": "ℹ️ Choose:",
#         "tr": "ℹ️ Seçin:",
#         "ar": "ℹ️ اختر:"
#     }
#
#     kb = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text=submenu['info'])],
#             [KeyboardButton(text=submenu['images'])],
#             [KeyboardButton(text=submenu['location'])],
#             [KeyboardButton(text=submenu['back'])],
#         ],
#         resize_keyboard=True
#     )
#
#     await message.answer(choose_text[lang], reply_markup=kb)
#
#
# # 5. ABOUT INFORMATION HANDLER - ENDI FAQAT BU YERDA MA'LUMOT CHIQADI
# @dp.message(F.text.in_({"📑 Ma'lumotlar", "📑 Информация", "📑 Information", "📑 Bilgiler", "📑 المعلومات"}))
# async def about_info_handler(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#
#     # Ma'lumotlar matni
#     info_text = {
#         "uz": "📑 *Ma'lumotlar*\n\nZamonaviy, 4 yulduzli mehmonxona - Toshkent shahrida joylashgan. Biz mijozlarimizga qulaylik va yuqori darajadagi xizmatni taqdim etamiz.\n\n📍 *Manzil:* Toshkent shahri, Yunusobod tumani\n📞 *Telefon:* +998998897776\n📧 *Email:* sharqhotel2023@gmail.com",
#         "ru": "📑 *Информация*\n\nСовременный отель в Ташкенте с 4 звездами. Мы предлагаем комфорт и высокий уровень обслуживания для наших клиентов.\n\n📍 *Адрес:* г. Ташкент, Юнусабадский район\n📞 *Телефон:* +998998897776\n📧 *Email:* sharqhotel2023@gmail.com",
#         "en": "📑 *Information*\n\nA modern 4-star hotel located in Tashkent. We provide comfort and high-level service to our clients.\n\n📍 *Address:* Tashkent city, Yunusabad district\n📞 *Phone:* +998998897776\n📧 *Email:* sharqhotel2023@gmail.com",
#         "tr": "📑 *Bilgiler*\n\nTaşkent'te bulunan modern, 4 yıldızlı bir otel. Müşterilerimize konfor ve yüksek seviyede hizmet sunuyoruz.\n\n📍 *Adres:* Taşkent şehri, Yunusabad ilçesi\n📞 *Telefon:* +998998897776\n📧 *Email:* sharqhotel2023@gmail.com",
#         "ar": "📑 *المعلومات*\n\nفندق حديث من فئة 4 نجوم في طشقند. نحن نقدم الراحة وخدمة عالية المستوى لعملائنا.\n\n📍 *العنوان:* مدينة طشقند، حي يونوس آباد\n📞 *الهاتف:* +998998897776\n📧 *البريد الإلكتروني:* sharqhotel2023@gmail.com"
#     }
#
#     await message.answer(info_text[lang], parse_mode="Markdown")
#
#
# # 6. ABOUT IMAGES HANDLER - BARCHA RASMLARNI 1 TA ALBOMDA
# @dp.message(F.text.in_({"🖼️ Rasmlar", "🖼️ Изображения", "🖼️ Images", "🖼️ Görseller", "🖼️ الصور"}))
# async def about_images_handler(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#
#     # Avval xabar yuboramiz
#     images_text = {
#         "uz": "🏨 Mehmonxona rasmlari yuklanmoqda...",
#         "ru": "🏨 Загружаются изображения отеля...",
#         "en": "🏨 Loading hotel images...",
#         "tr": "🏨 Otel görselleri yükleniyor...",
#         "ar": "🏨 يتم تحميل صور الفندق..."
#     }
#
#     await message.answer(images_text[lang])
#
#     # Keyin albom yuboramiz
#     await send_photo_album(message, lang)
#
#
# async def send_photo_album(message: Message, lang: str):
#     """images/photo1.jpg dan photo7.jpg gacha BARCHA RASMLARNI 1 TA ALBOMDA YUBORISH"""
#
#     # images papkasini tekshirish
#     images_folder = "images"
#
#     # Agar papka bo'lmasa
#     if not os.path.exists(images_folder):
#         folder_text = {
#             "uz": "❌ 'images' papkasi topilmadi. Iltimos, bot fayli bilan bir papkada 'images' papkasini yarating.",
#             "ru": "❌ Папка 'images' не найдена. Пожалуйста, создайте папку 'images' в той же папке, что и бот.",
#             "en": "❌ 'images' folder not found. Please create 'images' folder in the same directory as the bot.",
#             "tr": "❌ 'images' klasörü bulunamadı. Lütfen bot dosyasıyla aynı dizinde 'images' klasörü oluşturun.",
#             "ar": "❌ لم يتم العثور على مجلد 'images'. يرجى إنشاء مجلد 'images' في نفس دليل البوت."
#         }
#
#         await message.answer(folder_text[lang])
#         return
#
#     # Rasm fayllarini yig'ish
#     media = []
#     total_found = 0
#
#     # Barcha mumkin bo'lgan rasm fayllarini qidirish
#     for i in range(1, 8):
#         # Har xil formatlarni tekshirish
#         possible_names = [
#             f"photo{i}.jpg", f"photo{i}.jpeg", f"photo{i}.png",
#             f"photo{i}.JPG", f"photo{i}.JPEG", f"photo{i}.PNG",
#             f"Photo{i}.jpg", f"Photo{i}.jpeg", f"Photo{i}.png"
#         ]
#
#         found = False
#         for name in possible_names:
#             file_path = os.path.join(images_folder, name)
#             if os.path.exists(file_path):
#                 try:
#                     # Rasmni media guruhga qo'shish
#                     photo = types.FSInputFile(file_path)
#
#                     # Agar bu birinchi rasm bo'lsa, caption qo'shamiz
#                     if total_found == 0:
#                         caption_text = {
#                             "uz": f"🏨 HL 309 Hotel - {i}-rasm\n📍 Toshkent shahri, Yunusobod tumani\n📞 +998998897776",
#                             "ru": f"🏨 HL 309 Hotel - {i}-изображение\n📍 г. Ташкент, Юнусабадский район\n📞 +998998897776",
#                             "en": f"🏨 HL 309 Hotel - {i}-image\n📍 Tashkent city, Yunusabad district\n📞 +998998897776",
#                             "tr": f"🏨 HL 309 Hotel - {i}-görsel\n📍 Taşkent şehri, Yunusabad ilçesi\n📞 +998998897776",
#                             "ar": f"🏨 فندق HL 309 - {i}-صورة\n📍 مدينة طشقند، حي يونوس آباد\n📞 +998998897776"
#                         }
#
#                         caption = caption_text.get(lang, f"HL 309 Hotel - {i}-image")
#                         media.append(InputMediaPhoto(media=photo, caption=caption))
#                     else:
#                         # Qolgan rasmlarga caption qo'shmaymiz
#                         media.append(InputMediaPhoto(media=photo))
#
#                     total_found += 1
#                     found = True
#                     print(f"✅ Rasm {i} topildi: {name}")
#                     break
#
#                 except Exception as e:
#                     print(f"⚠️ Rasm {i} yuklashda xatolik: {str(e)}")
#                     continue
#
#         if not found:
#             print(f"ℹ️ Rasm {i} topilmadi")
#
#     # Agar hech qanday rasm topilmasa
#     if total_found == 0:
#         no_images_text = {
#             "uz": "❌ 'images' papkasida hech qanday rasm topilmadi. Iltimos, rasmlarni quyidagi nomda joylashtiring:\n\nphoto1.jpg\nphoto2.jpg\nphoto3.jpg\nphoto4.jpg\nphoto5.jpg\nphoto6.jpg\nphoto7.jpg",
#             "ru": "❌ В папке 'images' не найдено изображений. Пожалуйста, разместите изображения со следующими именами:\n\nphoto1.jpg\nphoto2.jpg\nphoto3.jpg\nphoto4.jpg\nphoto5.jpg\nphoto6.jpg\nphoto7.jpg",
#             "en": "❌ No images found in 'images' folder. Please place images with the following names:\n\nphoto1.jpg\nphoto2.jpg\nphoto3.jpg\nphoto4.jpg\nphoto5.jpg\nphoto6.jpg\nphoto7.jpg",
#             "tr": "❌ 'images' klasöründe hiçbir görsel bulunamadı. Lütfen görselleri aşağıdaki isimlerle yerleştirin:\n\nphoto1.jpg\nphoto2.jpg\nphoto3.jpg\nphoto4.jpg\nphoto5.jpg\nphoto6.jpg\nphoto7.jpg",
#             "ar": "❌ لم يتم العثور على أي صور في مجلد 'images'. يرجى وضع الصور بالأسماء التالية:\n\nphoto1.jpg\nphoto2.jpg\nphoto3.jpg\nphoto4.jpg\nphoto5.jpg\nphoto6.jpg\nphoto7.jpg"
#         }
#
#         await message.answer(no_images_text[lang])
#         return
#
#     # Albomni yuborish
#     try:
#         # Telegram albom chegarasi - bir martada maksimum 10 ta media
#         if len(media) > 10:
#             # Agar 10 tadan ko'p bo'lsa, bo'lib yuboramiz
#             for i in range(0, len(media), 10):
#                 chunk = media[i:i + 10]
#                 await message.answer_media_group(chunk)
#                 await asyncio.sleep(0.5)  # Kichik kechikish
#         else:
#             # 10 tadan kam bo'lsa, bir martada yuboramiz
#             await message.answer_media_group(media)
#
#         # Natija haqida xabar
#         result_text = {
#             "uz": f"✅ {total_found} ta rasm albom shaklida yuborildi!",
#             "ru": f"✅ {total_found} изображений отправлены в виде альбома!",
#             "en": f"✅ {total_found} images sent as an album!",
#             "tr": f"✅ {total_found} görsel albüm şeklinde gönderildi!",
#             "ar": f"✅ تم إرسال {total_found} صورة على شكل ألبوم!"
#         }
#
#         await message.answer(result_text[lang])
#
#     except Exception as e:
#         print(f"❌ Albom yuborishda xatolik: {str(e)}")
#
#         # Xato haqida xabar
#         error_text = {
#             "uz": "⚠️ Albom yuborishda texnik xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.",
#             "ru": "⚠️ Произошла техническая ошибка при отправке альбома. Пожалуйста, попробуйте позже.",
#             "en": "⚠️ A technical error occurred while sending the album. Please try again later.",
#             "tr": "⚠️ Albüm gönderilirken teknik bir hata oluştu. Lütfen daha sonra tekrar deneyin.",
#             "ar": "⚠️ حدث خطأ تقني أثناء إرسال الألبوم. يرجى المحاولة مرة أخرى لاحقًا."
#         }
#
#         await message.answer(error_text[lang])
#
#
# # 7. ABOUT LOCATION HANDLER - XARITA TASHLASH
# @dp.message(F.text.in_({"📍 Manzil", "📍 Локация", "📍 Location", "📍 Konum", "📍 الموقع"}))
# async def about_location_handler(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#
#     # Location ma'lumotlarini yuborish
#     await message.answer(location_info[lang], parse_mode="Markdown")
#
#     # Xaritani tashlash
#     await send_map_location(message, lang)
#
#
# async def send_map_location(message: Message, lang: str):
#     """Xaritani jo'natish funksiyasi"""
#     # Google Maps location (latitude, longitude)
#     latitude = 41.3310
#     longitude = 69.2805
#
#     try:
#         # 1. TELEGRAM LOCATION XUSUSIYATI ORQALI XARITA JO'NATISH
#         await message.answer_location(
#             latitude=latitude,
#             longitude=longitude,
#             horizontal_accuracy=50
#         )
#
#         # Xarita haqida xabar
#         map_text = {
#             "uz": "📍 Mehmonxona joylashuvi yuborildi. Telegram xaritasida ko'ring.",
#             "ru": "📍 Местоположение отеля отправлено. Посмотрите в картах Telegram.",
#             "en": "📍 Hotel location sent. View in Telegram maps.",
#             "tr": "📍 Otel konumu gönderildi. Telegram haritalarında görüntüleyin.",
#             "ar": "📍 تم إرسال موقع الفندق. اعرض في خرائط Telegram."
#         }
#
#         await message.answer(map_text[lang])
#
#         # 2. GOOGLE MAPS HAVOLASI
#         google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
#
#         # Havola matni tilda
#         link_text = {
#             "uz": "📍 Google Mapsda ochish:",
#             "ru": "📍 Открыть в Google Maps:",
#             "en": "📍 Open in Google Maps:",
#             "tr": "📍 Google Haritalar'da aç:",
#             "ar": "📍 فتح في خرائط جوجل:"
#         }
#
#         await message.answer(f"{link_text.get(lang, 'Open in Google Maps:')}\n{google_maps_link}")
#
#     except Exception as e:
#         # Agar location jo'natishda xatolik bo'lsa
#         error_text = {
#             "uz": "📍 Mehmonxona manzili:\nToshkent shahri, Yunusobod tumani\n📍 Google Maps: https://goo.gl/maps/example",
#             "ru": "📍 Адрес отеля:\nг. Ташкент, Юнусабадский район\n📍 Google Maps: https://goo.gl/maps/example",
#             "en": "📍 Hotel address:\nTashkent city, Yunusabad district\n📍 Google Maps: https://goo.gl/maps/example",
#             "tr": "📍 Otel adresi:\nTaşkent şehri, Yunusabad ilçesi\n📍 Google Maps: https://goo.gl/maps/example",
#             "ar": "📍 عنوان الفندق:\nمدينة طشقند، حي يونوس آباد\n📍 خرائط جوجل: https://goo.gl/maps/example"
#         }
#
#         await message.answer(error_text[lang])
#
#
# # 8. ABOUT MENYUSIDAGI ORQAGA TUGMASI
# @dp.message(F.text.in_({"🔙 Orqaga", "🔙 Назад", "🔙 Back", "🔙 Geri", "🔙 العودة"}))
# async def back_handler_about(message: Message):
#     user = message.from_user.id
#     lang = user_lang.get(user, "uz")
#     back_text = {
#         "uz": "Asosiy menyuga qaytildi",
#         "ru": "Вернуться в главное меню",
#         "en": "Returned to main menu",
#         "tr": "Ana menüye dönüldü",
#         "ar": "العودة إلى القائمة الرئيسية"
#     }
#     await message.answer(back_text[lang], reply_markup=menus[lang])
#
#
# # CHANGE LANGUAGE HANDLER
# @dp.message(
#     F.text.in_({"🌍 Tilni o'zgartirish", "🌍 Изменить язык", "🌍 Change language", "🌍 Dil değiştir", "🌍 تغيير اللغة"}))
# async def change_lang_handler(message: Message):
#     await message.answer(
#         "Tilni tanlang / Choose language / Выберите язык / Dilinizi seçin / اختر اللغة 👇",
#         reply_markup=lang_kb
#     )
#
#
# # Main bot polling function
# async def main():
#     print("=" * 50)
#     print("🤖 HL 309 Hotel Bot ishga tushdi!")
#     print("=" * 50)
#
#     # images papkasini tekshirish
#     images_folder = "images"
#
#     if not os.path.exists(images_folder):
#         print(f"⚠️ '{images_folder}' papkasi topilmadi.")
#         print(f"ℹ️ Bot faqatgina '{images_folder}' papkasidagi rasmlarni yuboradi.")
#     else:
#         print(f"✅ '{images_folder}' papkasi topildi!")
#
#         # Papkadagi rasm fayllarini tekshirish
#         print("\n🔍 Rasm fayllarini tekshiryapmiz...")
#         found_images = []
#
#         for i in range(1, 8):
#             found = False
#             possible_names = [
#                 f"photo{i}.jpg", f"photo{i}.jpeg", f"photo{i}.png",
#                 f"photo{i}.JPG", f"photo{i}.JPEG", f"photo{i}.PNG"
#             ]
#
#             for name in possible_names:
#                 file_path = os.path.join(images_folder, name)
#                 if os.path.exists(file_path):
#                     found_images.append((i, name))
#                     found = True
#                     break
#
#             if found:
#                 print(f"   ✅ photo{i} - TOPILDI")
#             else:
#                 print(f"   ❌ photo{i} - TOPILMADI")
#
#         if found_images:
#             print(f"\n📊 Jami {len(found_images)} ta rasm topildi.")
#         else:
#             print("\n⚠️ Hech qanday rasm topilmadi!")
#
#     print("\n📸 Bot RASMLARNI 1 TA ALBOMDA YUBORISH funksiyasi yoqildi")
#     print("🗺️ Xarita funksiyasi yoqildi")
#     print("ℹ️ 'Biz haqimizda' faqat menyu ko'rsatadi")
#     print("📑 'Ma'lumotlar' tugmasida ma'lumotlar chiqadi")
#     print("=" * 50)
#
#     await dp.start_polling(bot)
#
#
# # Start the bot
# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto, FSInputFile
from aiogram.filters import Command
from dotenv import load_dotenv

# ============================
# KONFIGURATSIYA
# ============================
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

if API_TOKEN is None:
    print("❌ XATO: API_TOKEN environment variable not set.")
    API_TOKEN = input("Iltimos, Telegram Bot Tokenini kiriting: ").strip()
    if not API_TOKEN:
        print("❌ Token kiritilmadi. Dastur to'xtatildi.")
        exit(1)
else:
    print(f"✅ Bot tokeni .env faylidan muvaffaqiyatli o'qildi")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
user_data = {}


# ============================
# DEBOUNCE DECORATOR
# ============================
def debounce(seconds=1):
    def decorator(func):
        async def wrapper(message: Message):
            user_id = message.from_user.id
            now = datetime.now()

            if user_id in user_data and "last_request" in user_data[user_id]:
                last_time = user_data[user_id]["last_request"]
                if (now - last_time).seconds < seconds:
                    lang = user_data[user_id].get("lang", "uz")
                    warning_msg = {
                        "uz": "⏳ Iltimos, biroz kuting!",
                        "ru": "⏳ Пожалуйста, подождите!",
                        "en": "⏳ Please wait a moment!",
                        "tr": "⏳ Lütfen bekleyin!",
                        "ar": "⏳ انتظر قليلاً!"
                    }
                    await message.answer(warning_msg.get(lang, "⏳ Please wait!"))
                    return

            if user_id not in user_data:
                user_data[user_id] = {}
            user_data[user_id]["last_request"] = now

            return await func(message)

        return wrapper

    return decorator


# ============================
# KLAVISHATURALAR
# ============================
lang_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbek")],
        [KeyboardButton(text="🇷🇺 Русский")],
        [KeyboardButton(text="🇬🇧 English")],
        [KeyboardButton(text="🇹🇷 Türkçe")],
        [KeyboardButton(text="🇸🇦 العربية")]
    ],
    resize_keyboard=True
)


def get_main_menu(lang="uz"):
    menus = {
        "uz": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Ijtimoiy Tarmoqlar")],
                [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="📞 Kontakt")],
                [KeyboardButton(text="🌍 Tilni o'zgartirish")]
            ],
            resize_keyboard=True
        ),
        "ru": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Соцсети")],
                [KeyboardButton(text="ℹ️ О нас"), KeyboardButton(text="📞 Контакты")],
                [KeyboardButton(text="🌍 Изменить язык")]
            ],
            resize_keyboard=True
        ),
        "en": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Social Media")],
                [KeyboardButton(text="ℹ️ About"), KeyboardButton(text="📞 Contact")],
                [KeyboardButton(text="🌍 Change language")]
            ],
            resize_keyboard=True
        ),
        "tr": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Sosyal Medya")],
                [KeyboardButton(text="ℹ️ Hakkımızda"), KeyboardButton(text="📞 İletişим")],
                [KeyboardButton(text="🌍 Dil değiştir")]
            ],
            resize_keyboard=True
        ),
        "ar": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 وسائل التواصل الاجتماعي")],
                [KeyboardButton(text="ℹ️ عن الشركة"), KeyboardButton(text="📞 الاتصال")],
                [KeyboardButton(text="🌍 تغيير اللغة")]
            ],
            resize_keyboard=True
        ),
    }
    return menus.get(lang, menus["uz"])


def get_social_menu(lang="uz"):
    social_menus = {
        "uz": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
                [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
                [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
                [KeyboardButton(text="⬅️ Orqaga")]
            ],
            resize_keyboard=True
        ),
        "ru": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
                [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
                [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
                [KeyboardButton(text="⬅️ Назад")]
            ],
            resize_keyboard=True
        ),
        "en": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
                [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
                [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
                [KeyboardButton(text="⬅️ Back")]
            ],
            resize_keyboard=True
        ),
        "tr": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
                [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
                [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
                [KeyboardButton(text="⬅️ Geri")]
            ],
            resize_keyboard=True
        ),
        "ar": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📸 Instagram"), KeyboardButton(text="📘 Facebook")],
                [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
                [KeyboardButton(text="🎥 RuTube"), KeyboardButton(text="🟦 VK")],
                [KeyboardButton(text="⬅️ العودة")]
            ],
            resize_keyboard=True
        )
    }
    return social_menus.get(lang, social_menus["uz"])


def get_about_menu(lang="uz"):
    about_menus = {
        "uz": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📑 Ma'lumotlar")],
                [KeyboardButton(text="🖼️ Rasmlar"), KeyboardButton(text="📍 Manzil")],
                [KeyboardButton(text="🔙 Orqaga")]
            ],
            resize_keyboard=True
        ),
        "ru": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📑 Информация")],
                [KeyboardButton(text="🖼️ Изображения"), KeyboardButton(text="📍 Локация")],
                [KeyboardButton(text="🔙 Назад")]
            ],
            resize_keyboard=True
        ),
        "en": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📑 Information")],
                [KeyboardButton(text="🖼️ Images"), KeyboardButton(text="📍 Location")],
                [KeyboardButton(text="🔙 Back")]
            ],
            resize_keyboard=True
        ),
        "tr": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📑 Bilgiler")],
                [KeyboardButton(text="🖼️ Görseller"), KeyboardButton(text="📍 Konum")],
                [KeyboardButton(text="🔙 Geri")]
            ],
            resize_keyboard=True
        ),
        "ar": ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📑 المعلومات")],
                [KeyboardButton(text="🖼️ الصور"), KeyboardButton(text="📍 الموقع")],
                [KeyboardButton(text="🔙 العودة")]
            ],
            resize_keyboard=True
        )
    }
    return about_menus.get(lang, about_menus["uz"])


# ============================
# MATN VA MA'LUMOTLAR
# ============================
lang_confirmation = {
    "uz": "🇺🇿 O'zbek tili tanlandi!",
    "ru": "🇷🇺 Русский язык выбран!",
    "en": "🇬🇧 English language chosen!",
    "tr": "🇹🇷 Türkçe dili seçildi!",
    "ar": "🇸🇦 العربية اللغة المختارة!"
}

SOCIAL_LINKS = {
    "instagram": "https://www.instagram.com/hl309.hotel?igsh=OGptZjBlNHJkeDg=",
    "facebook": "https://www.facebook.com/share/1ANcayRW58/",
    "tiktok": "https://www.tiktok.com/@hlhotel.uz?_r=1&_t=ZM-91gzTyn1lDE",
    "youtube": "https://www.youtube.com/@HL309",
    "rutube": "https://rutube.ru/channel/31606755/",
    "vk": "https://vk.com/hl309"
}

social_texts = {
    "uz": {
        "instagram": "📸 Instagram sahifamiz:\n",
        "facebook": "📘 Facebook sahifamiz:\n",
        "tiktok": "🎵 TikTok sahifamiz:\n",
        "youtube": "▶️ YouTube kanalimiz:\n",
        "rutube": "🎥 RuTube kanalimiz:\n",
        "vk": "🟦 VK sahifamiz:\n"
    },
    "ru": {
        "instagram": "📸 Наша страница Instagram:\n",
        "facebook": "📘 Наша страница Facebook:\n",
        "tiktok": "🎵 Наш TikTok:\n",
        "youtube": "▶️ Наш YouTube канал:\n",
        "rutube": "🎥 Наш RuTube канал:\n",
        "vk": "🟦 Наша страница VK:\n"
    },
    "en": {
        "instagram": "📸 Our Instagram page:\n",
        "facebook": "📘 Our Facebook page:\n",
        "tiktok": "🎵 Our TikTok page:\n",
        "youtube": "▶️ Our YouTube channel:\n",
        "rutube": "🎥 Our RuTube channel:\n",
        "vk": "🟦 Our VK page:\n"
    },
    "tr": {
        "instagram": "📸 Instagram sayfamız:\n",
        "facebook": "📘 Facebook sayfamız:\n",
        "tiktok": "🎵 TikTok sayfamız:\n",
        "youtube": "▶️ YouTube kanalımız:\n",
        "rutube": "🎥 RuTube kanalımız:\n",
        "vk": "🟦 VK sayfamız:\n"
    },
    "ar": {
        "instagram": "📸 صفحتنا على Instagram:\n",
        "facebook": "📘 صفحتنا على فيسبوك:\n",
        "tiktok": "🎵 صفحتنا على TikTok:\n",
        "youtube": "▶️ قناتنا على YouTube:\n",
        "rutube": "🎥 قناتنا على RuTube:\n",
        "vk": "🟦 صفحتنا على VK:\n"
    }
}

contact_info = {
    "uz": "📞 Kontaktlar\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
    "ru": "📞 Контакты\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
    "en": "📞 Contact\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
    "tr": "📞 İletişim\n📱 +998998897776\n📧 sharqhotel2023@gmail.com",
    "ar": "📞 الاتصال\n📱 +998998897776\n📧 sharqhotel2023@gmail.com"
}

about_info = {
    "uz": "ℹ️ Biz haqimizda\n"
          "Zamonaviy, 4 yulduzli «⭐️⭐️⭐️⭐️» mehmonxona — O'zbekistonning Toshkent "
          "shahrida, biznes va tarixiy markazda joylashgan.\n\n"
          "Mehmonlarimizga standart, delyuks, lyuks hamda villa turdagi xonalarni taklif etamiz.\n\n"
          "Yozgi ochiq basseyn, yashil hudud, SPA-markazi, sport zali va restoran mavjud.\n\n"
          "Batafsil: hlgroup.uz",

    "ru": "ℹ️ О нас\n"
          "Современный отель соответствующий стандартам – 4 звезды «⭐️⭐️⭐️⭐️» "
          "Расположенный в Узбекистане г.Ташкент в деловом-историческом центре.\n\n"
          "Предлагает вашему вниманию спектор номеров от стандартного, делюксы, люксы, виллы.\n\n"
          "С открытым летним бассейном, зелёной территорией SPA-центром, "
          "спортивным залом и рестораном детальное описание при бронировании и на сайте hlgroup.uz",

    "en": "ℹ️ About us\n"
          "A modern four-star hotel (⭐️⭐️⭐️⭐️) located in the business and historical center of Tashkent, Uzbekistan.\n\n"
          "We offer a wide selection of rooms, including Standard, Deluxe, Suite, and Villa accommodations.\n\n"
          "Guests can enjoy an outdoor summer pool, green landscaped area, SPA center, fitness gym, and an on-site restaurant.\n\n"
          "Detailed information is available during booking and on our website: hlgroup.uz",

    "tr": "ℹ️ Hakkımızda\n"
          "Modern, dört yıldızlı «⭐️⭐️⭐️⭐️» otel — Özbekistan'ın Taşkent şehrinde, iş ve tarihi merkezde yer almaktadır.\n\n"
          "Misafirlerimize standart, delüks, süit ve villa tipi odalar sunuyoruz.\n\n"
          "Yazlık açık havuz, yeşil alan, SPA merkezi, spor salonu ve restoran mevcuttur.\n\n"
          "Detaylı bilgi: hlgroup.uz",

    "ar": "ℹ️ عنا\n"
          "فندق حديث من فئة 4 نجوم «⭐️⭐️⭐️⭐️» يقع في طشقند، أوزبكستان، في المركز التجاري والتاريخي.\n\n"
          "نقدم لضيوفنا غرفًا من أنواع: ستاندرد، ديلوكس، جناح، وفيلا.\n\n"
          "يتوفر مسبح صيفي مفتوح، منطقة خضراء، مركز سبا، صالة رياضية ومطعم.\n\n"
          "مزيد من التفاصيل: hlgroup.uz"
}

location_info = {
    "uz": "📍 Manzil\nToshkent shahri, Rakatboshi ko'chasi 3A\n📍 *GPS:* 41.30390° N, 69.26108° E",
    "ru": "📍 Локация\nг. Ташкент, ул. Ракатбоши 3A\n📍 *GPS:* 41.30390° N, 69.26108° E",
    "en": "📍 Location\nTashkent city, Rakatboshi street 3A\n📍 *GPS:* 41.30390° N, 69.26108° E",
    "tr": "📍 Konum\nTaşkent şehri, Rakatboshi cad. 3A\n📍 *GPS:* 41.30390° N, 69.26108° E",
    "ar": "📍الموقع\nمدينة طشقند، شارع راكاتبوشي 3A\n📍 *GPS:* 41.30390° N, 69.26108° E"
}


# ============================
# RASMLARNI O'QISH FUNKTSIYASI - TEZ VERSIYA
# ============================
def get_image_files():
    """images papkasidagi rasm fayllarini tez o'qish"""
    if not os.path.exists("images"):
        return []

    image_files = []
    image_extensions = {'.jpg', '.jpeg', '.png', '.jfif', '.webp', '.bmp', '.gif'}

    # Oson tekshirish
    try:
        for filename in os.listdir("images"):
            file_path = os.path.join("images", filename)

            # Faqat oddiy fayllar
            if not os.path.isfile(file_path):
                continue

            # Tez kengaytma tekshirish
            ext = os.path.splitext(filename)[1].lower()
            if ext in image_extensions:
                image_files.append(file_path)
    except Exception as e:
        print(f"❌ Papka o'qish xatosi: {e}")
        return []

    # Nom bo'yicha tartiblash
    image_files.sort()
    return image_files


# ============================
# RASMLARNI YUBORISH - OLDINDAN TAYYORLASH BILAN
# ============================
async def send_images_optimized(message: Message, lang: str):
    """Rasmlarni optimallashtirilgan tarzda yuborish"""

    # 1. Rasmlarni olish
    image_files = get_image_files()

    if not image_files:
        no_images_text = {
            "uz": "❌ Hech qanday rasm topilmadi!",
            "ru": "❌ Изображения не найдены!",
            "en": "❌ No images found!",
            "tr": "❌ Görsel bulunamadı!",
            "ar": "❌ لم يتم العثور على صور!"
        }
        await message.answer(no_images_text.get(lang, "❌ No images found!"))
        return

    total_images = len(image_files)
    print(f"🚀 {total_images} ta rasm topildi")

    # 2. Rasmlarni bir vaqtning o'zida yuborish
    try:
        # Agar 10 tadan kam bo'lsa, bitta albomda
        if total_images <= 10:
            media_group = []

            for i, img_path in enumerate(image_files):
                photo = FSInputFile(img_path)

                if i == 0:  # Birinchi rasm uchun caption
                    caption_text = {
                        "uz": f"🏨 HL 309 Hotel\n📍 Toshkent shahri, Rakatboshi ko'chasi 3A\n📞 +998998897776\n📸 Jami: {total_images} ta rasm",
                        "ru": f"🏨 HL 309 Hotel\n📍 г. Ташкент, ул. Ракатбоши 3A\n📞 +998998897776\n📸 Всего: {total_images} изображений",
                        "en": f"🏨 HL 309 Hotel\n📍 Tashkent city, Rakatboshi street 3A\n📞 +998998897776\n📸 Total: {total_images} images",
                        "tr": f"🏨 HL 309 Hotel\n📍 Taşkent şehri, Rakatboshi cad. 3A\n📞 +998998897776\n📸 Toplam: {total_images} görsel",
                        "ar": f"🏨 فندق HL 309\n📍 nمدينة طشقند، شارع راكاتبوشي\n📞 +998998897776\n📸 المجموع: {total_images} صورة"
                    }
                    caption = caption_text.get(lang, f"🏨 HL 309 Hotel\nTotal: {total_images} images")
                    media_group.append(InputMediaPhoto(media=photo, caption=caption))
                else:
                    media_group.append(InputMediaPhoto(media=photo))

            # Barcha rasmlarni bir vaqtda yuborish
            await message.answer_media_group(media_group)

        else:
            # 10 tadan ko'p bo'lsa, parallel yuborish
            num_albums = (total_images + 9) // 10

            for album_num in range(num_albums):
                start_idx = album_num * 10
                end_idx = min(start_idx + 10, total_images)
                album_images = image_files[start_idx:end_idx]

                media_group = []
                for i, img_path in enumerate(album_images):
                    photo = FSInputFile(img_path)

                    if i == 0:  # Har bir albomning birinchi rasmi uchun caption
                        if album_num == 0:
                            caption_text = {
                                "uz": f"🏨 HL 309 Hotel\n📍 Toshkent shahri, Yunusobod tumani\n📞 +998998897776\n📸 Jami: {total_images} ta rasm (1/{num_albums})",
                                "ru": f"🏨 HL 309 Hotel\n📍 г. Ташкент, Юнусабадский район\n📞 +998998897776\n📸 Всего: {total_images} изображений (1/{num_albums})",
                                "en": f"🏨 HL 309 Hotel\n📍 Tashkent city, Yunusabad district\n📞 +998998897776\n📸 Total: {total_images} images (1/{num_albums})",
                                "tr": f"🏨 HL 309 Hotel\n📍 Taşkent şehri, Yunusabad ilçesi\n📞 +998998897776\n📸 Toplam: {total_images} görsel (1/{num_albums})",
                                "ar": f"🏨 فندق HL 309\n📍 مدينة طشقند، حي يونوس آباد\n📞 +998998897776\n📸 المجموع: {total_images} صورة (1/{num_albums})"
                            }
                        else:
                            caption_text = {
                                "uz": f"🏨 HL 309 Hotel\n📸 Albom {album_num + 1}/{num_albums}",
                                "ru": f"🏨 HL 309 Hotel\n📸 Альбом {album_num + 1}/{num_albums}",
                                "en": f"🏨 HL 309 Hotel\n📸 Album {album_num + 1}/{num_albums}",
                                "tr": f"🏨 HL 309 Hotel\n📸 Albüm {album_num + 1}/{num_albums}",
                                "ar": f"🏨 فندق HL 309\n📸 الألبوم {album_num + 1}/{num_albums}"
                            }
                        caption = caption_text.get(lang, f"🏨 HL 309 Hotel\nAlbum {album_num + 1}/{num_albums}")
                        media_group.append(InputMediaPhoto(media=photo, caption=caption))
                    else:
                        media_group.append(InputMediaPhoto(media=photo))

                # Albomni yuborish
                await message.answer_media_group(media_group)

                # Keyingi albom uchun kichik kutish (agar kerak bo'lsa)
                if album_num < num_albums - 1 and num_albums > 1:
                    await asyncio.sleep(0.1)  # Juda qisqa kutish

        # 3. Muvaffaqiyat xabari
        # success_text = {
        #     "uz": f"✅ {total_images} ta rasm muvaffaqiyatli yuborildi!",
        #     "ru": f"✅ {total_images} изображений успешно отправлены!",
        #     "en": f"✅ {total_images} images sent successfully!",
        #     "tr": f"✅ {total_images} görsel başarıyla gönderildi!",
        #     "ar": f"✅ تم إرسال {total_images} صورة بنجاح!"
        # }
        # await message.answer(success_text.get(lang, f"✅ {total_images} images sent!"))

    except Exception as e:
        print(f"❌ Rasm yuborish xatosi: {e}")
        error_text = {
            "uz": "❌ Rasm yuborishda xatolik yuz berdi!",
            "ru": "❌ Ошибка при отправке изображений!",
            "en": "❌ Error sending images!",
            "tr": "❌ Görsel gönderilirken hata!",
            "ar": "❌ خطأ في إرسال الصور!"
        }
        await message.answer(error_text.get(lang, "❌ Error sending images!"))


# ============================
# HANDLER FUNKTSIYALARI
# ============================

@dp.message(Command("start"))
@debounce()
async def start_handler(message: Message):
    await message.answer(
        "Tilni tanlang / Choose language / Выберите язык / Dilinizi seçin / اختر اللغة 👇",
        reply_markup=lang_kb
    )


@dp.message(F.text.in_(["🇺🇿 O'zbek", "🇷🇺 Русский", "🇬🇧 English", "🇹🇷 Türkçe", "🇸🇦 العربية"]))
@debounce()
async def language_handler(message: Message):
    user_id = message.from_user.id

    lang_map = {
        "🇺🇿 O'zbek": "uz",
        "🇷🇺 Русский": "ru",
        "🇬🇧 English": "en",
        "🇹🇷 Türkçe": "tr",
        "🇸🇦 العربية": "ar"
    }

    lang = lang_map.get(message.text, "uz")

    if user_id not in user_data:
        user_data[user_id] = {}
    user_data[user_id]["lang"] = lang

    await message.answer(lang_confirmation[lang], reply_markup=get_main_menu(lang))


@dp.message(
    F.text.in_(["📱 Ijtimoiy Tarmoqlar", "📱 Соцсети", "📱 Social Media", "📱 Sosyal Medya", "📱 وسائل التواصل الاجتماعي"]))
@debounce()
async def social_menu_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    welcome_text = {
        "uz": "Ijtimoiy tarmoqlarimiz:",
        "ru": "Наши соцсети:",
        "en": "Our social media:",
        "tr": "Sosyal medya hesaplarımız:",
        "ar": "وسائل التواصل الاجتماعي الخاصة بنا:"
    }

    await message.answer(welcome_text.get(lang, "Our social media:"), reply_markup=get_social_menu(lang))


soc_map = {
    "📸 Instagram": "instagram",
    "📘 Facebook": "facebook",
    "🎵 TikTok": "tiktok",
    "▶️ YouTube": "youtube",
    "🎥 RuTube": "rutube",
    "🟦 VK": "vk"
}


@dp.message(F.text.in_(soc_map.keys()))
@debounce()
async def social_links_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    platform = soc_map[message.text]
    text = social_texts.get(lang, social_texts["en"]).get(platform, "")

    await message.answer(f"{text}{SOCIAL_LINKS[platform]}")


@dp.message(F.text.in_(["📞 Kontakt", "📞 Контакты", "📞 Contact", "📞 İletişim", "📞 الاتصال"]))
@debounce()
async def contact_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    await message.answer(contact_info.get(lang, contact_info["en"]), reply_markup=get_main_menu(lang))


@dp.message(F.text.in_(["ℹ️ Biz haqimizda", "ℹ️ О нас", "ℹ️ About", "ℹ️ Hakkımızda", "ℹ️ عن الشركة"]))
@debounce()
async def about_menu_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    choose_text = {
        "uz": "ℹ️ Tanlang:",
        "ru": "ℹ️ Выберите:",
        "en": "ℹ️ Choose:",
        "tr": "ℹ️ Seçin:",
        "ar": "ℹ️ اختر:"
    }

    await message.answer(choose_text.get(lang, "ℹ️ Choose:"), reply_markup=get_about_menu(lang))


@dp.message(F.text.in_(["📑 Ma'lumotlar", "📑 Информация", "📑 Information", "📑 Bilgiler", "📑 المعلومات"]))
@debounce()
async def about_info_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    await message.answer(about_info.get(lang, about_info["en"]))


# TEZLASHTIRILGAN RASMLAR HANDLERI
@dp.message(F.text.in_(["🖼️ Rasmlar", "🖼️ Изображения", "🖼️ Images", "🖼️ Görseller", "🖼️ الصور"]))
@debounce(seconds=1)  # Faqat 1 soniya debounce
async def images_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    # Tez yuklash xabari (faqat tasdiq uchun)
    loading_text = {
        "uz": "🚀 Rasmlar yuklanmoqda...",
        "ru": "🚀 Изображения загружаются...",
        "en": "🚀 Loading images...",
        "tr": "🚀 Görseller yükleniyor...",
        "ar": "🚀 يتم تحميل الصور..."
    }

    await message.answer(loading_text.get(lang, "🚀 Loading images..."))

    # Tez yuklash
    await send_images_optimized(message, lang)


@dp.message(F.text.in_(["📍 Manzil", "📍 Локация", "📍 Location", "📍 Konum", "📍 الموقع"]))
@debounce()
async def location_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    await message.answer(location_info.get(lang, location_info["en"]))

    try:
        latitude = 41.30390
        longitude = 69.26108

        await message.answer_location(
            latitude=latitude,
            longitude=longitude,
            horizontal_accuracy=50
        )

        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        map_text = {
            "uz": "📍 Google Mapsda ochish:",
            "ru": "📍 Открыть в Google Maps:",
            "en": "📍 Open in Google Maps:",
            "tr": "📍 Google Haritalar'da aç:",
            "ar": "📍 فتح في خرائط جوجل:"
        }

        await message.answer(f"{map_text.get(lang, '📍 Open in Google Maps:')}\n{google_maps_link}")

    except Exception as e:
        print(f"❌ Xarita yuborish xatosi: {e}")


@dp.message(F.text.in_(["⬅️ Orqaga", "⬅️ Назад", "⬅️ Back", "⬅️ Geri", "⬅️ العودة"]))
@debounce()
async def back_social_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    await message.answer("↩️", reply_markup=get_main_menu(lang))


@dp.message(F.text.in_(["🔙 Orqaga", "🔙 Назад", "🔙 Back", "🔙 Geri", "🔙 العودة"]))
@debounce()
async def back_about_handler(message: Message):
    user_id = message.from_user.id
    lang = user_data.get(user_id, {}).get("lang", "uz")

    back_text = {
        "uz": "Asosiy menyuga qaytildi",
        "ru": "Вернуться в главное меню",
        "en": "Returned to main menu",
        "tr": "Ana menüye dönüldü",
        "ar": "العودة إلى القائمة الرئيسية"
    }

    await message.answer(back_text.get(lang, "Back to main menu"), reply_markup=get_main_menu(lang))


@dp.message(
    F.text.in_(["🌍 Tilni o'zgartirish", "🌍 Изменить язык", "🌍 Change language", "🌍 Dil değiştir", "🌍 تغيير اللغة"]))
@debounce()
async def change_language_handler(message: Message):
    await message.answer(
        "Tilni tanlang / Choose language / Выберите язык / Dilinizi seçin / اختر اللغة 👇",
        reply_markup=lang_kb
    )


# ============================
# ASOSIY FUNKSIYA
# ============================
async def main():
    print("=" * 50)
    print("🤖 HL 309 Hotel Bot ishga tushmoqda...")
    print(f"🔐 Token mavjudligi: {'✅' if API_TOKEN else '❌'}")
    print("=" * 50)

    # images papkasini tekshirish
    if not os.path.exists("images"):
        os.makedirs("images")
        print("📁 'images' papkasi yaratildi")
        print("ℹ️ Rasmlarni 'images' papkasiga joylang")

    # Rasmlarni tekshirish
    image_files = get_image_files()
    total_images = len(image_files)

    print(f"📊 Rasmlar soni: {total_images} ta")

    if total_images > 0:
        print("📁 Topilgan rasmlar:")
        for i, img_path in enumerate(image_files[:5], 1):  # Faqat 5 tasini ko'rsat
            filename = os.path.basename(img_path)
            file_size = os.path.getsize(img_path) / 1024  # KB
            print(f"   {i}. {filename} ({file_size:.0f} KB)")

        if total_images > 5:
            print(f"   ... va yana {total_images - 5} ta rasm")

    print("⚡ TEZLASHTIRILGAN yuklash rejimi")
    print("🌍 5 til qo'llab-quvvatlanadi")
    print("⏱️  Debounce: 1 soniya")
    print("=" * 50)
    print("✅ Bot ishga tushirilmoqda...")

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("\n🛑 Bot to'xtatildi!")
    except Exception as e:
        print(f"❌ Xatolik: {e}")


if __name__ == "__main__":
    asyncio.run(main())