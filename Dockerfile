FROM python:alpine3.7

COPY requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python -m pip install -r requirements.txt && \
 apk --purge del .build-deps


CMD ["python", "/app/manage.py" ,"runserver", "--threaded"]
