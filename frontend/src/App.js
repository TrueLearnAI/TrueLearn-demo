import React from 'react';
import VisualisationSidebar from './components/VisualisationSidebar';
import Window from './components/Window';
import TopicSidebar from './components/TopicSidebar';

import './App.css';


class App extends React.Component {
  constructor() {
    super();
    this.state = {
      currentVisualisations: null,
      topics: [],
      selectedTopics: []
    };
    
    this.handleVizClick = this.handleVizClick.bind(this);
    this.handleTopicClick = this.handleTopicClick.bind(this);
    this.handleClearSelection = this.handleClearSelection.bind(this);
  }

  handleVizClick(visualisationClicked) {
    this.setState({
      currentVisualisations: visualisationClicked
    });
  }

  handleTopicClick(topicClicked) {
    this.setState({
      selectedTopics: this.state.selectedTopics.concat(topicClicked)
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
        <VisualisationSidebar onClick={this.handleVizClick} />
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
