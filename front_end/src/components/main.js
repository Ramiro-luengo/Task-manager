import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { CookiesProvider } from "react-cookie";

import Home from './home';
import Signup from './signup/signup';
import Login from './login/login';
import Board from './board/board';

const Main = () => {
    return (
        <CookiesProvider>
            <Routes>
                <Route exact path='/' element={<Home />} />
                <Route exact path='/signup' element={<Signup />} />
                <Route exact path='/login' element={<Login />} />
                <Route exact path='/board' element={<Board />} />
            </Routes>
        </CookiesProvider>
    );
}

export default Main;