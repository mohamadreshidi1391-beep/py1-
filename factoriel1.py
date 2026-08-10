def factorial(n):
  """این تابع فاکتوریل یک عدد را محاسبه می‌کند."""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

result = factorial(5)
print("فاکتوریل 5 برابر است با:", result)
