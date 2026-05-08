ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.7
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    python3 \
    py3-pip \
    curl \
    ffmpeg

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app /app

CMD ["/init"]
