import axios from 'axios';
import { useSearchParams } from 'react-router-dom';

import './board.css'

axios.defaults.withCredentials = true;

async function fetchBoard() {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/board/`;
    return await axios.get(url);
}

function Board() {
    const [searchParams, _] = useSearchParams();
    const username = searchParams.get('username') || '';
    const board_data = fetchBoard();

    return (
        <div className="board_container">
            <div className="trello">
                <div className="trello__list">
                    <span>Title</span>
                    <div className="trello__list__item">
                        <span>CSS is so good.</span>
                        <span className="highlighted">CSS</span>
                    </div>
                    <div className="trello__list__item">
                        <span>GFG is great site to learn new things.</span>
                        <span className="highlighted">GFG</span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Board;
