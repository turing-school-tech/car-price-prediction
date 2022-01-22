from datetime import datetime

import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error,\
    mean_absolute_percentage_error, mean_absolute_percentage_error

from config import config
from services.airtable import AirTableClient

table = AirTableClient(
    config['airtable']['api_key'],
    config['airtable']['base_id'],
    config['airtable']['table']
)

def get_summary_result(model, X_test, y_test):
    name = type(model).__name__
    params = str(model.get_params())
    
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    r2 = model.score(X_test, y_test)
    
    now = datetime.now()
    
    result = {
        'Model': name,
        'Hyperparams': params,
        'R2': r2,
        'RMSE': rmse,
        'MAE': mae,
        'MAPE': mape,
        'Time': now.strftime('%H:%M:%S %d-%m-%Y')
    }
    
    table.add_row(result)
    
    print(result)