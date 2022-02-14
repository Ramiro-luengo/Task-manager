import axios from "axios";
import React, { useState } from "react";
import { Link, useNavigate } from 'react-router-dom';
import { useCookies } from "react-cookie";

import './login.css';
import logo from '../signup/logo.png';


function Login() {
    const [errorMessage, setErrorMessage] = useState('');
    const [cookies, _] = useCookies();
    axios.defaults.headers["X-CSRFToken"] = cookies.csrftoken;

    let redirect = useNavigate();

    async function handleSubmit(event) {
        event.preventDefault();

        const url = `${process.env.REACT_APP_BACKEND_URL}/api/login/`;
        const username = event.target.username.value
        const password = event.target.password.value

        const data = {
            username: username,
            password: password
        };
        const res = await axios.post(url, data, { withCredentials: true }).catch(
            err => {
                return err.response.data;
            });
        if (res.status === 200) {
            // Backend authenticated successfully
            return redirect(`/board?username=${username}`)
        } else {
            // Backend authentication failed
            // Display error message
            setErrorMessage(res.message.flat()[0]);
        }
    }

    return (
        <div className="container">
            <div className="card">
                <form onSubmit={handleSubmit} className="main active">
                    <div className="top-div">
                        <div className="msg-img">
                            <img src={logo} />
                            <h3>Trello2.0</h3>
                        </div>
                    </div>
                    <div className="align_center">
                        <div className="input-text">
                            <input type="text" name="username" placeholder="Username or Email" require="true" id="f_name" />
                        </div>
                        <div className="input-text">
                            <input type="password" name="password" placeholder="Password" require="true" />
                        </div>
                        <div className="buttons">
                            <button type="submit" className="next-btn">Sign in</button>
                        </div>
                        {errorMessage && <div className="error"> {errorMessage} </div>}
                    </div>
                </form>
                <div className="sign-in">
                    <p>Don't have an account?
                        <Link to="/signup"> Sign up</Link>
                    </p>
                </div>
            </div >
        </div >
    );
}

export default Login;