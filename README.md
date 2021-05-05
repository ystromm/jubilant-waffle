# jubilant-waffle

## Build a  simple web server and dockerize it

### Web Server 

requests.txt:
````text
Flask==1.0
requests==2.25.1
````
app.py:
```python
import os

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    search = requests.get("https://api.thecatapi.com/v1/images/search").json()
    print(search)
    url = search[0]["url"]
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
```

templates/index.html:
```html
<html>
  <head>
    <style type="text/css">
      body {
        background: black;
        color: white;
      }
      h4 {
        text-transform: uppercase;
      }
    </style>
  </head>
  <body>
      <h4>Cat of the day</h4>
      <img src="{{url}}" />
  </body>
</html>
```

```
python3 app.py
```

Dockerfile:

```docker
FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
```

### Build and run

```
docker build . -t cat
docker run -d cat
curl localhost:5000
docker ps 
docker stop <container id>
```

No cats?

```
docker run -p80:5000 -d cat
docker ps
curl localhost
```

### Push to docker repo

