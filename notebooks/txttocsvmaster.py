#combine all the separate raw data files into a single master csv file

import os
import pandas as pd

folder_path = "C:/Users/paul3/Desktop/master_text_data" 
output_csv = "master.csv"


text_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")] #list all the txt files in the folder

all_data = []

#loop through each file and process it
for file in text_files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path, delimiter="\t", header=None, engine="python")
        
        df.insert(0, "Source_File", file)  

        all_data.append(df)
    except Exception as e:
        print(f"Error processing {file}: {e}")

#concatenate all df and save to a CSV
if all_data:
    master_df = pd.concat(all_data, ignore_index=True)
    master_df.to_csv(output_csv, index=False)

    print(f"Master CSV created: {output_csv}")
else:
    print("No valid text files found or processed.")
