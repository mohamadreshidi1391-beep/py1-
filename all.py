import tkinter as tk

def calculate_commission_sale():
    property_value = float(entry_property_value.get())
    commission_rate = 0.0025
    tax_rate = 0.09
    commission = property_value * commission_rate
    tax = commission * tax_rate
    total_commission = commission + tax
    label_result_sale.config(text=f"جمع حق کمیسیون و مالیات: {total_commission} تومان")

def calculate_commission_rent():
    monthly_rent = float(entry_monthly_rent.get())
    commission_rate = 0.25
    tax_rate = 0.09
    commission = monthly_rent * commission_rate
    tax = commission * tax_rate
    total_commission = commission + tax
    label_result_rent.config(text=f"جمع حق کمیسیون و مالیات: {total_commission} تومان")

def calculate_commission_deposit():
    deposit_amount = float(entry_deposit_amount.get())
    conversion_rate = 30
    commission_rate = 0.25
    tax_rate = 0.09
    monthly_rent_equivalent = deposit_amount * conversion_rate
    commission = monthly_rent_equivalent * commission_rate
    tax = commission * tax_rate
    total_commission = commission + tax
    label_result_deposit.config(text=f"جمع حق کمیسیون و مالیات: {total_commission} تومان")

root = tk.Tk()
root.title("محاسبه حق کمیسیون مشاوران املاک")

frame_sale = tk.Frame(root)
frame_sale.pack(pady=10)
label_property_value = tk.Label(frame_sale, text="ارزش ملک (تومان):")
label_property_value.pack(side=tk.LEFT)
entry_property_value = tk.Entry(frame_sale)
entry_property_value.pack(side=tk.LEFT)
button_calculate_sale = tk.Button(frame_sale, text="محاسبه", command=calculate_commission_sale)
button_calculate_sale.pack(side=tk.LEFT)
label_result_sale = tk.Label(frame_sale, text="")
label_result_sale.pack(side=tk.LEFT)

frame_rent = tk.Frame(root)
frame_rent.pack(pady=10)
label_monthly_rent = tk.Label(frame_rent, text="مبلغ اجاره ماهیانه (تومان):")
label_monthly_rent.pack(side=tk.LEFT)
entry_monthly_rent = tk.Entry(frame_rent)
entry_monthly_rent.pack(side=tk.LEFT)
button_calculate_rent = tk.Button(frame_rent, text="محاسبه", command=calculate_commission_rent)
button_calculate_rent.pack(side=tk.LEFT)
label_result_rent = tk.Label(frame_rent, text="")
label_result_rent.pack(side=tk.LEFT)

frame_deposit = tk.Frame(root)
frame_deposit.pack(pady=10)
label_deposit_amount = tk.Label(frame_deposit, text="مبلغ رهن (تومان):")
label_deposit_amount.pack(side=tk.LEFT)
entry_deposit_amount = tk.Entry(frame_deposit)
entry_deposit_amount.pack(side=tk.LEFT)
button_calculate_deposit = tk.Button(frame_deposit, text="محاسبه", command=calculate_commission_deposit)
button_calculate_deposit.pack(side=tk.LEFT)
label_result_deposit = tk.Label(frame_deposit, text="")
label_result_deposit.pack(side=tk.LEFT)

root.mainloop()
