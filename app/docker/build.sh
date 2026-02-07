#!/usr/bin/env bash

set -e

: "${MODE:=development}"

echo "Installing requirements"
if [ "$MODE" = "development" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/development.txt"
elif [ "$MODE" = "ci" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/ci.txt"
elif [ "$MODE" = "production" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/production.txt"
elif [ "$MODE" = "staging" ]; then
    pip3 install --no-input --no-cache-dir -r "$1/staging.txt"
fi
echo "Requirements installed"
