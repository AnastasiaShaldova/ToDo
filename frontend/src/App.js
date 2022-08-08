import React from "react";
import './App.css';
import UsersList from "./components/users";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'usersapp': []
    }
  }

  componentDidMount() {
    const usersapp = [
      {
        'username': 'Ivan',
        'first_name': 'Иванов',
        'last_name': 'Иван',
        'email': 'ivan@ivan.ru',
      },
      {
        'username': 'Frodo',
        'first_name': 'Федор',
        'last_name': 'Федоров',
        'email': 'frodo@frodo.ru',
      },
    ]
    this.setState(
        {
          'usersapp': usersapp
        }
    )
  }

  render() {
    return (
        <div>
          <UsersList usersapp={this.state.usersapp}/>
        </div>
    )
  }
}

export default App;
