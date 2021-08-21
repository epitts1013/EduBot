#!/bin/bash

# create configuration file
echo "Bot:
  api_token:

Database:
  database_url:
  database_user:
  database_password:" > config.yaml

# install dependencies
python -m pip install -r requirements.txt