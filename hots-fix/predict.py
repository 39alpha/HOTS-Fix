import pickle
import sklearn
import pandas as pd
import numpy as np
import time
import os

__HERE__ = os.path.dirname(os.path.abspath(__file__))
POSSIBLE_PREDS = ["alk", "dic", "doc", "nit", "ph", "phos", "sil", "sigma", "theta"]

def predict_from_cast(var, cast_data, models):
    """Predict the desired HOTS variable from the data collected from cast measurements"""
    if var not in POSSIBLE_PREDS:
        raise ValueError((f"Prediction Variable not supported, please check the spelling \n",
                          f"Supported variables: {POSSIBLE_PREDS}"))
    valid_cast_data = validate_cast_data(cast_data)

    pred_model = models[var]

    predictions = pred_model.predict(valid_cast_data)
    return predictions

def validate_cast_data(cast_data):
    # Cast data should be organized like
    #  ["temp", "press", "csal", "coxy"]
    x_vars = ["temp", "press", "csal", "coxy"]
    if type(cast_data) == type(dict()):
        var_present = [x for x in x_vars if x in cast_data.keys()]
        if len(var_present) != 4:
            raise ValueError("Input Cast data is incorrect")
        X = [cast_data.get(x,None) for x in x_vars]
        X_df = pd.DataFrame(np.array(X).reshape(1,-1), columns=["temp", "press", "csal", "coxy"])
    elif type(cast_data) == type(pd.DataFrame()):
        if [x for x in cast_data.columns] != x_vars:
            raise ValueError("Input Cast data is incorrect")
        X_df = cast_data
    elif type(cast_data) == type(list([0])) or type(cast_data) == type(np.array([0])):
        if len(cast_data) != 4:
            raise ValueError("Input Cast data is incorrect")
        print( (f"Assuming list or Array is organized like: "
                "[temp, press, csal, coxy]"))
        X = cast_data
        X_df = pd.DataFrame(np.array(X).reshape(1,-1), columns=["temp", "press", "csal", "coxy"])

    else:
        raise ValueError("Input Cast data format not recognized")

    return X_df

def load_all_models(preds = POSSIBLE_PREDS):
    """Load all models from file"""
    all_models = {}
    for p in preds:
        loaded_model = pickle.load(open(f"{__HERE__}/models/{p}-from-cast.sk", "rb"))
        all_models[p] = loaded_model
    return all_models

if __name__ == "__main__":
    start = time.time()
    # loaded_model = pickle.load(open("models/alk-from-cast.sk", 'rb'))
    test_T = 22.709
    test_P = 130.4
    test_csal = 35.1289
    test_coxy = 212.9
    test_list = [test_T, test_P, test_csal, test_coxy]
    
    test_dict = {"press":test_P, "temp":test_T, "csal":test_csal, "coxy":test_coxy}
    test_df = pd.DataFrame(np.array(test_list).reshape(1,-1), columns = ["temp", "press", "csal", "coxy"])
    print(predict_from_cast("alk", test_list, load_all_models()))
    print(predict_from_cast("alk", test_dict, load_all_models()))
    print(predict_from_cast("alk", test_df, load_all_models()))