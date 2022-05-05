import axios from "axios"


export async function login(auth) {
    return axios.post('/api/token/login/', auth)
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function register(auth) {
    return axios.post('/api/users/', auth)
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function logout() {
    return axios.post('api/token/logout/')
        .then(response => response, (error) => {
            console.log(error);
        });
}
