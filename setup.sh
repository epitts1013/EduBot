#!/bin/bash

# create configuration file
echo "# ~ is placeholder value, replace with your configuration
# Bot
api_token: ~
debug_mode: false

# Database
database_url: ~
database_user: ~
database_password: ~" > config.yaml

# install dependencies
python -m pip install -r requirements.txt