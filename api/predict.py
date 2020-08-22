#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from tapap import ModelWrapper
import typer
import re

# set up parser for audio input data

model_wrapper = ModelWrapper()


# @MAX_API.doc('predict')
# @MAX_API.expect(input_parser)
# @MAX_API.marshal_with(predict_response)
def predict(file: typer.FileBinaryRead = typer.Option(...)):
    """Predict audio classes from input data"""

    # processed_total = 0
    # for bytes_chunk in file:
    #     # Process the bytes in bytes_chunk
    #     processed_total += len(bytes_chunk)
    # typer.echo(f"Processed bytes total: {processed_total}")

    # audio_data = args.audio.read()
    audio_data = file.read()

    # Getting the predictions
    try:
        preds = model_wrapper._predict(audio_data, 0)
    except Exception as e:
        print("eror in predictions")

    # Aligning the predictions to the required API format
    label_preds = [{'label_id': p[0], 'label': p[1], 'probability': p[2]} for p in preds]
    print("lelabel_preds", label_preds)
    # Filter list
    # if args['filter'] is not None and any(x.strip() != '' for x in args['filter']):
    #     label_preds = [x for x in label_preds if x['label'] in args['filter']]

    # result['predictions'] = label_preds
    # result['status'] = 'ok'


if __name__ == "__main__":
    typer.run(predict)

