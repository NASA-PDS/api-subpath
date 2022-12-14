# 💁‍♀️ Demonstration of an API on a Subpath served with HTTPS

This repository demonstrates how we can serve a simple ReST API behind a _subpath_ and _over HTTPS_ with a self-signed certificate. The end goal will be able to have these URLs working:

-   https://0.0.0.0:8443/my/app/1/ — return a simple JSON payload `{"Hello":"🌎"}`
-   https://0.0.0.0:8443/my/app/1/items/123?q=blah — return a JSON payload `{"item_id":"123","q":"blah}`
-   https://0.0.0.0:8443/my/app/1/docs — Swagger-style docs
-   https://0.0.0.0:8443/my/app/1/redoc — Redoc-style docs


## 👩‍💻 The Application

First step is to build the demo application:

    cd app
    python3.10 -m venv venv
    venv/bin/pip3 install --quiet --upgrade setuptools pip wheel build fastapi==0.88.0 'uvicorn[standard]==0.20.0'

Test it out:

    venv/bin/uvicorn --reload main:app

These URLs should now work:

-   https://0.0.0.0:8443/my/app/1/
-   https://0.0.0.0:8443/my/app/items/123?q=haha
-   https://0.0.0.0:8443/my/app/1/docs
-   https://0.0.0.0:8443/my/app/1/redoc

Now hit ⌃C (or whatever your interrupt key is) and make a Docker image:

    docker image build --tag myapp:latest .

The key point in the `Dockerfile` is:

    "--root-path", "/my/app/1"

This tells FastAPI how to find the `openapi.json` file. The ReST APIs _will work without this_, but the `/docs` and `/redoc` user interfaces won't function.

Now go onto the next step below.


## 🚒 Make a Custom Nginx Webserver

Head into the `web` directory and make the image:

    cd ../web
    docker image build --tag mynginx:latest .

That's it. The key points are:

    location /my/app/1/

which tells Nginx what subpath to look for, and

    proxy_pass http://app:8000/

Here, the trailing slash here tells Nginx to map that to the `/` endpoint in the `app`.


## 🎼 Start the Composition

Now we can start it all up:

    cd ..
    docker compose up

These URLs will now function (once you get past the self-signed certificate warnings):

-   https://0.0.0.0:8443/my/app/1/
-   https://0.0.0.0:8443/my/app/1/items/123?q=whatever
-   https://0.0.0.0:8443/my/app/1/docs
-   https://0.0.0.0:8443/my/app/1/redoc
