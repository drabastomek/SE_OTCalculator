#!/bin/bash

echo "Azure Storage installation start"

cd "/tmp"
git clone git://github.com/Azure/azure-storage-python.git
cd azure-storage-python
python setup.py install

echo "Azure Storage installation completed"