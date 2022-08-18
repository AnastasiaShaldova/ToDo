import React from "react";
import './footer.css'

const FooterList = () => {
    return (
        <article>
            <footer>
                <h1>&copy;{new Date().getFullYear()} Сервис для заметок</h1>
            </footer>
        </article>
    )
}

export default FooterList;