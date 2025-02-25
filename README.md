## DRF Generic Contact

[![PyPI version](https://img.shields.io/pypi/v/drf-generic-contact.svg)](https://pypi.org/project/drf-generic-contact/)
[![Run linter and tests](https://github.com/anexia/drf-generic-contact/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/anexia/drf-generic-contact/actions/workflows/test.yml)
[![Codecov](https://img.shields.io/codecov/c/gh/anexia/drf-generic-contact)](https://codecov.io/gh/anexia/drf-generic-contact)

An extension of the [django-generic-contact](https://github.com/anexia/django-generic-contact) that provides a POST endpoint to create new instances for
the `Contact` model via HTTP.

### Installation

```shell
pip install drf-generic-contact
```

Make sure the main module [django-generic-contact](https://github.com/anexia/django-generic-contact) is part of the INSTALLED_APPS.

### Usage

Add the `ContactViewSet` to your project's `urls.py`, e.g.:

```
from drf_generic_contact.rest.views import ContactViewSet

router = get_api_router()
router.register(r"contact", ContactViewSet)

urlpatterns = [
    ...
    path("", include(router.urls)),
]
```

See `tests/testapp` for exemplary usage.

## Unit Tests

See folder [tests/](tests/). The provided tests cover these criteria:
* success:
  * add new contact via HTTP POST request
* failure:
  * HTTP GET request to read contact list
  * HTTP GET request to read single contact
  * HTTP PUT request to update contact
  * HTTP PATCH request to update contact

Follow below instructions to run the tests.
You may exchange the installed Django and DRF versions according to your requirements.
:warning: Depending on your local environment settings you might need to explicitly call `python3` instead of `python`.
```bash
# install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# setup environment
pip install -e .

# run tests
cd tests && python manage.py test
```

### Contributing

Contributions are welcomed! Read the [Contributing Guide](CONTRIBUTING.md) for more information.

### Licensing

See [LICENSE](LICENSE) for more information.
