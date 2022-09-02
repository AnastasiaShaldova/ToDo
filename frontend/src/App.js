import React from "react";
import './App.css';
import AppHeader from "./components/header";
import UsersList from "./components/user";
import TasksList from "./components/tasks";
import TasksUser from "./components/tasksUser";
import AppFooter from "./components/footer";
import NotFound404 from "./components/NotFound404";
import LoginForm from "./Auth";
import axios from "axios";
import Cookies from "universal-cookie";
import {BrowserRouter, Route, Routes, Navigate, NavLink} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'tasks': [],
            'token': '',
        }
    }

    logout() {
        this.set_token('')
    }

    is_auth(){
        return !!this.state.token
    }
    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
        console.log(this.state.token)
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        const data = {username: username, password: password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data)
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users', {headers}).then(response => {
            console.log(response.data)
            this.setState(
                {
                    'users': response.data
                }
            )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/tasks', {headers}).then(response => {
            console.log(response.data)
            this.setState(
                {
                    'tasks': response.data.results
                }
            )
        }).catch(error => console.log(error))
    }

    get_headers() {
        let headers = {
            'Content-Type':'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <BrowserRouter>
                <NavLink to='/'>Главная</NavLink>
                <NavLink to='/users'>Пользователи</NavLink>
                <NavLink to='/tasks'>Записки</NavLink>
                {this.is_auth() ? <button onClick={() => this.logout()}>Выйти</button> : <NavLink to='/login'>Войти</NavLink>}
                <Routes>
                    <Route path="/" element={<AppHeader header={this.state.header}/>}></Route>
                    <Route path="/" element={<AppFooter footer={this.state.footer}/>}></Route>
                    <Route path="/users" element={<UsersList users={this.state.users}/>}></Route>
                    <Route path="/tasks" element={<TasksList tasks={this.state.tasks}/>}></Route>
                    <Route path="/login" element={
                        <LoginForm get_token={(username, password) => this.get_token(username, password)}/>}></Route>
                    <Route path='/users/:user' element={<TasksUser users={this.state.users}/>}></Route>
                    <Route path="/task" element={<Navigate to='/tasks'/>}></Route>
                    <Route path="/*" element={<NotFound404/>}></Route>
                </Routes>
            </BrowserRouter>
        )
    }
}

export default App;
