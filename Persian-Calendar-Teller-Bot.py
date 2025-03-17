import telepot
from datetime import datetime, timedelta
import jdatetime

TOKEN = ''
CHANNEL_ID = ''

bot = telepot.Bot(TOKEN)

# Convert weekday names to Persian
def get_jalali_weekday(weekday):
    weekdays = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]
    return weekdays[weekday]

# Convert Jalali month names to Persian
def get_jalali_month(month):
    months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    return months[month - 1]

# Convert numbers to Persian
def to_farsi_number(num):
    farsi_numbers = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
    return ''.join(farsi_numbers.get(i, i) for i in str(num))

# Common function to get Jalali and Gregorian dates
def get_jalali_and_gregorian_dates():
    jalali_now = jdatetime.datetime.now()
    jalali_weekday = get_jalali_weekday(jalali_now.weekday())  # Jalali weekday
    jalali_date = to_farsi_number(jalali_now.day)  # Jalali day
    jalali_month = get_jalali_month(jalali_now.month)  # Jalali month

    # Calculate tomorrow's date
    jalali_tomorrow = jalali_now + timedelta(days=1)
    jalali_tomorrow_weekday = get_jalali_weekday(jalali_tomorrow.weekday())
    jalali_tomorrow_date = to_farsi_number(jalali_tomorrow.day)
    jalali_tomorrow_month = get_jalali_month(jalali_tomorrow.month)
    
    # Today's Gregorian date
    gregorian_now = datetime.now()
    gregorian_day = gregorian_now.strftime('%A')  # Gregorian weekday
    gregorian_date = gregorian_now.strftime('%b %d, %Y')  # Gregorian date
    
    return jalali_weekday, jalali_date, jalali_month, jalali_tomorrow_weekday, jalali_tomorrow_date, jalali_tomorrow_month, gregorian_day, gregorian_date

# Check if the bot is an admin in the specified chat
def is_admin(chat_id):
    admins = bot.getChatAdministrators(chat_id)
    for admin in admins:
        if admin['user']['id'] == bot.getMe()['id']:
            return True
    return False

# Send Jalali and Gregorian dates to the channel
def send_jalali_time():
    if is_admin(CHANNEL_ID):
        jalali_weekday, jalali_date, jalali_month, jalali_tomorrow_weekday, jalali_tomorrow_date, jalali_tomorrow_month, gregorian_day, gregorian_date = get_jalali_and_gregorian_dates()
        
        message = f"امروز {jalali_weekday} {jalali_date} {jalali_month} است.\nفردا {jalali_tomorrow_weekday} {jalali_tomorrow_date} {jalali_tomorrow_month} است.\n\n{gregorian_day}, {gregorian_date}\n\n📅"
        bot.sendMessage(CHANNEL_ID, message)

# Send the date
send_jalali_time()
