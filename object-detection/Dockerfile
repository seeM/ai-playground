# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

EXPOSE 8888

# Source: https://github.com/open-mmlab/mmdetection/blob/240d7a31c745578aa8c4df54c3074ce78b690c34/docker/Dockerfile#L11-L13
RUN apt-get update \
    && apt-get install --yes gcc ffmpeg libsm6 libxext6 git ninja-build \
       libglib2.0-0 libsm6 libxrender-dev libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install torch==1.11.0 torchvision==0.12.0 openmim && \
    mim install mmdet
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

# Source: https://stackoverflow.com/a/39734201
CMD [ "jupyter-notebook", "--allow-root", "--no-browser", "--ip=0.0.0.0" ]
