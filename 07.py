import pyttsx3  # کتابخانه تبدیل متن به گفتار

class Speaker:  # تعریف کلاس
    def __init__(self):  # متد سازنده
        self.engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار

    def speak(self, text):  # متد گفتار
        self.engine.say(text)  # تنظیم پیام گفتاری
        self.engine.runAndWait()  # اجرای پیام گفتاری

text = input("چه چیزی می‌خواهید بگویید؟ ")  # گرفتن متن از کاربر
speaker = Speaker()  # ایجاد شیء از کلاس
speaker.speak(text)  # فراخوانی متد کلاس
