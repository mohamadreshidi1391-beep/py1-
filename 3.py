#۳. محاسبه حق کمیسیون برای رهن ملک
# ورودی کاربر
deposit_amount = float(input("مبلغ رهن (تومان): "))

# Constants
conversion_rate = 30  # نرخ تبدیل رهن به اجاره
commission_rate = 0.25  # نرخ کمیسیون
tax_rate = 0.09  # نرخ مالیات بر ارزش افزوده

# تبدیل رهن به اجاره
monthly_rent_equivalent = deposit_amount * conversion_rate

# محاسبه حق کمیسیون
commission = monthly_rent_equivalent * commission_rate
tax = commission * tax_rate
total_commission = commission + tax

print(f"حق کمیسیون: {commission} تومان")
print(f"مالیات: {tax} تومان")
print(f"جمع حق کمیسیون و مالیات: {total_commission} تومان")
