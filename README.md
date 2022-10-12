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

## Example

## Limitations

