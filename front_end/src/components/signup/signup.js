import { Link } from 'react-router-dom';

import './signup.css';
import logo from './logo.png';

function SingUp() {
    return (
        <div className="container">
            <div className="card">
                <form action="" method="" className="main active">
                    <div className="top-div">
                        <div className="msg-img">
                            <img src={logo} />
                            <h3>Trello2.0</h3>
                        </div>
                        <h2>Sign Up</h2>
                        <p>Basic Details</p>
                    </div>
                    <div className="input-text">
                        <input type="text" placeholder="Username" require id="f_name" />
                    </div>
                    <div className="input-text">
                        <input type="text" placeholder="Email" require />
                    </div>
                    <div className="input-text">
                        <input type="password" placeholder="Password" require />
                    </div>
                    <div className="input-text">
                        <input type="password" placeholder="Confirm Password" require />
                    </div>
                    <div className="buttons">
                        <button className="next-btn">Next</button>
                    </div>
                </form>
                <div className="sign-in2">
                    <p>Already have an account?
                        <Link to="/login"> Sign in</Link>
                    </p>
                </div>
            </div>
        </div>
    );
}

export default SingUp;