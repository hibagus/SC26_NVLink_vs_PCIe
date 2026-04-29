#!/bin/bash

# Download from Zenodo
echo "Downloading part 1 of 2..."
wget -c --content-disposition https://zenodo.org/records/19866687/files/mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.00?download=1
echo "Downloading part 2 of 2..."
wget -c --content-disposition https://zenodo.org/records/19867168/files/mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.01?download=1

# Assemble the parts
echo "Assembling parts to form complete image..."
cat mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.* > mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz

# Delete Parts
# echo "Deleting parts..."
# rm mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.*

# Load Image to Docker
echo "Loading Docker Image..."
docker load -i mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz

# Tag Docker Image
echo "Tagging Docker Image..."
docker tag ec1a18b3145216b64fab8c32c85e5a8a9a6c41190cdce28ca5efa508a0319189 ghcr.io/hibagus/sc26_nvlink_vs_pcie/mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release:latest
