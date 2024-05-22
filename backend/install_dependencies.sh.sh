# backend/install_dependencies.sh
apt-get update && apt-get install -y \
    libffi-dev \
    libgirepository1.0-dev \
    pkg-config \
    libcairo2-dev \
    gcc \
    g++ \
    make
