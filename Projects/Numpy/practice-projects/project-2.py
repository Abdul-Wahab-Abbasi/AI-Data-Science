import numpy as np
months = np.array(["Jan","Feb","Mar","Apr","May","Jun",
                   "Jul","Aug","Sep","Oct","Nov","Dec"])
sales = np.array([4200, 3800, 5100, 4700, 6200, 5800,
                  7100, 6900, 5400, 4900, 8200, 9100])

# sales = np.random.randint(1000, 9000, size=12) # for random sales

# *** Tasks ***
# 1. Total sales, average sales, best month and worst month (print month NAME)
print("\n Task 1")
total_sales = np.sum(sales)
average_sales = np.mean(sales)
print(f"Total sales: {total_sales}")
print(f"Average sales: {average_sales}")
best_month = np.argmax(sales)
worst_month = np.argmin(sales)
print(f"Best Month: {months[best_month]} | Worst Month: {months[worst_month]}")

# 2. Reshape the 12 months into 4 quarters (4 rows x 3 months)
print("\n Task 2")
months_quarter = np.reshape(months,(4,3))
print(f"Months reshaped into 4 quarters (4x3) {months_quarter}")

# 3. Total sales of each quarter — which quarter was best?
print("\n Task 3")
sales_quarter = np.reshape(sales, (4,3))
quarter_sales = np.sum(sales_quarter,axis=1)
for q_sales, q_months in zip(quarter_sales,months_quarter):
    print(f"Total Sale of quarter {q_months} is {q_sales}")
print(f"Best quarter is {months_quarter[np.argmax(quarter_sales)]} with total sales of {np.max(quarter_sales)}")

# 4. Month-over-month growth (how much sales went up/down each month)
print("\n Task 4")
growth = np.diff(sales)
for month, diff in zip(months[1:], growth):
    print(f"In {month} the sales went {"Up" if diff > 0 else "Down"} by {diff}")

# 5. Running total of sales through the year
print("\n Task 5")
running_sales =  np.cumsum(sales)
for month, r_sale in zip(months, running_sales):
    print(f"By end of {month}, total sales so far: {r_sale}")

# 6. Which months performed ABOVE the yearly average?
print("\n Task 6")
sales_above_average = np.where(sales > average_sales)
print(f"These months performed ABOVE the yearly average: {months[sales_above_average]}")

# 7. Each month's contribution as a percentage of total sales
print("\n Task 7")
contributions = np.round((sales / total_sales * 100),2)
print("Each month's contribution as a percentage of total sales")
for month, contribution in zip(months, contributions):
    print(f"{month}: {contribution}%")

# 8. Split the year into 2 halves and compare their totals
print("\n Task 8")
year_halves = np.array_split(sales,2)
year_halves_sums = np.sum(year_halves,axis=1)
print(f"The first half of the year has {"Greater" if year_halves_sums[0] > year_halves_sums[1] else "Less"} Sales '{year_halves_sums[0]}' than the second half sales '{year_halves_sums[1]}'.")