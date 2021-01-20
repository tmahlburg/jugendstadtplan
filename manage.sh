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

# run gunicorn for production
run_gunicorn () {
	gunicorn jugendstadtplan.wsgi
}

case "$1" in
	setup_admin) setup_admin ;;
	setup_docker) setup_docker ;;
	run_gunicorn) run_gunicorn ;;
	*) echo "Specify command: setup_admin, setup_docker or run_gunicorn"
		return 1 ;;
esac
