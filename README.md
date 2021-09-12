# Bloodbath Python Library

![Build Status](https://github.com/bloodbath-io/bloodbath-python/actions/workflows/main.yml/badge.svg)

The Bloodbath Python library provides convenient access to the Bloodbath API from
applications written in the Python language.


## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade bloodbath
```

Install from source with:

```sh
python setup.py install
```

## Usage

The library needs to be configured with your account's secret key which is
available in your [Bloodbath Dashboard][api-keys]. Set `bloodbath.api_key` to its
value:

```python
import bloodbath
bloodbath.api_key = "NTI6PASMD9BQhYtRh..."

# list events
events = bloodbath.Event.list()

# find an event
event = bloodbath.Event.find("b7ccff...")

# schedule an event
event = bloodbath.Event.schedule(
  scheduled_for=(datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(),
  headers="{}",
  method="post",
  body="some body content",
  endpoint='https://api.acme.com/path'
)

# cancel an event
bloodbath.Event.cancel("b7ccff...")

# print that event's id
print(event.id)
```

For more documentation about how to use Bloodbath, don't hesitate to check [Bloodbath Docs](https://bloodbath.notion.site/Guide-00a3edc8f43b4528b2e34bf5eac5b0df).

## Development

Run all tests:

```
  $ python setup.py pytest
```

[api-keys]: https://app.bloodbath.io/
