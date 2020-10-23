from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
from db_models.models.result_model import Result
import init
from classification_service import predict
import globals
import requests

global_init()

def save_to_db(db_object, to_save):
    print("*****************SAVING TO DB******************************")
    db_object.labels = db_object.labels.append(to_save["labels"]) 
    db_object.scores = db_object.scores.append(to_save["scores"])
    db_object.save()
    print("*****************SAVED TO DB******************************")


def update_state(file):
    payload = {
        'topic_name': globals.RECEIVE_TOPIC,
        'client_id': globals.CLIENT_ID,
        'value': file
    }
    try:
        requests.request("POST", globals.DASHBOARD_URL,  data=payload)
    except: 
        print("EXCEPTION IN UPDATE STATE API CALL......")


if __name__ == "__main__":
    print('main fxn')
    print("Connected to Kafka at " + globals.KAFKA_HOSTNAME + ":" + globals.KAFKA_PORT)
    print("Kafka Consumer topic for this Container is " + globals.RECEIVE_TOPIC)
    for message in init.consumer_obj:
        message = message.value
        db_key = str(message)
        print(db_key, 'db_key')
        try:
            db_object = Cache.objects.get(pk=db_key)
        except:
            print("EXCEPTION IN GET PK... continue")
            continue

        file_name = db_object.file_name
        
        print("#############################################")
        print("########## PROCESSING FILE " + file_name)
        print("#############################################")

       
        with open(file_name, 'wb') as file_to_save:
            file_to_save.write(db_object.file.read())
        try:
            audio_results = predict(file_name)
        except:
            print("ERROR IN PREDICE")
            continue
        to_save = audio_results
        print("to_save audio", to_save)
        save_to_db(db_object, to_save)
        print(".....................FINISHED PROCESSING FILE.....................")
        update_state(file_name)