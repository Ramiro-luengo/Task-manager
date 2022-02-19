import './board.css';

function TodoItem({ todoItem }) {
    return (
        <div className="trello__list__item">
            <span className='trello__list__title'>{todoItem.name}</span>
            <span>{todoItem.description ? `Description: ${todoItem.description}` : ""}</span>
            <span className="highlighted">CSS</span>
        </div>
    )
}
export default TodoItem;