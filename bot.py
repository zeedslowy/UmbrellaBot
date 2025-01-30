import instaloader
import telebot
from telebot import types

# Bot Token'i buraya ekleyin
TOKEN = "{TOKEN}"
bot = telebot.TeleBot(TOKEN)

# Instaloader başlat
loader = instaloader.Instaloader()

# /start komutu
@bot.message_handler(commands=['start'])
def start_message(message):
    # Başlangıç mesajı ve butonlar
    keyboard = types.InlineKeyboardMarkup()

    # Butonlar
    button1 = types.InlineKeyboardButton(text="♂️ SAHİP", url="https://t.me/ViosCeo")
    button2 = types.InlineKeyboardButton(text="🗨️ KANAL", url="https://t.me/ViosTsam")
    button3 = types.InlineKeyboardButton(text="📕 Komutlar", callback_data="help")

    keyboard.add(button1, button2, button3)

    bot.reply_to(
        message,
        "Merhaba! Ben bir görsel işleme botuyum. Bana hayalindeki bir sahneyi tarif et ve sana özel bir görsel göndereyim.\n\n"
        "Aşağıdaki butonları kullanarak daha fazla bilgi alabilirsin:",
        reply_markup=keyboard  # Butonları mesajın altına ekliyoruz
    )

# /help komutu
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_message(call):
    # Yardım mesajı
    help_text = (
        "Komutlar:\n"
        "/rave - Belirtilen kullanıcı adının sosyal medya profillerini analiz eder.\n\n"
        "Sosyal medya platformlarını tek tek sorgularım ve bağlantı butonlarını gönderirim!"
    )

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, help_text)

# /rave komutu
@bot.message_handler(commands=['rave'])
def profile_info(message):
    try:
        # Kullanıcı adını al
        username = message.text.split(maxsplit=1)[1]

        # Sosyal medya platformları ve durumu
        social_media_buttons = []

        # Instagram
        instagram_url = f"https://www.instagram.com/{username}"
        instagram_button = types.InlineKeyboardButton(text="Instagram ✅", url=instagram_url)
        instagram_status = "✅" if check_profile(instagram_url) else "❌"

        # TikTok
        tiktok_url = f"https://www.tiktok.com/@{username}"
        tiktok_button = types.InlineKeyboardButton(text="TikTok ✅", url=tiktok_url)
        tiktok_status = "✅" if check_profile(tiktok_url) else "❌"

        # YouTube
        youtube_url = f"https://www.youtube.com/{username}"
        youtube_button = types.InlineKeyboardButton(text="YouTube ✅", url=youtube_url)
        youtube_status = "✅" if check_profile(youtube_url) else "❌"

        # GitHub
        github_url = f"https://github.com/{username}"
        github_button = types.InlineKeyboardButton(text="GitHub ✅", url=github_url)
        github_status = "✅" if check_profile(github_url) else "❌"

        # Tumblr
        tumblr_url = f"https://{username}.tumblr.com"
        tumblr_button = types.InlineKeyboardButton(text="Tumblr ✅", url=tumblr_url)
        tumblr_status = "✅" if check_profile(tumblr_url) else "❌"

        # Pinterest
        pinterest_url = f"https://www.pinterest.com/{username}"
        pinterest_button = types.InlineKeyboardButton(text="Pinterest ✅", url=pinterest_url)
        pinterest_status = "✅" if check_profile(pinterest_url) else "❌"

        # Twitter
        twitter_url = f"https://twitter.com/{username}"
        twitter_button = types.InlineKeyboardButton(text="Twitter ✅", url=twitter_url)
        twitter_status = "✅" if check_profile(twitter_url) else "❌"

        # Telegram kullanıcı adı
        telegram_username = message.from_user.username
        telegram_info = f"Telegram Kullanıcı Adınız: @{telegram_username}"

        # Platformlara göre ayrı ayrı mesajlar
        if tiktok_status == "✅":
            bot.send_message(message.chat.id, f"TİKTOK\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(tiktok_button))
        else:
            bot.send_message(message.chat.id, f"TİKTOK\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(tiktok_button))

        if instagram_status == "✅":
            bot.send_message(message.chat.id, f"INSTAGRAM\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(instagram_button))
        else:
            bot.send_message(message.chat.id, f"INSTAGRAM\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(instagram_button))

        if youtube_status == "✅":
            bot.send_message(message.chat.id, f"YOUTUBE\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(youtube_button))
        else:
            bot.send_message(message.chat.id, f"YOUTUBE\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(youtube_button))

        if github_status == "✅":
            bot.send_message(message.chat.id, f"GITHUB\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(github_button))
        else:
            bot.send_message(message.chat.id, f"GITHUB\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(github_button))

        if tumblr_status == "✅":
            bot.send_message(message.chat.id, f"TUMBLR\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(tumblr_button))
        else:
            bot.send_message(message.chat.id, f"TUMBLR\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(tumblr_button))

        if pinterest_status == "✅":
            bot.send_message(message.chat.id, f"PINTEREST\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(pinterest_button))
        else:
            bot.send_message(message.chat.id, f"PINTEREST\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(pinterest_button))

        if twitter_status == "✅":
            bot.send_message(message.chat.id, f"TWITTER\n\n[BAŞARILI ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(twitter_button))
        else:
            bot.send_message(message.chat.id, f"TWITTER\n\n[TARAMA ✅]\n\n- Butonlu bağlantı", reply_markup=types.InlineKeyboardMarkup().add(twitter_button))

        # Telegram kullanıcı adını göster
        bot.send_message(message.chat.id, f"{telegram_info}")

    except Exception as e:
        bot.reply_to(message, "[KULLANIM ✅]\n\n/rave [KULLANICI ADI]")

# /id komutu
@bot.message_handler(commands=['id'])
def send_id(message):
    # Telegram Kullanıcı Adı
    telegram_username = message.from_user.username
    bot.reply_to(message, f"Telegram Kullanıcı Adınız: @{telegram_username}")

# Profilin varlığını kontrol etmek için fonksiyon
def check_profile(url):
    try:
        # Burada profile erişim kontrolü yapılabilir. 
        # Hızlı bir kontrol için URL'yi açıp başarılı olup olmadığını kontrol edebilirsiniz.
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

# Botu başlat
print("Bot çalışıyor...")
bot.polling(none_stop=True, interval=0, timeout=60)
