#!/usr/bin/env bash
docker stop flasksocketiosample && docker container rm flasksocketiosample
cd /opt/flasksocketiosample
docker build --no-cache -t flasksocketiosample .
docker run -d -p 12380:12380 --name=flasksocketiosample -ti -v /flasksocketiosample:/flasksocketiosample flasksocketiosample