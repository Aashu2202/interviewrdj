#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install system dependencies for pygobject
apt-get update
apt-get install -y libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

# Install Python dependencies
pip install -r requirements.txt
