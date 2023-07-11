import pandas as pd
import matplotlib.pyplot as plt


# Read the payment data from a CSV file
data = pd.read_csv('payment_data.csv')

# Pie chart: Percentage of transactions with has_cbk = True
has_cbk_counts = data['has_cbk'].value_counts()
labels = ['No Chargeback', 'Chargeback']
plt.pie(has_cbk_counts, labels=labels, autopct='%1.1f%%')
plt.title('Percentage of Transactions with Chargebacks')
plt.show()

# Bar chart: Transaction amount range with the highest chargebacks
chargeback_amount_ranges = pd.cut(data[data['has_cbk'] == True]['transaction_amount'],
                                 bins=range(0, 1000, 200), include_lowest=True)
chargeback_amount_ranges_counts = chargeback_amount_ranges.value_counts().sort_index()
x_labels = [f'{x}-{x+200}' for x in range(0, 1000, 200)]
plt.bar(x_labels, chargeback_amount_ranges_counts)
plt.xlabel('Transaction Amount Range')
plt.ylabel('Number of Chargebacks')
plt.title('Chargebacks by Transaction Amount Range')
plt.show()

# Top 30 CC numbers used for chargebacks
top_30_cc_numbers = data[data['has_cbk'] == True]['card_number'].value_counts().head(30)
top_30_cc_numbers.plot(kind='bar')
plt.xlabel('Credit Card Number')
plt.ylabel('Number of Chargebacks')
plt.title('Top 30 Credit Card Numbers for Chargebacks')
plt.show()
