import axios from 'axios';
import React, { useEffect, useState } from "react";
import { css } from "@emotion/react";
import RotateLoader from 'react-spinners/RotateLoader';

import './board.css'
import Folders from './folder.js';

axios.defaults.withCredentials = true;
const override = css`
  display: flex;
  margin: 0 auto;
  border-color: red;
`;

async function fetchBoard() {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/board/`;
    const response = await axios.get(url);
    return await response.data;
}

function Board() {
    const [bodyStr, setBodyStr] = useState("");
    useEffect(() => {
        let isMounted = true;
        const getCards = async () => {
            const cards = await fetchBoard();
            setBodyStr(cards);
        }
        getCards();
        return () => { isMounted = false };
    }, []);

    return bodyStr ? (
        <div className="board_container">
            <Folders data={bodyStr} />
        </div>) :
        <RotateLoader loading={bodyStr} css={override} size={150} />
}

export default Board;
