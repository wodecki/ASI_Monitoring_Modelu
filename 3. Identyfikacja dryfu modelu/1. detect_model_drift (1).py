import numpy as np
import pandas as pd
from datetime import date, datetime
import os.path

# Read model evaluation results
eval_results = pd.read_csv('evaluation/model_eval.csv')

print(eval_results['time_stamp'].max())


'''
# Create the evaluation dataframe
eval_df = pd.DataFrame()

now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': batch_no, 'metric': 'RMSE', 'score': RMSE}, ignore_index=True)
eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': batch_no, 'metric': 'r2', 'score': r2}, ignore_index=True)

# Save evaluation to file
evaluation_file_name = 'evaluation/model_eval.csv'

if os.path.isfile(evaluation_file_name):
    eval_df.to_csv('evaluation/model_eval.csv', mode='a', index=False, header=False)
else:
    eval_df.to_csv('evaluation/model_eval.csv', index=False)
'''