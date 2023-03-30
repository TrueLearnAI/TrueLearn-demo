import React from 'react';
import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import './sidebar.css';

function VisualisationSidebar({ onClick }) {
  return (
    <Sidebar style={{ height: "100vh" }}>
      <Menu id="menu">
        <MenuItem onClick={() => onClick("line")}>Line chart</MenuItem>
        <MenuItem onClick={() => onClick("pie")}>Pie chart</MenuItem>
        <MenuItem onClick={() => onClick("rose")}>Rose chart</MenuItem>
        <MenuItem onClick={() => onClick("bar")}>Bar chart</MenuItem>
        <MenuItem onClick={() => onClick("dot")}>Dot chart</MenuItem>
        <MenuItem onClick={() => onClick("bubble")}>Bubble chart</MenuItem>
        <MenuItem onClick={() => onClick("radar")}>Radar chart</MenuItem>
        <MenuItem onClick={() => onClick("word")}>Wordcloud</MenuItem>
        <MenuItem onClick={() => onClick("tree")}>Treemap</MenuItem>
      </Menu>
    </Sidebar>
  );
}

export default VisualisationSidebar;
