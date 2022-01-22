# car-price-prediction

This project provides starter code for Car Price Prediction.
By utilizing this base framework, we can try out - build model faster through iterations


## Installation
This project is developed using Python 3.8.12
```sh
pip install -r requirements.txt
```

Copy config.json.template and fill the required information

## Features
- [x] Save training result to Airtable
- [ ] Data Processing pipeline
- [ ] Auto model evaluation & training 


## Roadmap
- [x] Model evaluation
    - [x] MAE
    - [x] MAPE
    - [x] RMSE
    - [x] MAPE
- [x] Save result in Airtable
- [x] Data Preprocessing
    - [x] Data normalization (JSON Flatten)
    - [x] Drop all-value-missing fields (or equal to zero all)
    - [x] Drop strongly correlation fields
- [ ] Data cleaning 
    - [ ] Handling wrong input 'Used_distance'
    - [ ] Handling wrong input 'Serie'
- [ ] Modeling