import axios from "axios"

export async function getCalculator() {
    return axios.get('/api/calculator/')
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function createCalculator(calculator) {
    return axios.post('/api/calculator/', calculator)
        .then(response => response, (error) => {
            console.log(error);
        });
}
