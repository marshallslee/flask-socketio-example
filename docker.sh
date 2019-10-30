#!/usr/bin/env bash
docker stop flasksocketioexample && docker container rm flasksocketioexample
cd /opt/flasksocketioexample
docker build --no-cache -t flasksocketioexample .
docker run -d -p 12380:12380 --name=flasksocketioexample -ti -v /flasksocketioexample:/flasksocketioexample flasksocketioexample