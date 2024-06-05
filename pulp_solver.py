import pulp
import pandas as pd
import numpy as np

revenue_df = pd.read_excel('results/base/revenue_enver.xlsx')
cost_df = pd.read_excel('results/base/cost_enver.xlsx')

real_total_revenue = 29299749.30999999
real_total_cost = 7824792.109999999

# Function to run the optimization model with a given budget constraint
def run_model(budget_constraint):
    output_df = pd.DataFrame(columns=["Item", "Discount Rate", "Expected Revenue", "Cost", "Real Discount Rate", "Real Revenue", "Real Cost"])
    
    # Fill the first column with item numbers (1 to 12)
    output_df["Item"] = range(1, 13)
    
    # Fill the last 3 columns with the output from model 1 (discount rate, expected revenue, and cost)
    output_df["Real Discount Rate"] = [0.08, 0.09, 0.08, 0.06, 0.08, 0.12, 0.12, 0.18, 0.15, 0.12, 0.14, 0.12]
    output_df["Real Revenue"] = [4866527.739999999, 11056153.950000001, 1594367.9100000001, 133687.80999999997, 4371370.259999997, 170544.28999999998, 286772.5, 564489.2899999999, 452823.0199999997, 672728.4299999997, 4524994.459999998, 605289.6500000001]
    output_df["Real Cost"] = [808387.4400000003, 2158638.8600000013, 345253.7599999999, 32528.340000000004, 992592.7399999996, 61003.64, 65632.15999999999, 417442.50000000006, 253977.76000000013, 320547.72000000015, 1885953.8499999999, 482833.34]
    
    # Number of items
    num_items = 12
    
    # List of discount rates (example: [0.00, 0.02, 0.04, ..., 0.20])
    discount_rates = np.arange(0.00, 1, 0.02).tolist() + [0.15, 0.09]
    discount_rates.sort()
    discount_rates = [round(i, 2) for i in discount_rates]
    
    # Create the problem variable to maximize total revenue
    model = pulp.LpProblem("Maximize_Revenue", pulp.LpMaximize)
    
    # Decision Variables
    choices = pulp.LpVariable.dicts("Choice", 
                                    ((i, dr) for i in range(num_items) for dr in discount_rates),
                                    cat='Binary')
    
    # Objective Function: Maximize Total Revenue
    model += pulp.lpSum(choices[i, dr] * revenue_df.loc[i, str(dr)] for i in range(num_items) for dr in discount_rates)
    
    # Constraints
    # Only one discount rate per item
    for i in range(num_items):
        model += pulp.lpSum(choices[i, dr] for dr in discount_rates) == 1, f"One_rate_per_item_{i}"
    
    # Total cost must not exceed the budget constraint
    # model += pulp.lpSum(choices[i, dr] * cost_df.loc[i, str(dr)] for i in range(num_items) for dr in discount_rates) <= budget_constraint, "Budget_Constraint"
    
    # Solve the problem
    model.solve()
    
    # Print the selected discount rates for each item if the solution is optimal
    if model.status == pulp.LpStatusOptimal:
        for i in range(num_items):
            for dr in discount_rates:
                if choices[(i, dr)].varValue == 1:
                    print(f"Item {i+1} should use discount rate {dr} with expected revenue {revenue_df.loc[i, str(dr)]} and cost {cost_df.loc[i, str(dr)]}")
                    output_df.loc[i, "Discount Rate"] = dr
                    output_df.loc[i, "Expected Revenue"] = revenue_df.loc[i, str(dr)]
                    output_df.loc[i, "Cost"] = cost_df.loc[i, str(dr)]
    else:
        print("No optimal solution found")
    
    # Append the totals row
    totals = {
        "Item": "Total",
        "Discount Rate": "",
        "Expected Revenue": output_df["Expected Revenue"].sum(),
        "Cost": output_df["Cost"].sum(),
        "Real Discount Rate": "",
        "Real Revenue": real_total_revenue,
        "Real Cost": real_total_cost
    }
    output_df = output_df.append(totals, ignore_index=True)
    
    return output_df

# Run the model with different budget constraints and save the results in an Excel file
budget_factors = [0.5, 1, 1.5, 2]  # Example factors to multiply with the default budget constraint
default_budget_constraint = 7824792.109999999

with pd.ExcelWriter("results/output_comparison.xlsx") as writer:
    for factor in budget_factors:
        budget_constraint = factor * default_budget_constraint
        result_df = run_model(budget_constraint)
        result_df.to_excel(writer, sheet_name=f"Budget_{factor}", index=False)
