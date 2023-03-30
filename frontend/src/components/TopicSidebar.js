import React from 'react';
import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import './sidebar.css';


function TopicSidebar({ topics, selectedTopics, onClick, onClearSelection }) {
  let menuItems = topics.map((topic) => {
    const additionalText = selectedTopics.includes(topic) ? "☑" : "";
    return <MenuItem onClick={() => onClick(topic)}>{`${additionalText} ${topic}`}</MenuItem>
  }
  )
  return (
    <Sidebar rtl={true} style={{ height: "100vh" }}>
      <Menu id="menu">
        {menuItems}
        <MenuItem style={{ textAlign: "center" }} onClick={() => onClearSelection()}>
          <b>✗ Clear selections ✗</b>
        </MenuItem>
      </Menu>
    </Sidebar>
  );
}

export default TopicSidebar;
