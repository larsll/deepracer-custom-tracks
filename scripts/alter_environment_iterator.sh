#!/usr/bin/env bash

ENV_FILE="$1"

# Check if ENV_FILE exists
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: Environment file $ENV_FILE does not exist"
    exit 1
fi

# Extract DR_RUN_ID from environment file
DR_RUN_ID=$(grep "^DR_RUN_ID=" "$ENV_FILE" | cut -d'=' -f2)

if [ -z "$DR_RUN_ID" ]; then
    echo "Error: DR_RUN_ID not found in $ENV_FILE"
    exit 1
fi

# Add eval to container name if second argument is -e
if [ "$2" = "-e" ]; then
    echo "Evaluation mode"
    CONTAINER_FILTER="deepracer-eval-${DR_RUN_ID}_robomaker"
else
    CONTAINER_FILTER="deepracer-${DR_RUN_ID}_robomaker"
fi

for container in $(docker ps -q -f name=$CONTAINER_FILTER); do
    echo Container: $container
    docker exec $container bash -c "source /opt/simapp/setup.bash && python3 /scripts/alter_environment_random.py"
    echo ""
done
