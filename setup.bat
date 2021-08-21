ECHO OFF
:: create configuration file
(
echo # ~ is placeholder value, replace with your configuration
echo # Bot
echo api_token: ~
echo debug_mode: false
echo.
echo # Database
echo database_url: ~
echo database_user: ~
echo database_password: ~
) > config.yaml

:: install dependencies
python -m pip install -r requirements.txt