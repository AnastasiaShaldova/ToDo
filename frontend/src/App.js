import React from "react";
import './App.css';
import UsersList from "./components/user";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'usersapp': []
    }
  }

  componentDidMount() {
    const users = [
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
          'usersapp': users
        }
    )
  }

  render() {
    return (
        <div>
          <UsersList users={this.state.usersapp}/>
        </div>
    )
  }
}

export default App;
