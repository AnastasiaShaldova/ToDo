import React from "react";
import './App.css';
import AppHeader from "./components/header";
import UsersList from "./components/user";
import TasksList from "./components/tasks";
import TasksUser from "./components/tasksUser";
import AppFooter from "./components/footer";
import NotFound404 from "./components/NotFound404";
import axios from "axios";
import {BrowserRouter, Route, Routes, Navigate, NavLink} from 'react-router-dom';



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'tasks': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users').then(response => {
            console.log(response.data)
            this.setState(
                {
                    'users': response.data
                }
            )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/tasks').then(response => {
            console.log(response.data)
            this.setState(
                {
                    'tasks': response.data.results
                }
            )
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <BrowserRouter>
                    <NavLink to='/'>Главная</NavLink>
                    <NavLink to='/users'>Пользователи</NavLink>
                    <NavLink to='/tasks'>Записки</NavLink>
                <Routes>
                    <Route path="/" element={<AppHeader header={this.state.header}/>}></Route>
                    <Route path="/" element={<AppFooter footer={this.state.footer}/>}></Route>
                    <Route path="/users" element={<UsersList users={this.state.users}/>}></Route>
                    <Route path="/tasks" element={<TasksList tasks={this.state.tasks}/>}></Route>
                    <Route path='/users/:user'><TasksUser users={this.state.users}/></Route>
                    <Route path="/task" element={<Navigate to='/tasks'/>}></Route>
                    <Route path="/*" element={<NotFound404/>}></Route>
                </Routes>
            </BrowserRouter>
        )
    }
}

export default App;
