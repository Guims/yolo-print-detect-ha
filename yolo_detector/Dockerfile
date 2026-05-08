ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.7
FROM ${BUILD_FROM}

ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8

RUN apk add --no-cache \
    python3 \
    py3-pip \
    curl \
    ffmpeg

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app /app
COPY rootfs /

RUN chmod -R a+x /etc/services.d

EXPOSE 5001
