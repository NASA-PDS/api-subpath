FROM python:3.11.1-alpine3.16
RUN pip3 install --quiet --upgrade setuptools pip wheel build fastapi==0.88.0 'uvicorn[standard]==0.20.0'
WORKDIR /usr/src/app
COPY ./main.py ./
EXPOSE 8000
ENTRYPOINT ["uvicorn"]
CMD [ \
    "--host", "0.0.0.0", "--port", "8000", "--access-log", "--log-level", "debug", "--root-path", "/my/app/1", \
    "main:app" \
]
