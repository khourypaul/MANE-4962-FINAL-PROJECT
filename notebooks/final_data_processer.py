import pandas as pd
import numpy as np
import os

def compute_rms(series):
    #Compute the root mean square
    return np.sqrt(np.mean(series**2))

def compute_mav(series):
    #Compute the mean absolute value 
    return np.mean(np.abs(series))

def compute_ssc(series):
    #Compute the number of slope sign changes 
    
    diff = np.diff(series)
    #sign change plus one whenever the product of consecutive differences is negative
    ssc_count = np.sum(diff[:-1] * diff[1:] < 0)
    return ssc_count

def process_emg_data(input_csv):
    #read the csv file with the second row as header
    df = pd.read_csv(input_csv, header=1)
    
    df = df.iloc[:, 1:]
    
    df = df.apply(pd.to_numeric, errors='coerce')
    
    #ignore rows with any NaN values (improperly formatted data)
    initial_row_count = len(df)
    df.dropna(inplace=True)
    dropped = initial_row_count - len(df)
    if dropped > 0:
        print(f"Dropped {dropped} improperly formatted row(s).")
    
    #create a grouping key for contiguous segments (instances) where the 'class' doesn't change.
    df['group'] = (df['class'] != df['class'].shift()).cumsum()
    
    #sensor channel columns have 'channel' in their names
    sensor_cols = [col for col in df.columns if 'channel' in col]
    
    #compute RMS, MAV, SSC for each col
    instances = []
    for group_id, group_data in df.groupby('group'):
        instance = {}
        for col in sensor_cols:
            instance[col + '_RMS'] = compute_rms(group_data[col])
            instance[col + '_MAV'] = compute_mav(group_data[col])
            instance[col + '_SSC'] = compute_ssc(group_data[col])

        instance['class'] = group_data['class'].iloc[0]
        instance['instance'] = group_id 
        instances.append(instance)
    
    result_df = pd.DataFrame(instances)
    
    ordered_cols = ['instance']
    for col in sensor_cols:
        ordered_cols.extend([col+'_RMS', col+'_MAV', col+'_SSC'])
    ordered_cols.append('class')
    result_df = result_df[ordered_cols]
    
   
    base, ext = os.path.splitext(input_csv)  #generate the output file path.
    output_csv = f"{base}_RMS_MAV_SSC{ext}"
    

    result_df.to_csv(output_csv, index=False)     #save resultats
    print(f"Processed data saved to {output_csv}")

input_csv_path = "master.csv" 

process_emg_data(input_csv_path)

