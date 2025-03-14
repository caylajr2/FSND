#!/bin/bash

# Update package lists
apt-get update

# Install required system dependencies
apt-get install -y build-essential python3-dev libssl-dev libffi-dev

# Upgrade pip and setuptools to make sure dependencies are installed properly
pip install --upgrade pip setuptools wheel

# Install dependencies from requirements.txt
pip install -r requirements.txt
