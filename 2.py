#۲. محاسبه حق کمیسیون برای اجاره ملک
# ورودی کاربر
monthly_rent = float(input("مبلغ اجاره ماهیانه (تومان): "))

# Constants
commission_rate = 0.25  # نرخ کمیسیون
tax_rate = 0.09  # نرخ مالیات بر ارزش افزوده

# محاسبه حق کمیسیون
commission = monthly_rent * commission_rate
tax = commission * tax_rate
total_commission = commission + tax

print(f"حق کمیسیون: {commission} تومان")
print(f"مالیات: {tax} تومان")
print(f"جمع حق کمیسیون و مالیات: {total_commission} تومان")
