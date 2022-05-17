#!/usr/bin/env bash
docker run \
    --publish 8888:8888 \
    --interactive --tty \
    --rm \
    --volume "$PWD":/app \
    ai-playground-object-detection
