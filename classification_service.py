from core.model import ModelWrapper
import os

def caption(audio):
    model_wrapper = ModelWrapper()
    start_time = 0
    # Getting the predictions
    try:
        preds = model_wrapper._predict(audio, start_time)
        return preds
    except ValueError:
        error = {'status': 'error', 'message': 'Invalid start time: value outside audio clip'}
        print(error, "ERROR")


def predict(file_name):

    preds = caption(file_name)

    full_res = [{'label': p[1], 'probability': p[2]}
                   for p in [x for x in preds]]
       
    os.remove(file_name)

    return full_res
