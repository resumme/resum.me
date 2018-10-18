<img src="https://storage.googleapis.com/bluekiri-kiri-pro-resumme-static/static/images/logos/logo-p.png" alt="Resumme Logo"  width="300" />

> Build free resumes connecting with your favourite online schools. This plataforms will create a cool resume for you. The cool feature of this platform is the integration with your favourite course providers. While you are working hard finishing your latest courses, we will make sure to update your resume automatically.


Focus on learning, we will make sure to create a cool resume to get you a great job!

![](media/profile.gif)

## Production setup

The project is build on top of Google Cloud Platform. In production we use Google App engine in order to provide a fast and scalable solution.

To deploy the app make sure that you have the Google crendentials in the root of the "/src" folder. The deploy procedure is done using the Oauth system from Google. Without explicit permision from the @Bluekiri devops team you could not deploy the app.

To deploy the app simply run the script "deploy.sh"

```sh
bash deploy.sh
```

## Development setup

In order to run the project in development mode, you will need:

1. Virtualenv, to install the project. I use virtualenvwrapper.
2. PostgreSQL, currently using the latest version and PGadmin 4.
3. Python 3.6

Make sure that you have installed PostgreSQL in your machine and is running. You will need to create a database that matches the following database configuration:

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

Then you can create the virtual environment to install the requirements and run the project.

```sh
cd resumme/src
mkvirtualenv resumme -a . -r requirements.txt --python=`which python3.6`
python manage.py migrate
python manage.py runserver
```

## Contributing

1. Fork it (<https://github.com/resumme/resum.me>)
2. Create your feature branch (`git checkout -b feature/coolFeature`)
3. Commit your changes (`git commit -am 'Added some cool feature'`)
4. Push to the branch (`git push origin feature/coolFeature`)
5. Create a new Pull Request


## Sponsors

Without the help of this cool companies we could not provide this awesome service. Thanks for being awesome :heart:
[![Bluekiri](media/bluekiri-logo.svg)](https://bluekiri.com)
