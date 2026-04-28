#!/bin/bash

# Download from Zenodo
wget -c --content-disposition https://zenodo.org/records/19866687/files/mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.00?download=1
wget -c --content-disposition https://zenodo.org/records/19867168/files/mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.01?download=1

# Assemble the parts
cat mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.* > mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz

# Delete Parts
rm mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz.*

# Load Image to Docker
docker load mlpinf-v5.0-cuda12.8-pytorch25.01-ubuntu24.04-x86_64-release.tar.gz

