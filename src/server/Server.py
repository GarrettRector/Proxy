import requests.exceptions
import references.notFound as notFound
from ServerWorker import serverWorker
from flask import Flask, request, Response

app = Flask(__name__, template_folder="template")

host = "localhost"
port = 8000


@app.route("/", methods=["GET"])
def incoming():
    url = request.args.get("")
    if not url:
        return notFound.notFound(url)
    try:
        return Response(serverWorker(url, f"{host}:{port}").getUrl())
    except requests.exceptions.ConnectionError:
        return notFound.notFound(url)


if __name__ == "__main__":
    app.run(host=host, port=port)
