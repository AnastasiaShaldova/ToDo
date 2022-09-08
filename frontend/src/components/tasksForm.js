import React from "react";

class TaskForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {text: '', users: []}
    }

    handleTaskChange(event) {
        if(!event.target.selectedOptions()){
            this.setState({'users': []})
            return;
        }
        let users = []
        for (let i = 0; i <event.target.selectedOptions.length; i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({'users': users})
    }

    handleSubmit(event) {
        this.props.create_task(this.state.text, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="formGroup">
                    <label htmlFor="text"></label>
                    <input type="text" name="text" placeholder="text"
                           value={this.state.text} onChange={(event) => this.handleChange(event)}/>
                </div>
                <select name="users" multiple onClick={(event) => this.handleTaskChange(event)}>
                    {this.props.users.map((item) => <option value="{item.id}">{item.text}</option>)}
                </select>

                <input type="submit" value="Save"/>
            </form>
        );

    }
}

export default TaskForm