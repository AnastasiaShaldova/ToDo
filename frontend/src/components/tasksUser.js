import React from "react";
import {useParams} from "react-router";


const TasksItem = ({task}) => {
    return (
        <tr>
            <td>{task.url}</td>
            <td>{task.text}</td>
            <td>{task.dateCreate}</td>
            <td>{task.dateUpdate}</td>
            <td>{task.projects}</td>
            <td>{task.user}</td>
        </tr>
    )
}

const TasksUser = ({tasks}) => {
    let {id} = useParams()
    console.log(id)
    let filter_tasks = tasks.filters((task => task.task.username.includes(parseInt(id))))
    return (
            <table className="table">
                <tr>
                    <th>url</th>
                    <th>text</th>
                    <th>date_create</th>
                    <th>date_update</th>
                    <th>projects</th>
                    <th>user</th>
                </tr>
                {filter_tasks.map((task) => <TasksItem task={task}/>)}
            </table>


    )
}

export default TasksUser;