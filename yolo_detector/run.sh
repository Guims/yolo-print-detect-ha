#!/command/with-contenv bashio

bashio::log.info "Starting YOLO Print Detection service..."

CONFIG_PATH=/data/options.json

CAMERA_URL=$(bashio::config 'camera_url')
THRESHOLD=$(bashio::config 'threshold')

export CAMERA_URL
export THRESHOLD

bashio::log.info "Camera URL: ${CAMERA_URL}"
bashio::log.info "Threshold: ${THRESHOLD}"

cd /app

python3 detector.py
