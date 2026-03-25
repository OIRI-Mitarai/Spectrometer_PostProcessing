import os
import pandas as pd

data_folder = 'data'

txt_files = [f for f in os.listdir(data_folder) if f.endswith('.txt')]

merged_df = None

for file in txt_files:
    file_path = os.path.join(data_folder, file)

    # skip 1st row
    df = pd.read_csv(file_path, encoding='cp932', skiprows=1)

    # temporary define column name(header)
    df.columns = ['波長[nm]', '透過率']

    # file name for columns(header)
    sample_name = os.path.splitext(file)[0]

    # rename
    df = df[['波長[nm]', '透過率']].rename(columns={'透過率': sample_name})

    # set λ parameter
    if merged_df is None:
        merged_df = df
    else:
        merged_df = pd.merge(merged_df, df, on='波長[nm]', how='outer')

# save
merged_df.to_csv('merged_data.csv', index=False, encoding='utf-8-sig')

print("saved at merged_data.csv")
