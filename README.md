This is a work in progress

## Starting

Create a virtuan environment and activate it.

```
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements.

```
pip install -r requirements.txt
```

You then need to start both the action server and the REST api.

```
rasa run actions
rasa run --enable-api --cors "*"
```
