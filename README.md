# Resumme
> Dynamic resumes build from your favourite course providers. This plataforms will create a cool resume for you. The cool feature of this platform is the integration with your favourite course providers. While you are working hard finishing your latest courses, we will make sure to update your resume automatically.


Focus on learning, we will make sure to create a cool resume to get you a great job!

![](media/profile.gif)

## Production setup

The project is build on top of Docker. First of all make sure that you have a .env file in the root of the repo. The file should look something like this:

```sh
SECRET_KEY=randomStringThatWillBeUsedAsSecretKey
DEBUG=False
```

Once you have your env file setted, you simply can run:

```sh
docker-compose up
```


## Development setup

In order to run the project in development mode, you should run it without Docker. You will need:

1. Virtualenv, to install the project. I use virtualenvwrapper.
2. PostgreSQL, currently using the latest version and PGadmin 4.
3. Python 3.6

First of all you need to configure the DB in your local machine. Use the default settings of the PGadmin.
You will also need to set up a .env file with Debug enabled

```sh
SECRET_KEY=randomStringThatWillBeUsedAsSecretKey
DEBUG=True
```

Then you can create the virtual env and install the requirements.

```sh
cd resumme/src
mkvirtualenv resumme -a . -r requirements.txt --python=`which python3.6`
python manage.py migrate
python manage.py runserver
```

## Contributing

1. Fork it (<https://github.com/adriancast/resum.me>)
2. Create your feature branch (`git checkout -b feature/coolFeature`)
3. Commit your changes (`git commit -am 'Added some cool feature'`)
4. Push to the branch (`git push origin feature/coolFeature`)
5. Create a new Pull Request
