#!/bin/bash

# Update package lists
apt-get update

# Install build dependencies for Python packages like greenlet
apt-get install -y build-essential python3-dev libssl-dev libffi-dev

# Install Python dependencies via pip
pip install -r requirements.txt
