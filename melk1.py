import json
import os

# مسیر فایل برای ذخیره اطلاعات
FILE_PATH = "properties.json"

# تابع برای ذخیره مشخصات ملک
def save_property(property_data):
    if os.path.exists(FILE_PATH):
        # اگر فایل وجود داشته باشد، اطلاعات قبلی را بارگذاری می‌کنیم
        with open(FILE_PATH, "r") as file:
            all_properties = json.load(file)
    else:
        # اگر فایل وجود نداشته باشد، یک لیست جدید ایجاد می‌کنیم
        all_properties = []
    
    # افزودن ملک جدید به لیست
    all_properties.append(property_data)
    
    # ذخیره اطلاعات در فایل
    with open(FILE_PATH, "w") as file:
        json.dump(all_properties, file, indent=4)
    print("مشخصات ملک ذخیره شد.")

# تابع برای نمایش مشخصات تمامی املاک
def print_properties():
    if not os.path.exists(FILE_PATH):
        print("هیچ ملکی ذخیره نشده است.")
        return
    
    # بارگذاری اطلاعات از فایل
    with open(FILE_PATH, "r") as file:
        all_properties = json.load(file)
    
    # نمایش اطلاعات هر ملک
    for index, property_data in enumerate(all_properties, start=1):
        print(f"\nملک شماره {index}:")
        for key, value in property_data.items():
            print(f"{key}: {value}")

# تابع اصلی برنامه
def main():
    while True:
        print("\n==== سیستم مدیریت املاک ====")
        print("1. افزودن ملک جدید")
        print("2. نمایش مشخصات املاک")
        print("3. خروج")
        
        choice = input("انتخاب کنید: ")
        
        if choice == "1":
            # دریافت اطلاعات ملک از کاربر
            property_data = {
                "نام مالک": input("نام مالک: "),
                "آدرس": input("آدرس ملک: "),
                "مساحت (متر مربع)": float(input("مساحت (متر مربع): ")),
                "تعداد اتاق‌ها": int(input("تعداد اتاق‌ها: ")),
                "قیمت (تومان)": float(input("قیمت (تومان): "))
            }
            # ذخیره ملک
            save_property(property_data)
        
        elif choice == "2":
            # نمایش مشخصات املاک
            print_properties()
        
        elif choice == "3":
            print("خروج از برنامه.")
            break
        
        else:
            print("انتخاب نامعتبر! لطفاً دوباره امتحان کنید.")

# اجرای برنامه
if __name__ == "__main__":
    main()
