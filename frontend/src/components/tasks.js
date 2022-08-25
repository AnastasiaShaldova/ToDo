import React from "react";


const TasksItem = ({task}) => {
    return (
        <table className="table">
            <tr>
                <td>{task.id}</td>
                <td>{task.url}</td>
                <td>{task.text}</td>
                <td>{task.dateCreate}</td>
                <td>{task.dateUpdate}</td>
                <td>{task.projects}</td>
                <td>{task.user}</td>
            </tr>
        </table>
    )
}

const TasksList = ({tasks}) => {
    return (
        <table className="table">
            <tfoot>
            <tr>
                <th>url</th>
                <th>text</th>
                <th>date_create</th>
                <th>date_update</th>
                <th>projects</th>
                <th>user</th>
            </tr>
            {tasks.map((task) => <TasksItem task={task}/>)}
            </tfoot>
        </table>


    )
}

export default TasksList;

