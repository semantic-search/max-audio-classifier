from core.model import ModelWrapper
import os

def caption(audio):
    model_wrapper = ModelWrapper()
    start_time = 0
    # Getting the predictions
    try:
        preds = model_wrapper._predict(audio, start_time)
    except ValueError:
        error = {'status': 'error', 'message': 'Invalid start time: value outside audio clip'}
        print(error)
    return preds


def predict(file_name, doc=False):

    preds = caption(file_name)

    full_res = [{'label': p[1], 'probability': p[2]}
                   for p in [x for x in preds]]
    text_res = [{'label': p[1]}
                   for p in [x for x in preds]]
    if doc:
        response = {
            "full_res": full_res,
            "text_res": text_res
        }
    else:
        response = {
            "file_name": file_name,
            "full_res": full_res,
            "text_res": text_res,
            "is_doc_type": False
        }
        
    os.remove(file_name)

    return response
