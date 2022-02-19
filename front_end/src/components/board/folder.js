import './board.css';
import TodoItem from './todoItem';

function Folders({ data }) {
    console.log(data);
    const folders = data.folders;
    const todos = data.todoItems;

    return folders.map(
        (folder, idx) => (
            <div key={idx} className="trello" >
                <span className='trello_folder_title'>{folder.name}</span>
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