# Launch server

```bash
uvicorn app.main:app --reload
```

# Unit tests

```bash
pytest --cov-report term-missing --cov=app app/tests/
```

# Acceptance tests

It uses [behave](https://behave.readthedocs.io/en/latest/) to run acceptance tests.

To run them:

```bash
behave
```
