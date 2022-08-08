import React from "react";
import './App.css';
import UsersList from "./components/user";
import FooterList from "./components/footer";
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
  }

  render() {
    return (
        <div>
          <UsersList users={this.state.usersapp}/>
          <FooterList footer={this.state.footer}/>
        </div>
    )
  }
}

export default App;
