import pyttsx3  # کتابخانه تبدیل متن به گفتار

engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار
i = 0  # مقداردهی متغیر شمارنده
while i < 3:  # حلقه while تا زمانی که شرط برقرار است
    engine.say("Hello!")  # تنظیم پیام گفتاری
    i += 1  # افزایش شمارنده
engine.runAndWait()  # اجرای پیام گفتاری
