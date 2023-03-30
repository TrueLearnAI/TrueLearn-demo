from flask import (
    Flask,
    request,
    render_template
)
from flask_cors import CORS
from data.user_knowledge import knowledge
from plotters import (
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
import plotly

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "<p>Backend of the Truelearn visualisations demo.</p>"


@app.route("/line")
def line():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = LinePlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/pie")
def pie():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = PiePlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/rose")
def rose():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = RosePlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/bar")
def bar():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = BarPlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/dot")
def dot():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = DotPlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/radar")
def radar():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = RadarPlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/tree")
def tree():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = TreePlotter()
    plt.plot(content=knowledge, topics=topics)
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/topics")
def topics():
    topics = []
    for _, kc in knowledge.items():
        topics.append(kc['title'])
    return topics
