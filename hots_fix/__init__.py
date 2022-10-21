from .predictions import load_all_models, predict_from_cast

all_models = load_all_models()

def predict(var, cast_data):
    """
    Predict the one of the availible HOTS measurements from from the CTD data

    Args:
    var: Variable to predict which must be one of the following strings:
        ["theta", "sigma", "dic", "ph", "alk", "phos", "nit", "sil", "doc"].
    cast_data: CTD data in one of the following formats:
            - Pandas DataFrame with the following columns ["temp", "press", "csal", "coxy"]
              (multiple rows supported)
            - Dictionary with the following keys ["temp", "press", "csal", "coxy"]
            - List or numpy array in the following order  ["temp", "press", "csal", "coxy"]

    Returns:
        An array containing the predictions for `var` based on the CTD inputs.

    Example:
    ```
        >>> import hots_fix
        >>> example_cast_data = [22.709, 130.4, 35.1289, 212.9] # [temp, press, csal, coxy]
        >>> hots_fix.predict("alk", example_cast_data) # array([2306.94])
    ```
    """
    return predict_from_cast(var, cast_data, all_models)