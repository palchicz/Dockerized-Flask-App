APP_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/app"

docker run -e "DB_URI=sqlite:///:memory:" -v $APP_ROOT:/app -w /app flask-docker-workflow nosetests
