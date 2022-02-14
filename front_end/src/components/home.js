import { Link } from 'react-router-dom';

function Home() {
    return (
        <div>
            <p>Home is a nice place</p>
            <Link to='/login'>Login</Link>
        </div>
    );
}

export default Home;