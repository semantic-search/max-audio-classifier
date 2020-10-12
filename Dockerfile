FROM codait/max-base:v1.3.2
LABEL org.opencontainers.image.source https://github.com/semantic-search/max-audio-classifier

ARG model_bucket=https://max-cdn.cdn.appdomain.cloud/max-audio-classifier/1.0.0
ARG model_file=assets.tar.gz

WORKDIR /workspace

RUN wget -nv --show-progress --progress=bar:force:noscroll ${model_bucket}/${model_file} --output-document=assets/${model_file} && \
  tar -x -C assets/ -f assets/${model_file} -v && rm assets/${model_file}

COPY requirements.txt /workspace
RUN pip install -r requirements.txt

COPY . /workspace

CMD ["python", "main.py"]

