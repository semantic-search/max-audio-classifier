import json
import uuid
from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
from db_models.models.result_model import Result
import init
from classification_service import predict
import globals
import requests

global_init()

def save_to_db(db_object, result_to_save):
    print("*****************SAVING TO DB******************************")
    result_obj = Result()
    result_obj.results = result_to_save
    result_obj.model_name = globals.RECEIVE_TOPIC
    db_object.results.append(result_obj)
    db_object.save()
    print("*****************SAVED TO DB******************************")


def update_state(file):
    payload = {
        'topic_name': globals.RECEIVE_TOPIC,
        'client_id': globals.CLIENT_ID,
        'value': file
    }
    requests.request("POST", globals.DASHBOARD_URL,  data=payload)


def send_to_topic(topic, value_to_send_dic):
    # default=convert only used in this project
    data_json = json.dumps(value_to_send_dic)
    init.producer_obj.send(topic, value=data_json)


if __name__ == "__main__":
    print('main fxn')
    print("Connected to Kafka at " + globals.KAFKA_HOSTNAME + ":" + globals.KAFKA_PORT)
    print("Kafka Consumer topic for this Container is " + globals.RECEIVE_TOPIC)
    for message in init.consumer_obj:
        message = message.value
        db_key = str(message)
        print(db_key, 'db_key')
        db_object = Cache.objects.get(pk=db_key)
        file_name = db_object.file_name
        
        print("#############################################")
        print("########## PROCESSING FILE " + file_name)
        print("#############################################")

        if db_object.is_doc_type:
            """document"""
            if db_object.contains_images:
                images_array = []
                for image in db_object.files:
                    pdf_image = str(uuid.uuid4()) + ".jpg"
                    with open(pdf_image, 'wb') as file_to_save:
                        file_to_save.write(image.file.read())
                    images_array.append(pdf_image)
                to_save = []
                for image in images_array:
                    audio_results = predict(image)
                    to_save.append(audio_results)
                print("to_Save in docs", to_save)
                # save_to_db(db_object, to_save)
                print(".....................FINISHED PROCESSING FILE.....................")
                # update_state(file_name)
            else:
                pass

        else:
            """image"""
            print('in image type')
            with open(file_name, 'wb') as file_to_save:
                file_to_save.write(db_object.file.read())
            audio_results = predict(file_name)
            
            to_save = [audio_results]
            print("to_save img", to_save)
            # save_to_db(db_object, to_save)
            print(".....................FINISHED PROCESSING FILE.....................")
            # update_state(file_name)