export DJANGO_SETTINGS_MODULE=resumme.settings.dev
python manage.py collectstatic --noinput
gcloud app deploy --no-promote
osascript -e 'display notification "Your gcloud instance is updated, check the terminal for more info" with title "Deploy update" sound name "default" '