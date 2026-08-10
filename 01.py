import pyttsx3  # کتابخانه تبدیل متن به گفتار

engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار
a=input("Please enter: ")
engine.say(a)  # تنظیم پیام گفتاری
engine.runAndWait()  # اجرای پیام گفتاری
