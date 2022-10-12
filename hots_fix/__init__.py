from .predict import load_all_models, predict_from_cast
all_models = load_all_models()
def predict_hots(var, cast_data):
    return predict_from_cast(var, cast_data, all_models)