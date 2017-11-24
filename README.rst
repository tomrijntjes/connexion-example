==============================
Connexion Example REST Service
==============================

This example application expands on the very basic "pet shop" REST service using the `Connexion`_ Python library by adding a PostgreSQL backend and Pony ORM.

Connexion is a framework on top of Flask_ to automagically handle your REST API requests
based on `Swagger 2.0 Specification`_ files in YAML.


Features
========

This example application shows various features supported by the Connexion library:

* mapping of REST operations to Python functions (using the ``operationId`` in ``swagger.yaml``)

  * maps path, query and body parameters to keyword arguments

* bundled Swagger UI (served on `/ui/`_ path)
* automatic JSON serialization for ``application/json`` content type
* schema validation for the HTTP request body and query parameters:

  * required object properties
  * primitive JSON types (string, integers, etc)
  * date/time values
  * string lengths
  * minimum/maximum values
  * regular expression patterns

* gevent WSGI server
* OAuth2 protection


Files
=====

The example application only needs very few files:

* ``swagger.yaml``: the pet shop REST API Swagger definition
* ``app.py``: implementation of the pet shop operations with in-memory storage
* ``requirements.txt``: list of required Python libraries
* ``Dockerfile``: to build the example as a runnable Docker image
* ``test.sh``: shell script to execute example HTTP requests against the pet shop API


Running with Docker-Compose
===================

You can build the example application as a Docker image and run it:

.. code-block:: bash

    $ docker-compose up -d pets-db
    $ docker-compose up -d pets-service
    $ ./test.sh # do some test HTTP requests



See the `uWSGI documentation`_ for more information.

.. _Connexion: https://pypi.python.org/pypi/connexion
.. _Flask: http://flask.pocoo.org/
.. _Swagger 2.0 Specification: https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md
.. _/ui/: http://localhost:8080/ui/
.. _using Flask with uWSGI: http://flask.pocoo.org/docs/latest/deploying/uwsgi/
.. _uWSGI documentation: https://uwsgi-docs.readthedocs.org/
