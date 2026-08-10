import pyttsx3  # کتابخانه تبدیل متن به گفتار

def speak(text):  # تعریف تابع برای گفتار
    engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار
    engine.say(text)  # تنظیم پیام گفتاری
    engine.runAndWait()  # اجرای پیام گفتاری

text = input("چه چیزی می‌خواهید بگویید؟ ")  # گرفتن متن از کاربر
speak(text)  # فراخوانی تابع
