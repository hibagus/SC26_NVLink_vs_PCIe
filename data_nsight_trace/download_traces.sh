#!/bin/bash

mkdir -p traces
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/PP1TP2.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/PP2TP1FUSED.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/PP2TP1UNFUSED.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/PP4TP1FUSED.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/PP4TP1UNFUSED.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP1PP8FUSED.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP1PP8UNFUSED.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP2PP2.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP2PP4.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP4PP1.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP4PP2.nsys-rep?download=1"
wget -c --content-disposition --progress=bar:force -P traces "https://zenodo.org/records/19718270/files/TP8PP1.nsys-rep?download=1"