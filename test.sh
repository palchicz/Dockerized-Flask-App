APP_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/app"
docker run -e "APP_SETTINGS=config.TestConfig" -v $APP_ROOT:/app -w /app flask-docker-workflow nosetests
