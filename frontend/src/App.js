import React from 'react';
import { flushSync } from 'react-dom';
import axios from 'axios';
import VisualisationSidebar from './components/VisualisationSidebar';
import Window from './components/Window';
import TopicSidebar from './components/TopicSidebar';

import './App.css';

const server = 'http://127.0.0.1:5000';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      currentVisualisation: "bar",
      topics: [],
      selectedTopics: ["Machine learning", "Cognitive science", "Algorithm"],
      visualisation: null,
    };
    
    this.handleVizClick = this.handleVizClick.bind(this);
    this.handleTopicClick = this.handleTopicClick.bind(this);
    this.handleClearSelection = this.handleClearSelection.bind(this);
  }

  componentDidMount() {
    axios.get(server + '/topics')
      .then(response => {
        this.setState({
          topics: response.data
        });
      })
      .catch(error => {
        console.log(error);
      });
    this.getVisualisation();
  }

  getVisualisation() {
    let statics = ["bubble", "word"];
    let url = `${server}/${this.state.currentVisualisation}?topics=${this.state.selectedTopics}`;
    axios.get(url)
      .then(response => {
        let newVisualisation = null;
        if (statics.includes(this.state.currentVisualisation)) {
          newVisualisation = url;
        } else {
          newVisualisation = response.data;
        }
        flushSync(() => {
          this.setState({
            visualisation: newVisualisation
          });
        });
      })
      .catch(error => {
        console.log(error);
      })
  }

  handleVizClick(visualisationClicked) {
    flushSync(() => {
      this.setState({
        currentVisualisation: visualisationClicked
      });
    });
    this.getVisualisation();
  }

  handleTopicClick(topicClicked) {
    let currentTopics = this.state.selectedTopics;
    let newTopics = null;
    if (currentTopics && currentTopics.includes(topicClicked)) {
      newTopics = currentTopics.filter((topic) => 
        topic !== topicClicked
      );
    } else {
      newTopics = currentTopics.concat(topicClicked)
    }
    flushSync(() => {
      this.setState({
        selectedTopics: newTopics
      })
    });
    this.getVisualisation();
  }

  handleClearSelection() {
    flushSync(() => {
      this.setState({
        selectedTopics: []
      })
    });
    this.getVisualisation();
  }

  render() {
    return (
      <div id="app" style={({ height: "100vh" }, { display: "flex", justifyContent: "space-between" })}>
        <VisualisationSidebar
          currentVisualisation={this.state.currentVisualisation}
          onClick={this.handleVizClick}
        />
        <Window currentVisualisation={this.state.currentVisualisation} visualisation={this.state.visualisation} />
        <TopicSidebar
          topics={this.state.topics}
          selectedTopics={this.state.selectedTopics}
          onClick={this.handleTopicClick}
          onClearSelection={this.handleClearSelection}  
        />
      </div>
    );
  }
}

export default App;
