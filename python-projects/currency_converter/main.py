from datetime import date
import currency_converter

c = currency_converter.CurrencyConverter()

amount = float(input("Enter the amount: "))
source_cur = input("Source currency (ZAR/USD/EUR/CAD): ").strip().upper()
target_cur = input("Target currency (ZAR/USD/EUR/CAD): ").strip().upper()

conv = c.convert(amount, source_cur, target_cur)

print(f"{amount:.2f} {source_cur} is equal to {conv:.2f} {target_cur}")

# print(c.convert(1, "SAR", "USD", date = date(2025, 3, 20)))