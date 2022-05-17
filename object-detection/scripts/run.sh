#!/usr/bin/env bash
docker run \
    --publish 8888:8888 \
    --interactive --tty \
    --rm \
    ai-playground-object-detection
