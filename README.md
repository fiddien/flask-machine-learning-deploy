# flask-machine-learning-deploy

We create predict API with app.py wrapped in Flask and contained in Docker, while hosted in Google Cloud Virtual Machine.

The `predict` call take json file of (to-be-predicted) book_id and user_id, then return the predicted 6 highest ranked (by the inputed user_id) book_ids.

We dockerize them with following command:

```
Docker Build
docker build --rm -t flask . && \
docker rm -f flask && \
docker run -d --restart always -p 80:5000 --name flask flask
```

and check the logs by calling

```
docker logs flask
```

in the VM terminal.
