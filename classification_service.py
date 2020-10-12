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

    with open(file_name, 'rb') as fd:
        contents = fd.read()

    preds = caption(contents)
    # print(preds, "preds in service")

    final_labels = []
    final_scores = []

    [final_labels.append(p[1]) for p in [x for x in preds]]
    [final_scores.append(float(p[2])) for p in [x for x in preds]]

    # full_res = [{'label': p[1], 'probability': p[2]}
    #                for p in [x for x in preds]]
       
    os.remove(file_name)

    final_result = {
        "labels": final_labels,
        "scores": final_scores
    }
    return final_result
