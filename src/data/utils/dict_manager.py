import pickle

def save_dict(pth: str, d: dict) -> bool:
    """Save dictionary using pickle.

    Args:
        pth (str): path to store dictionary. Must end in ".pickle".
        d (dict): dictionary to be stored.

    Returns:
        bool: True/False depending on success.
    """
    try:
        with open(pth, "wb") as handle:
            pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return True
    except:
        print("File not saved successfully. Check path.")
        return False
    
def load_dict(pth: str) -> dict:
    """Load dictionary using pickle.

    Args:
        pth (str): path to store dictionary. Must end in ".pickle".

    Returns:
        dict: desired dictionary
    """
    try:
        with open(pth, "rb") as handle:
            d = pickle.load(handle)
        return d
    except:
        print("File not saved successfully. Check path and try again.")