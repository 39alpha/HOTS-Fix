import pickle
import sklearn
import pandas as pd
import numpy as np
import time

def predict_from_cast(var, cast_data, models):
    """Predict the desired HOTS variable from the data collected from cast measurements"""
    

def validate_cast_data(cast_data):
    # Cast data should be organized like
    #  ["temp", "press", "csal", "coxy"]
    x_vars = ["temp", "press", "csal", "coxy"]
    if type(cast_data) == dict():
        var_present = [x for x in x_vars if x in cast_data.keys()]
        if len(var_present) != 4:
            raise ValueError("Input Cast data is not complete")
        X = [cast_data.get(x,None) for x in x_vars]
    elif type(cast_data) == type(pd.DataFrame()):
        if [x for x in cast_data.columns] != x_vars:
            raise ValueError("Input Cast data is not complete")
        X = [x for x in cast_data[x_vars]]
    elif type(cast_data) == list() or type(cast_data) == type(np.array()):
        if len(cast_data) != 4:
            raise ValueError("Input Cast data is not complete")

        print( ("Assuming list or Array is organized like: ",
                "[temp, press, csal, coxy]"))
    
def load_all_models(preds = ["alk", "dic", "doc", "nit", "ph", "phos", "sil", "sigma", "theta"]):
    """Load all models from file"""
    all_models = {}
    for p in preds:
        loaded_model = pickle.load(open(f"models/{p}-from-cast.sk", "rb"))
        all_models[p] = loaded_model
    return all_models

if __name__ == "__main__":
    start = time.time()
    loaded_model = pickle.load(open("models/alk-from-cast.sk", 'rb'))
    print(time.time() - start)