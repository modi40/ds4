import matplotlib.pyplot as plt

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"]
customers = [150, 80, 60, 40, 30]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(8, 6))
plt.pie(customers, labels=payment_methods, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Preferred Payment Methods Among Customers")
plt.tight_layout()
plt.show()
