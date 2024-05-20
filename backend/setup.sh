#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update package lists
apt-get update

# Install necessary system dependencies
apt-get install -y pkg-config libgirepository1.0-dev libcairo2-dev libjpeg-dev libgif-dev

# Install Python dependencies
pip install -r requirements.txt
