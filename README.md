## RUN IMAGE FROM GHCR 

```sh
docker run -it --env-file .env ghcr.io/semantic-search/max_audio_classifier:latest
```

- Make sure you have `.env` file with following parameters
```.env
KAFKA_HOSTNAME=
KAFKA_PORT=
MONGO_HOST=
MONGO_PORT=
MONGO_DB=
MONGO_USER=
MONGO_PASSWORD=
KAFKA_CLIENT_ID=
KAFKA_USERNAME=
KAFKA_PASSWORD=
DASHBOARD_URL=
CLIENT_ID=151515
```

To build the docker image locally, run: 

```git
    git clone --recurse-submodules https://github.com/semantic-search/max-audio-classifier.git
```

```
docker build -t max-audio-classifier .
```

```
docker run -it  --env-file .env max-audio-classifier
```


