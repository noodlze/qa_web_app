FROM python:alpine3.7

WORKDIR /app

COPY . .

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python -m pip install -r requirements.txt && \
  apk --purge del .build-deps && \
  chmod +x entrypoint.sh

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
