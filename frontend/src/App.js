import React from "react";
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'usersapp': []
    }
  }

  render() {
    return (
        <div>
          Main App
        </div>
    )
  }
}

export default App;
