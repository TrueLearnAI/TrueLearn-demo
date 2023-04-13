import os

import plotly
from flask import (
    Flask,
    request,
    send_file
)
from flask_cors import CORS

from truelearn.utils.visualisations import (
    LinePlotter,
    PiePlotter,
    RosePlotter,
    BarPlotter,
    DotPlotter,
    BubblePlotter,
    WordPlotter,
    RadarPlotter,
    TreePlotter
)

from data.user_knowledge import knowledge


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def home():
    return "<p>Backend of the Truelearn visualisations demo.</p>"


@app.route("/topics")
def topics():
    topics = []
    for _, kc in knowledge.topic_kc_pairs():
        topics.append(kc.title)
    return topics


@app.route("/line")
def line():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = LinePlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/pie")
def pie():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = PiePlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/rose")
def rose():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = RosePlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/bar")
def bar():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = BarPlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/dot")
def dot():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = DotPlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/radar")
def radar():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = RadarPlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/tree")
def tree():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = TreePlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/bubble")
def bubble():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = BubblePlotter()
    path = "temp.png"
    plt.plot(content=knowledge, topics=topics).savefig(path)
    return send_file(path)


@app.route("/word")
def word():
    topics = request.args.get('topics')
    if not topics:
        return ""
    topics = topics.split(',')
    plt = WordPlotter()
    path = "temp.png"
    plt.plot(content=knowledge, topics=topics).savefig(path)
    return send_file(path)


if __name__ == "__main__":
    app.run()
