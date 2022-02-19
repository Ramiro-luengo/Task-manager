import './board.css';
import TodoItem from './todoItem';

function Folders({ data }) {
    console.log(data);
    const folders = data.folders;
    const todos = data.todoItems;

    return folders.map(
        folder => (
            <div className="trello" >
                <span>{folder.name}</span>
                {
                    todos.filter(todoItem => todoItem.folder === folder.name).map(
                        (todoItem, idx) => <TodoItem key={idx} todoItem={todoItem} />
                    )
                }
            </div>
        )
    )
}

export default Folders;