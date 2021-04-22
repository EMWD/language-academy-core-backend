#!/bin/bash

# uncomment if you want to full reset venv
# rm -rf venv 
# create virtual enviroment
python3 -m venv venv
# activate virtual enviroment
source venv/bin/activate &&
# install all dependencies
pip3 install -r requirements.txt