import pandas as pd
import numpy as np

group_1A = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_1A')
group_1B = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_1B')
group_2A1 = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2A1')
group_2A2A = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2A2A')
group_2A2B = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2A2B')
group_2B1A1 = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B1A1')
group_2B1A2A = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B1A2A')
group_2B1A2B = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B1A2B')
group_2B1B1 = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B1B1')
group_2B1B2 = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B1B2')
group_2B2A = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B2A')
group_2B2B = pd.read_excel('final_groups_data.xlsx', sheet_name='final_group_2B2B')

groups = [group_1A, group_1B, group_2A1, group_2A2A, group_2A2B, group_2B1A1, group_2B1A2A, group_2B1A2B, group_2B1B1, group_2B1B2, group_2B2A, group_2B2B]

def generate_synthetic_data(n, intercept, slope, sd_residual, min_res, median_res, max_res, mean_x):
    # Generate random direct_discount_percentage
    direct_discount_percentage = np.full(n, mean_x)

    # Calculate predicted total_quantity
    predicted_total_quantity = intercept + slope * direct_discount_percentage

    # Generate residuals using normal distribution centered around median to simulate skew
    residuals = np.random.normal(loc=median_res, scale=sd_residual, size=n)

    # Adjust residuals to avoid exceeding known min and max (simple clipping method)
    residuals = np.clip(residuals, min_res, max_res)

    # Generate synthetic total_quantity by adding adjusted residuals
    synthetic_total_quantity = predicted_total_quantity + residuals

    return synthetic_total_quantity


def generate_data(mean_x, n=1000, params={}):
    return generate_synthetic_data(n,
                                   intercept=params['intercept'],
                                   slope=params['slope'],
                                   sd_residual=params['sd_residual'],
                                   min_res=params['min_res'],
                                   median_res=params['median_res'],
                                   max_res=params['max_res'],
                                   mean_x=mean_x)

# Example function calls
generate_data_3_params = {
    'intercept': 703.4, 'slope': 224.3, 'sd_residual': 780.3,
    'min_res': -711.5, 'median_res': -310.9, 'max_res': 1967.3, 'mean_x': 0.08
}

generate_data_4_params = {
    'intercept': 247.60, 'slope': 1076.37, 'sd_residual': 523.4,
    'min_res': -686.97, 'median_res': -167.78, 'max_res': 2490.84, 'mean_x': 0.09
}

generate_data_7_params = {
    'intercept': 18.941, 'slope': 62.723, 'sd_residual': 131.3,
    'min_res': -63.82, 'median_res': -16.94, 'max_res': 2836.06, 'mean_x': 0.08
}

generate_data_9_params = {
    'intercept': 5.611, 'slope': 38.212, 'sd_residual': 18.51,
    'min_res': -29.877, 'median_res': -3.611, 'max_res': 208.561, 'mean_x': 0.06
}

generate_data_10_params = {
    'intercept': 52.392, 'slope': 172.508, 'sd_residual': 234.8,
    'min_res': -180.34, 'median_res': -49.39, 'max_res': 2679.39, 'mean_x': 0.08
}

generate_data_14_params = {
    'intercept': 2.2508, 'slope': 9.7997, 'sd_residual': 8.572,
    'min_res': -10.220, 'median_res': -1.251, 'max_res': 135.513, 'mean_x': 0.12
}

generate_data_16_params = {
    'intercept': 5.120, 'slope': 16.760, 'sd_residual': 18.5,
    'min_res': -15.013, 'median_res': -3.120, 'max_res': 268.404, 'mean_x': 0.12
}

generate_data_17_params = {
    'intercept': 5.662, 'slope': 100.216, 'sd_residual': 62.73,
    'min_res': -77.51, 'median_res': -4.66, 'max_res': 523.64, 'mean_x': 0.18
}

generate_data_19_params = {
    'intercept': 30.57, 'slope': 263.19, 'sd_residual': 240.9,
    'min_res': -177.41, 'median_res': -27.57, 'max_res': 1667.78, 'mean_x': 0.15
}

generate_data_20_params = {
    'intercept': 5.792, 'slope': 80.044, 'sd_residual': 74.88,
    'min_res': -63.34, 'median_res': -4.79, 'max_res': 939.32, 'mean_x': 0.12
}

generate_data_22_params = {
    'intercept': 20.361, 'slope': 68.033, 'sd_residual': 112.3,
    'min_res': -77.50, 'median_res': -19.36, 'max_res': 1351.87, 'mean_x': 0.14
}

generate_data_23_params = {
    'intercept': 1.509, 'slope': 233.525, 'sd_residual': 130.4,
    'min_res': -195.94, 'median_res': -0.51, 'max_res': 929.52, 'mean_x': 0.12
}

generated_data_list = [generate_data_3_params, generate_data_4_params, generate_data_7_params, generate_data_9_params, generate_data_10_params, generate_data_14_params, generate_data_16_params, generate_data_17_params, generate_data_19_params, generate_data_20_params, generate_data_22_params, generate_data_23_params]
repeatation_list = [10000, 10000, 1000, 1000, 5000, 1000, 1000, 1000, 3000, 1000, 2000, 1000]
#generate a list above with amount/10
#repeatation_list = [i//10 for i in repeatation_list]
mean_x = np.arange(0, 1, 0.02).tolist() + [0.15, 0.09]
# round the mean_x to 2 decimal places
mean_x.sort()
mean_x = [round(i, 2) for i in mean_x]

df_revs = pd.DataFrame()
df_costs = pd.DataFrame()
df = pd.DataFrame()

for idx in range(12):
    print(idx)
    for disc_rate in mean_x:
        revs = []
        costs = []
        for _ in range(repeatation_list[idx]):
            generated_quantity_list = np.array(generate_data(mean_x=disc_rate, n=len(groups[idx]), params=generated_data_list[idx]))

            # replace the negative generated_quantity_list with 0
            if (idx < 2):
                # delete the generated_quantity_list elements that are negative
                generated_quantity_list = generated_quantity_list[generated_quantity_list >= 0]
                mean_quantity = np.mean(generated_quantity_list)
                total_rev = np.sum(mean_quantity * groups[idx]['scaled_original_unit_price'] * (1-disc_rate))
                total_cost = np.sum(mean_quantity * groups[idx]['scaled_original_unit_price'] * (disc_rate))

            # calculate total revenue
            else:
                total_rev = np.sum(np.array(generated_quantity_list) * groups[idx]['scaled_original_unit_price'] * (1-disc_rate))
                total_cost = np.sum(np.array(generated_quantity_list) * groups[idx]['scaled_original_unit_price'] * (disc_rate))
            revs.append(total_rev)
            costs.append(total_cost)

        df.loc[disc_rate, 'mean_revenue ' + str(idx)] = np.mean(revs)
        df.loc[disc_rate, 'mean_cost  ' + str(idx)] = np.std(costs)

        df_revs.loc[str(idx), str(disc_rate)] = np.mean(revs)
        df_costs.loc[str(idx), str(disc_rate)] = np.mean(costs)


df.to_excel('results/mixed_enver.xlsx', sheet_name='mixed')
df_revs.to_excel('results/revenue_enver.xlsx', sheet_name='revenue')
df_costs.to_excel('results/cost_enver.xlsx', sheet_name='cost')



            