import telebot,datetime,requests
bot_token = '6074793820:AAF_SMWYg5GI1vnHU6O__DJsPhUPP89RTEA' 
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['code'])
def lqm_sms(message):
    uid = message.text.split()[1]
    print(uid)
    code=[
    'KGCPlayLive4',
    'KingGodCartoon22',
    'KGCLiveCollab2023',
    'JoinNowKgcGlobal',
    'KingGodGift23']
    for codes in code:
        data = {
            'uid': uid,
            'code': codes,
            'lang': 'en',
        }
        response = requests.post('https://kgc-coupon.awesomepiece.com/submitCoupon', data=data).text
        if 'Rewards have been sent to your inbox. Please log in to check.' in response:
            print('code nhập thành công',codes)
        elif 'This Player-ID does not exist. Please check and try again.' in response:
            print('Userid không hợp lệ',codes)
        elif 'This coupon number is invalid or has already been used.' in response:
            print('Code hết hạn hoặc đã sử dụng',codes)
        else:
            print('Lỗi không xác định',codes)

    bot.reply_to(message, f'🚀 Nhập code Thành Công 🚀 \n: [ {uid} ]')

@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''
🚀Danh sách lệnh:🚀
- /code {userid}
'''
    bot.reply_to(message, help_text)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, '🚀 Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh. 🚀')

bot.infinity_polling()



