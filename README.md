# Glerk

Glerk is a tool for cataloging and (eventually) digitizing your library of
physical books. Use with a barcode scanner to quickly add books to your library.

## First time setup using `just`:

```sh
just copy-env
just init-dcp
# replace `DJANGO_SECRET_KEY` in `.env` with output of below command
just dcp-generate-secret-key
just dcp-migrate
just dcp-load-dev-data
just dcp-up-all
# you can now log in with your superuser at 0.0.0.0:8000/admin
# username: admin@email.com
# password: password
```

## Installing 3rd party Python packages

```sh
python -m venv .venv
source .venv/bin/activate
pip install pipenv
PIPENV_VENV_IN_PROJECT=1 pipenv install --dev --deploy
pipenv install some_package
```

## Helpful scripts

* `just dcp-run-tests`
  * runs all tests, except those decorated with `@pytest.mark.integration`
  * tests.py test_*.py *_test.py *_tests.py
* `just django-admin <command>`
  * runs `manage.py` in the docker container with argument passthrough
  * `just django-admin makemigrations`
  * `just django-admin migrate`
  * `just django-admin startapp payments`
* `./utils/reload-docker-db.sh`
  * reloads `dev_data.json` by default
  * `./utils/reload-docker-db.sh --data=fixture_filename.json`
* `./utils/dump-data.sh`
  * `./utils/dump-data.sh > app/core/fixtures/dump-2021-10-08.json`
  * you can then reload these files with `./utils/reload-docker-db.sh`
