import pyttsx3  # کتابخانه تبدیل متن به گفتار

text = input("چه چیزی می‌خواهید بگویید؟ ")  # گرفتن متن از کاربر
engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار
engine.say(text)  # تنظیم پیام گفتاری
engine.runAndWait()  # اجرای پیام گفتاری
