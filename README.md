# HOTS-Fix
A python package for predicting missing data from the [HOTS (Hawaiian Ocean Timeseries)](https://hahana.soest.hawaii.edu/hot/)

This package used publically availble data from HOTS to train a Random Forest Model to predict
ocean composition variables from measurements that are made by the "CTD" instruments on HOTS Cruises.

For more information on the difference between HOTS measurements via "CTD" or "bottle"
measurements see the
[HOTS documentation](https://hahana.soest.hawaii.edu/hot/protocols/protocols.html#). See the
`CTD Protocols and Salinity` procedures specifically.

The four CTD measurements are required to make predictions: 
- `temp`
- `press`
- `csal`
- `coxy`

The following variables can be predicted:
- `alk`
- `dic`
- `doc`
- `init`
- `ph`
- `phos`
- `sil`
- `sigma`
- `theta`


## Install

If you simply want to use `HOTS-Fix` you can just install it via

```
/> git clone https://github.com/39alpha/HOTS-Fix
/> cd HOTS-Fix
/HOTS-Fix> pip install .
```
This will use the prebuilt models based on `39 Alpha` data cleaning and model training.
The relative accuracy (e.g. Mean % Error) of these models are shown in the table below

<img src="/hots_fix/models/RF_Prediction_Accuracy_Cast_Data.jpeg" alt="Accuracy" width="400"/>

### Data processing and Model Building
The data provided in this repository was collected from HOTS using the method described below and saved as NetCDF files in `data/raw-hots`. The pipeline to convert the NetCDF files to .csv and then train the prediction models is done using the `hots_fix/build_models.py` file, which contains the data cleaning and filtering steps.

This code could be adapted to achieve different modelling objectives or use different sets of data.

## Limitations

This predictions made by these models have relatively high accuracy for the HOTS dataset. But the regularity these models capture is specific to the HOTs dataset, so it does not generalize to different regions of the ocean (such as Bermuda for example). This was tested using the BATS dataset, and that work is not shown here. If you want to use this model in different regions of the ocean i) we discourage that, ii) you should test the accuracy for your specific use case. 

## Examples

You can use multiple different input formats for the prediction. The simplest is the
is to use a `list` but you need to ensure the list ordered correctly.

```
>>> import hots_fix
>>> example_cast_data = [22.709, 130.4, 35.1289, 212.9] # [temp, press, csal, coxy]
>>> hots_fix.predict("alk", example_cast_data) # array([2306.94])
```

If you don't want to worry about the order of the variables you can use a dictionary, or a
DataFrame (which can use multiple rows)
```
>>> import numpy as np
>>> import pandas as pd
>>> import hots_fix
>>> example_data = pd.DataFrame(np.array([22.709, 130.4, 35.1289, 212.9]).reshape(1,-1),
                                columns = ["temp", "press", "csal", "coxy"])
>>> hots_fix.predict("alk", example_data) # array([2306.94])
```


## Source Data 
This data is from Hawaiian Ocean timeseries datasets. 

It was collected on February 26th 2022 using the HOT-DOGS web tool (https://hahana.soest.hawaii.edu/hot/hot-dogs/bextraction.html)

The Data comes from the `Bottle` Selection tool. 

The following query was selected:

Stations: 1,2,6,8,50,52 (all were performed in sequence as different queries)

Dates (default range): Oct, 0, 1, 1988 - Dec 3, 1, 2020

Fields:
- Potential Temperature 
- Potential Density 
- CTD Temperature
- CTD Salinity 	
- CTD Oxygen 
- Bottle Salinity
- Bottle Dissolved Oxygen 
- Dissolved Inorganic Carbon 
- pH
- Alkalinity 
- Phosphate 
- Nitrate + Nitrite
- Nitrite 
- Silicate 
- Dissolved Organic Phosphorus
- Dissolved Organic Nitrogen 
- Dissolved Organic Carbon 
- Total Dissolved Phosphorus
- Total Dissolved Nitrogen 
- Particulate Phosphorus 
- Particulate Nitrogen
- Particulate Silica 
- Particulate Carbon 
- Low-Level Phosphorus 
- Low-Level Nitrogen 

A warning was raised that Analytical Methods have changed over the time range. 


