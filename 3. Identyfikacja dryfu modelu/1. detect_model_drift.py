import numpy as np
import pandas as pd
from datetime import date, datetime
import os.path

# Read model evaluation results
eval_results = pd.read_csv('evaluation/model_eval.csv')

last_run = eval_results['time_stamp'].max()

# Prepare data for tests
RMSE_logs = eval_results[eval_results['metric']=='RMSE']
r2_logs = eval_results[eval_results['metric']=='r2']

last_RMSE = RMSE_logs[RMSE_logs['time_stamp']==last_run]['score'].values[0]
all_other_RMSE = RMSE_logs[RMSE_logs['time_stamp']!=last_run]['score'].values

last_r2 = r2_logs[r2_logs['time_stamp']==last_run]['score'].values[0]
all_other_r2 = r2_logs[r2_logs['time_stamp']!=last_run]['score'].values


### Hard test ###

# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE
hard_test_RMSE = last_RMSE > np.mean(all_other_RMSE)
# it obviously may be set as a fixed value, like
# hard_test_RMSE = last_RMSE > 1.0

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2
hard_test_r2 = last_r2 < np.mean(all_other_r2)
# it obviously may be set as a fixed value, like
# hard_test_r2 = last_r2 < 0.7

print('Hard test: RMSE', hard_test_RMSE)
print('Hard test: r2', hard_test_r2)

### Parametric test ###
# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE + 2*std of all the past RMSE
param_test_RMSE = last_RMSE > np.mean(all_other_RMSE) + 2*np.std(all_other_RMSE)

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2 - 2*std of all the past r2
param_test_r2 = last_r2 < np.mean(all_other_r2) - 2*np.std(all_other_r2)

print('Parametric test: RMSE', param_test_RMSE)
print('Parametric test: r2', param_test_r2)


### Non-parametric (IQR) test ###
# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE + 2*std of all the past RMSE
iqr_RMSE = np.quantile(all_other_RMSE, 0.75) - np.quantile(all_other_RMSE, 0.25)
iqr_test_RMSE = last_RMSE > np.quantile(all_other_RMSE, 0.75) + iqr_RMSE*1.5

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2 - 2*std of all the past r2
iqr_r2 = np.quantile(all_other_r2, 0.75) - np.quantile(all_other_r2, 0.25)
iqr_test_r2 = last_r2 < np.quantile(all_other_r2, 0.25) - iqr_r2*1.5

print('IQR test: RMSE', iqr_test_RMSE)
print('IQR test: r2', iqr_test_r2)

# Re-training signal
re_training_conditions = {
                            'hard_test_RMSE': hard_test_RMSE, 
                            'hard_test_r2': hard_test_r2,
                            'param_test_RMSE': param_test_RMSE, 
                            'param_test_r2': param_test_r2,
                            'iqr_test_RMSE': iqr_test_RMSE, 
                            'iqr_test_r2': iqr_test_r2
                        }

a1 = True
a2 = False
a3 = False
a4 = True

c1 = {'hard_test_RMSE': hard_test_RMSE, 'param_test_RMSE': param_test_RMSE, 'iqr_test_RMSE': iqr_test_RMSE, 'hard_test_r2': hard_test_r2, 'param_test_r2': param_test_r2, 'iqr_test_r2': iqr_test_r2}
for c in c1:
    print(c, c1[c])

a = {'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4}

a_set = set(a.values())
if True in set(re_training_conditions.values()):
    print('There is a truth in...')
    for c in re_training_conditions:
        if re_training_conditions[c]:
            print(c)
else:
    print('There is no truth')