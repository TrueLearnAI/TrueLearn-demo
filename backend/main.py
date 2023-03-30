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


@app.route("/bar")
def bar():
    topics = request.args.get('topics')
    if not topics:
        return ""
    plt = BarPlotter()
    plt.plot(content=knowledge, topics=topics, history=True)
    # plt.to_html("temp.html")
    return plotly.io.to_json(plt.figure, pretty=True)


@app.route("/topics")
def topics():
    topics = []
    for _, kc in knowledge.items():
        topics.append(kc['title'])
    return topics
