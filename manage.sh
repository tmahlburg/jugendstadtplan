#! /bin/sh
# Basic configuration script for managing development setup of this project

# sets up an admin account, if none exist
setup_admin () {
	cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()  # get the currently active user model,

User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
EOF
}

# manages docker startup
setup_docker () {
	python manage.py migrate
	setup_admin
	python manage.py runserver 0.0.0.0:8000
}

# manages docker startup for production environments
setup_prod () {
	docker-compose down -v
	docker-compose -f docker-compose.prod.yml down -v
	docker-compose -f docker-compose.prod.yml up -d --build
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
}

case "$1" in
	setup_admin) setup_admin ;;
	setup_docker) setup_docker ;;
	setup_prod) setup_prod ;;
	*) echo "Specify command: setup_admin or setup_docker"
		return 1 ;;
esac
