# ASIA
A tool for the semantic enrichment of data available in tabular formats.

## Installation requirements
ASIA requires the following frameworks to be installed:
* [Django Web Framework](https://docs.djangoproject.com/en/1.11/intro/install/)
* [Django REST Framework](http://www.django-rest-framework.org/#installation)

## Project configuration settings
Create a copy of local_settings.py.template file, and rename it as local_settings.py.
Fill in all parameters in local_settings.py file.

## Run development server
Start the development server by running the following command:
```bash
$ python manage.py runserver
```
By default the server starts on port 8000. Please refer to official [Django Documentation](https://docs.djangoproject.com/en/2.0/) to learn how to configure 
server in different ways.

## License
ASIA is released under GNU Lesser General Public License v3.0.