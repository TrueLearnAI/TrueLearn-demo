import React from 'react';
import Plot from 'react-plotly.js';

class Window extends React.Component {
  render() {
    let currentVisualisation = this.props.currentVisualisation;
    let visualisation = this.props.visualisation;
    if (visualisation === null) {
      return <></>
    }
    let statics = ['bubble', 'word', 'radish'];
    if (statics.includes(currentVisualisation)) {
      return (
        <img style={{ width: "100%", maxHeight: "100vh" }} src={visualisation} alt={currentVisualisation} />
      )
    }
    return (
      <Plot style={{ width: "100%", maxHeight: "100vh" }} data={visualisation.data} layout={visualisation.layout}/>
    )
  }
}

export default Window;