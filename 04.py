import pyttsx3  # کتابخانه تبدیل متن به گفتار

engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار
for i in range(3):  # حلقه for برای سه بار گفتن
    engine.say("Hello!")  # تنظیم پیام گفتاری
engine.runAndWait()  # اجرای پیام گفتاری
