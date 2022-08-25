import React from "react";
import {NavLink} from "react-router-dom";


const UserItem = ({user}) => {
    return (
        <thead>
        <tr>
            <td><NavLink to={`/user/${user.id}`}>{user.username}</NavLink></td>
            <td>{user.firstName}</td>
            <td>{user.lastName}</td>
            <td>{user.email}</td>
        </tr>
        </thead>
    )
}

const UsersList = ({users}) => {
    return (
        <table className="table">
            <tfoot>
            <tr>
                <th>username</th>
                <th>first_name</th>
                <th>last_name</th>
                <th>email</th>
            </tr>
            </tfoot>
            {users.map((user) => <UserItem user={user}/>)}

        </table>
    )
}

export default UsersList;