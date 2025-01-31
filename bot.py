import instaloader
import requests
import telebot
from telebot import types

# Bot Token'inizi buraya ekleyin
TOKEN = "{TOKEN}"
bot = telebot.TeleBot(TOKEN)

# Instaloader başlat
loader = instaloader.Instaloader()

# /start komutu
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()

    # Butonlar
    button1 = types.InlineKeyboardButton(text="♂️ SAHİP", url="https://t.me/ViosCeo")
    button2 = types.InlineKeyboardButton(text="🗨️ KANAL", url="https://t.me/ViosTsam")
    button3 = types.InlineKeyboardButton(text="📕 Komutlar", callback_data="help")

    keyboard.add(button1, button2, button3)

    bot.reply_to(
        message,
        "Merhaba! Ben bir sosyal medya analiz botuyum. Bana kullanıcı adını ver, detayları getiriyim!\n\n"
        "Aşağıdaki butonları kullanarak daha fazla bilgi alabilirsin:",
        reply_markup=keyboard
    )

# /help komutu
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_message(call):
    help_text = (
        "Komutlar:\n"
        "/rave <kullanıcı_adı> - Sosyal medya profillerini analiz eder.\n\n"
        "Desteklenen platformlar: Instagram, GitHub, TikTok, Twitter, YouTube, Tumblr, Pinterest"
    )
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, help_text)

# /rave komutu - PROFİL ANALİZİ
@bot.message_handler(commands=['rave'])
def profile_info(message):
    try:
        # Kullanıcı adını al
        username = message.text.split(maxsplit=1)[1]

        ## ✅ INSTAGRAM PROFİL BİLGİLERİ
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
            instagram_bio = profile.biography
            followers = profile.followers
            following = profile.followees
            profile_pic_url = profile.profile_pic_url

            caption = f"📸 Instagram Profil Bilgileri\n\n"
            caption += f"👤 Kullanıcı Adı: {username}\n"
            caption += f"📌 Bio: {instagram_bio}\n"
            caption += f"👥 Takipçi: {followers}\n"
            caption += f"🔄 Takip Edilen: {following}\n"

            instagram_url = f"https://www.instagram.com/{username}"
            instagram_button = types.InlineKeyboardMarkup()
            instagram_button.add(types.InlineKeyboardButton(text="📷 Instagram Profiline Git", url=instagram_url))

            bot.send_photo(message.chat.id, profile_pic_url, caption, reply_markup=instagram_button)
        except:
            bot.send_message(message.chat.id, "❌ Instagram hesabı bulunamadı.")

        ## ✅ GITHUB PROFİL BİLGİLERİ
        github_url = f"https://api.github.com/users/{username}"
        response = requests.get(github_url)
        if response.status_code == 200:
            github_data = response.json()
            github_name = github_data.get("name", "Bilinmiyor")
            github_bio = github_data.get("bio", "Biyografi yok")
            github_repos = github_data.get("public_repos", 0)
            github_followers = github_data.get("followers", 0)
            github_following = github_data.get("following", 0)
            github_profile_pic = github_data.get("avatar_url")

            caption = f"🐙 GitHub Profil Bilgileri\n\n"
            caption += f"👤 İsim: {github_name}\n"
            caption += f"📌 Bio: {github_bio}\n"
            caption += f"📁 Depolar: {github_repos}\n"
            caption += f"👥 Takipçi: {github_followers}\n"
            caption += f"🔄 Takip Edilen: {github_following}\n"

            github_button = types.InlineKeyboardMarkup()
            github_button.add(types.InlineKeyboardButton(text="🐙 GitHub Profiline Git", url=f"https://github.com/{username}"))

            bot.send_photo(message.chat.id, github_profile_pic, caption, reply_markup=github_button)
        else:
            bot.send_message(message.chat.id, "❌ GitHub hesabı bulunamadı.")

        ## ✅ DİĞER PLATFORM BUTONLARI
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="🎵 TikTok", url=f"https://www.tiktok.com/@{username}"))
        keyboard.add(types.InlineKeyboardButton(text="📺 YouTube", url=f"https://www.youtube.com/{username}"))
        keyboard.add(types.InlineKeyboardButton(text="🐦 Twitter", url=f"https://twitter.com/{username}"))
        keyboard.add(types.InlineKeyboardButton(text="📌 Pinterest", url=f"https://www.pinterest.com/{username}"))
        keyboard.add(types.InlineKeyboardButton(text="🎨 Tumblr", url=f"https://{username}.tumblr.com"))

        bot.send_message(message.chat.id, "🔗 **Diğer Platformlar İçin:**", reply_markup=keyboard)

    except Exception as e:
        bot.reply_to(message, "⚠ Kullanım: /rave [Kullanıcı Adı]")

# Botu başlat
print("Bot çalışıyor...")
bot.polling(none_stop=True, interval=0, timeout=60)
