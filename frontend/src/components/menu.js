import React from "react";
import './menu.css'

const MenuList = () => {
    return (
        <article>
            <div className='menu'>
                <ul id="navbar">
                    <a href="#">Заметки</a>
                    <a href="#">Личный кабинет</a>
                </ul>
            </div>
        </article>

    )
}

export default MenuList;