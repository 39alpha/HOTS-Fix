import pandas as pd
from extract_and_clean import convert_all_cdf_to_csv, clean_hots
from train_and_save import build_rf_models, save_models

if __name__ == "__main__":
    print("Converting Data from NetCDF to .csv")
    convert_all_cdf_to_csv("..\\data\\raw-hots\\")
    print("Cleaning Data")
    clean_hots("..\\data\\raw-hots\\")
    print("Training Random Forest and Estimating Errors")
    cast_data_models, cast_data_models_errors = build_rf_models("..\\data\\parsed\\ideal-variables-2022.csv")
    print("Saving Models")
    save_models(cast_data_models)
    print("Saving Error Estimates")
    cast_data_models_errors.to_csv("..\\data\\parsed\\cast-model-errors-2022.csv")