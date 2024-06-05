import pandas as pd


revenues = []
costs =[]

for i in range(0, 12):
    data = pd.read_excel('final_groups_data.xlsx', sheet_name=i)
    cost = sum(data["scaled_original_unit_price"] * data["total_quantity"] * data["direct_discount_percentage"])
    costs.append(cost)
    revenue = sum(data["scaled_final_unit_price"] * data["total_quantity"])
    revenues.append(revenue)


print("Total Revenue: ", sum(revenues))
print("Total Cost: ", sum(costs))
print("Costs: ", costs)
print("Revenues: ", revenues)

