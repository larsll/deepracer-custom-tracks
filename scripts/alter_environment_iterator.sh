#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
DR_DIR="$(dirname $SCRIPT_DIR)"
ENV_FILE="$1"

if [[ -f "$DR_DIR/$ENV_FILE" ]]; then
  source $DR_DIR/bin/activate.sh $DR_DIR/$ENV_FILE
else
  echo "File $ENV_FILE does not exist."
  exit 1
fi

for container in $(docker ps -q -f name=deepracer-${DR_RUN_ID}_robomaker); do
    echo Container: $container
    docker exec $container bash -c "source /opt/simapp/setup.bash && python3 /scripts/alter_environment_random.py"
    echo ""
done
