from flask import render_template


def notFound(url):
    return render_template("urlError.html", url=url)
