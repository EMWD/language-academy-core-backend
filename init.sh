#!/bin/bash

# uncomment if you want to full reset venv
# rm -rf venv 

python3 -m venv venv

source venv/bin/activate &&

pip3 install -r requirements.txt