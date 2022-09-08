import React from "react";
// import {useParams} from "react-router";


const TasksItem = ({task}) => {
    return (
        <tr>
            <td>{task.id}</td>
            <td>{task.text}</td>
            <td>{task.date_create}</td>
            <td>{task.projects}</td>
            <td>{task.user}</td>
        </tr>
    )
}

const TasksUser = ({tasks}) => {
    // let {id} = useParams()
    // console.log(id)
    // let filter_tasks = tasks.filters((task => task.task.username.includes(parseInt(id))))
    return (
        <table className="table">
            <tr>
                <th>id</th>
                <th>text</th>
                <th>date_create</th>
                <th>projects</th>
                <th>user</th>
            </tr>
            {tasks.map((task) => <TasksItem task={task}/>)}
        </table>


    )
}

export default TasksUser;