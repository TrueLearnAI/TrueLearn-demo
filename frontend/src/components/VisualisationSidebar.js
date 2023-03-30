import React from 'react';
import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import './sidebar.css';

function VisualisationSidebar({ onClick, currentVisualisation }) {
  let topicArr = ["line", "pie", "rose", "bar", "dot", "bubble", "radar", "word", "tree"];
  let menuItems = topicArr.map(topic => {
    let additionalText = topic === currentVisualisation ? "☑" : "";
    return (
      <MenuItem onClick={() => onClick(topic)}>
        {`${additionalText} ${topic.charAt(0).toUpperCase() + topic.slice(1)} chart`}
      </MenuItem>
    )
  })
  return (
    <Sidebar style={{ height: "100vh" }}>
      <Menu id="menu">
        {menuItems}
      </Menu>
    </Sidebar>
  );
}

export default VisualisationSidebar;
