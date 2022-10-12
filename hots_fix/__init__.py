from .predictions import load_all_models, predict_from_cast

all_models = load_all_models()

def predict(var, cast_data):
    """ DOC-STRING FOR PREDICTION """
    return predict_from_cast(var, cast_data, all_models)