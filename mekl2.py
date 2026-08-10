import tkinter as tk
from tkinter import messagebox, ttk
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
    messagebox.showinfo("ذخیره شد", "مشخصات ملک با موفقیت ذخیره شد.")

# تابع برای نمایش مشخصات تمامی املاک
def show_properties():
    if not os.path.exists(FILE_PATH):
        messagebox.showinfo("اطلاع", "هیچ ملکی ذخیره نشده است.")
        return

    # بارگذاری اطلاعات از فایل
    with open(FILE_PATH, "r") as file:
        all_properties = json.load(file)

    # پاک کردن جدول
    for row in tree.get_children():
        tree.delete(row)

    # اضافه کردن اطلاعات به جدول
    for index, property_data in enumerate(all_properties, start=1):
        tree.insert(
            "", "end",
            values=(
                index,
                property_data["نام مالک"],
                property_data["آدرس"],
                property_data["مساحت (متر مربع)"],
                property_data["تعداد اتاق‌ها"],
                property_data["قیمت (تومان)"]
            )
        )

# تابع برای ذخیره اطلاعات از فرم
def save_from_form():
    property_data = {
        "نام مالک": owner_name_var.get(),
        "آدرس": address_var.get(),
        "مساحت (متر مربع)": area_var.get(),
        "تعداد اتاق‌ها": rooms_var.get(),
        "قیمت (تومان)": price_var.get()
    }
    save_property(property_data)

    # پاک کردن مقادیر فرم
    owner_name_var.set("")
    address_var.set("")
    area_var.set("")
    rooms_var.set("")
    price_var.set("")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("سیستم مدیریت املاک")

# فریم برای فرم ورود اطلاعات
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(side=tk.TOP, fill=tk.X)

tk.Label(form_frame, text="نام مالک:").grid(row=0, column=0, padx=5, pady=5)
owner_name_var = tk.StringVar()
tk.Entry(form_frame, textvariable=owner_name_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="آدرس:").grid(row=1, column=0, padx=5, pady=5)
address_var = tk.StringVar()
tk.Entry(form_frame, textvariable=address_var).grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="مساحت (متر مربع):").grid(row=2, column=0, padx=5, pady=5)
area_var = tk.StringVar()
tk.Entry(form_frame, textvariable=area_var).grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="تعداد اتاق‌ها:").grid(row=3, column=0, padx=5, pady=5)
rooms_var = tk.StringVar()
tk.Entry(form_frame, textvariable=rooms_var).grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="قیمت (تومان):").grid(row=4, column=0, padx=5, pady=5)
price_var = tk.StringVar()
tk.Entry(form_frame, textvariable=price_var).grid(row=4, column=1, padx=5, pady=5)

# دکمه برای ذخیره اطلاعات
tk.Button(form_frame, text="ذخیره ملک", command=save_from_form).grid(row=5, column=0, columnspan=2, pady=10)

# فریم برای نمایش اطلاعات
table_frame = tk.Frame(root, padx=10, pady=10)
table_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

columns = ("شماره", "نام مالک", "آدرس", "مساحت (متر مربع)", "تعداد اتاق‌ها", "قیمت (تومان)")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# دکمه برای نمایش اطلاعات
tk.Button(root, text="نمایش املاک", command=show_properties).pack(side=tk.BOTTOM, pady=5)

# اجرای برنامه
root.mainloop()
