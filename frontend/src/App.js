import React from "react";
import './App.css';
import UsersList from "./components/user";
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'usersapp': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/').then(response => {
      this.setState(
        {
          'usersapp': response.data
        }
    )
    }).catch(error => console.log(error))
    // const users = [
    //   {
    //     'username': 'Ivan',
    //     'first_name': 'Иванов',
    //     'last_name': 'Иван',
    //     'email': 'ivan@ivan.ru',
    //   },
    //   {
    //     'username': 'Frodo',
    //     'first_name': 'Федор',
    //     'last_name': 'Федоров',
    //     'email': 'frodo@frodo.ru',
    //   },
    // ]

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
