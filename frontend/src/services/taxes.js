import axios from "axios"

export async function getTaxes() {
    return axios.get('/api/taxes/')
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function createTax(tax) {
    return axios.post('/api/taxes/', tax)
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function deleteTax(tax_id) {
    return axios.delete('/api/taxes/' + tax_id)
        .then(response => response, (error) => {
            console.log(error);
        });
}

