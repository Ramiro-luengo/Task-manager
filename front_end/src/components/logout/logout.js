import axios from "axios";
axios.defaults.withCredentials = true;

async function Logout() {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/logout/`
    const res = await axios.post(url)
    console.log(res.message)
}

export default Logout;