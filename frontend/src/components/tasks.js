import React from "react";


const TasksItem = ({task, delete_tasks}) => {
    return (
        <table className="table">
            <tr>
                <td>{task.id}</td>
                <td>{task.url}</td>
                <td>{task.text}</td>
                <td>{task.date_create}</td>
                <td>{task.date_update}</td>
                <td>{task.projects}</td>
                <td>{task.users}</td>
                <td>
                    <button onClick={()=>delete_tasks(task)} type='button'>Delete</button>
                </td>
            </tr>
        </table>
    )
}

const TasksList = ({tasks, delete_tasks}) => {
    return (
        <table className="table">
            <tfoot>
            <tr>
                <th>id</th>
                <th>url</th>
                <th>text</th>
                <th>date_create</th>
                <th>date_update</th>
                <th>projects</th>
                <th>user</th>
            </tr>
            {tasks.map((task) => <TasksItem task={task} delete_tasks={delete_tasks}/>)}
            </tfoot>
        </table>


    )
}

export default TasksList;

