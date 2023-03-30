import React from 'react';
import Plot from 'react-plotly.js';

class Window extends React.Component {
  render() {
    let visualisation = this.props.visualisation;
    if (visualisation === null) {
      return <></>
    }
    return (
      <Plot style={{ width: "100%" }} data={visualisation.data} layout={visualisation.layout}/>
    )
  }
}

export default Window;