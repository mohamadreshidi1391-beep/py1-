#محاسبه حق کمیسیون مشاوران املاک برای خرید و فروش ملک
# ورودی کاربر
property_value = float(input("ارزش ملک (تومان): "))

# Constants
commission_rate = 0.0025  # نرخ کمیسیون
tax_rate = 0.09  # نرخ مالیات بر ارزش افزوده

# محاسبه حق کمیسیون
commission = property_value * commission_rate
tax = commission * tax_rate
total_commission = commission + tax

print(f"حق کمیسیون: {commission} تومان")
print(f"مالیات: {tax} تومان")
print(f"جمع حق کمیسیون و مالیات: {total_commission} تومان")
