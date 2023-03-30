import React from 'react';
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
      currentVisualisation: "line",
      topics: [],
      selectedTopics: []
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
        })
      })
      .catch(error => {
        console.log(error);
      });
  }

  handleVizClick(visualisationClicked) {
    this.setState({
      currentVisualisation: visualisationClicked
    });
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
    this.setState({
      selectedTopics: newTopics
    })
  }

  handleClearSelection() {
    this.setState({
      selectedTopics: []
    })
  }

  render() {
    return (
      <div id="app" style={({ height: "100vh" }, { display: "flex", justifyContent: "space-between" })}>
        <VisualisationSidebar
          currentVisualisation={this.state.currentVisualisation}
          onClick={this.handleVizClick}
        />
        <Window></Window>
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
