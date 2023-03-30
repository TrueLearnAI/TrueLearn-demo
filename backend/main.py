from flask import Flask
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

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "<p>Backend of the Truelearn visualisations demo.</p>"


@app.route("/bar")
def bar(topics):
    plt = BarPlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    return plt.to_html()


@app.route("/topics")
def topics():
    topics = []
    for _, kc in knowledge.items():
        topics.append(kc['title'])
    return topics
