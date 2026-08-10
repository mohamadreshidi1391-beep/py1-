# تعریف یک مجموعه
unique_numbers = {1, 2, 3, 2, 4, 5, 1}
print(f"مجموعه اعداد یکتا: {unique_numbers}") # تکرارها به صورت خودکار حذف می‌شوند

# اضافه کردن عنصر
unique_numbers.add(6)
print(f"بعد از اضافه کردن ۶: {unique_numbers}")

# عملیات مجموعه‌ها
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"اجتماع: {set_a.union(set_b)}")
print(f"اشتراک: {set_a.intersection(set_b)}")
print(f"تفاضل (A-B): {set_a.difference(set_b)}")