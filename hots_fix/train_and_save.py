import pickle
import pandas as pd
import numpy as np

import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

def build_rf_models(data_path):
    """ MAIN FUNCTION
    Train random forest models to predict the HOTS data from cast inputs
    """
    # Read in Data
    cleaned_data = pd.read_csv(data_path, index_col=0)
    # Drop data related to the cruise, station and cast number
    cleaned_data.drop(["crn", "stn", "cast"], axis=1, inplace=True)
    # These are cast measurements we're going to use to predict the remaining
    # observation
    features = ["temp", "press", "csal", "coxy"]
    measurables = [c for c in cleaned_data.columns if c not in features]
    # The features are constant for all models
    X = cleaned_data[features]
    # Use dictionaries to store the fit models and error
    models = dict()
    errors = dict()
    # Make a unique model for each measurable
    for m in measurables:
        mae, model = train_rf(X,cleaned_data[m])
        models[m] = model
        errors[m] = mae
    # Convert the errors to a dictionary
    error_df = pd.DataFrame.from_dict(errors, orient="index")
    error_df.rename({0:"Mean Absolute Error"}, inplace=True, axis=1)
    # Return the models and errors
    return models, error_df

def save_models(model_dict):
    """ Save models as pickled objects. Input dictionary should have the
        predicted variable as the key and the trained model as the value"""
    for pred_var, model in model_dict.items():
        pickle.dump(model, open(f"models/{pred_var}-from-cast.sk", 'wb')) 


def train_rf(X,y):
    """ Train a random forest resgressor (after center/scaling) on the data
        return the Mean absolute error from a test/train split (25% test) and
        then return a model trained on all the data for production
    """
    # Test train split
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    # Center/Scale and do random forest regression
    rf_pipe = make_pipeline(StandardScaler(), RandomForestRegressor())
    # Fit the model on trainning data
    rf_pipe.fit(X_train,y_train)
    # Predict
    y_fit = rf_pipe.predict(X_test)
    # Measure error
    mae = np.mean(abs(y_fit - y_test))
    # Retrain using full data
    full_rf_pipe = make_pipeline(StandardScaler(), RandomForestRegressor())
    full_rf_pipe.fit(X_train,y_train)
    # Return error and full trainned model
    return mae, full_rf_pipe

if __name__ == "__main__":
    cast_data_models, cast_data_models_errors = build_rf_models("..\\data\\parsed\\ideal-variables-2022.csv")
    save_models(cast_data_models)
    cast_data_models_errors.to_csv("..\\data\\parsed\\cast-model-errors-2022.csv")