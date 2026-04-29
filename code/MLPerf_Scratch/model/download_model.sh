#!/bin/bash
mkdir -p Llama2

# Download from Zenodo
echo "Downloading part 1 of 3..."
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19865308/files/Llama-2-70b-chat-hf.tar.gz.00?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19865308/files/Llama-2-70b-chat-hf.tar.gz.01?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19865308/files/Llama-2-70b-chat-hf.tar.gz.02?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19865308/files/Llama-2-70b-chat-hf.tar.gz.03?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19865308/files/Llama-2-70b-chat-hf.tar.gz.04?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19865308/files/Llama-2-70b-chat-hf.tar.gz.05?download=1"

echo "Downloading part 2 of 3..."
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19867426/files/Llama-2-70b-chat-hf.tar.gz.06?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19867426/files/Llama-2-70b-chat-hf.tar.gz.07?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19867426/files/Llama-2-70b-chat-hf.tar.gz.08?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19867426/files/Llama-2-70b-chat-hf.tar.gz.09?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19867426/files/Llama-2-70b-chat-hf.tar.gz.10?download=1"
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19867426/files/Llama-2-70b-chat-hf.tar.gz.11?download=1"

echo "Downloading part 3 of 3..."
wget -c --content-disposition --progress=bar:force -P Llama2 "https://zenodo.org/records/19877464/files/Llama-2-70b-chat-hf.tar.gz.12?download=1"

# Assemble the parts
echo "Assembling parts to form complete image..."
cd Llama2
cat Llama-2-70b-chat-hf.tar.gz.* > Llama-2-70b-chat-hf.tar.gz

# Delete Parts
# echo "Deleting parts..."
# rm Llama-2-70b-chat-hf.tar.gz.*

# Extract
tar -xvf Llama-2-70b-chat-hf.tar.gz

# Delete Compressed File
# echo "Deleting Tarfile..."
# rm Llama-2-70b-chat-hf.tar.gz