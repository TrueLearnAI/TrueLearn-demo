import React from 'react';
import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import './sidebar.css';


function TopicSidebar({ topics, selectedTopics, onClick, onClearSelection }) {
  const menuItems = topics.map((topic) => {
    const additionalText = topic in selectedTopics? "☑" : "";
    return <MenuItem onClick={() => onClick(topic)}>{`${topic}${additionalText}`}</MenuItem>
  }
  )
  return (
    <Sidebar rtl={true} style={{ height: "100vh" }}>
      <Menu id="menu">
        {menuItems}
        <MenuItem style={{ textAlign: "center" }} onClick={() => onClearSelection()}>X Clear selections X</MenuItem>
      </Menu>
    </Sidebar>
  );
}

export default TopicSidebar;
