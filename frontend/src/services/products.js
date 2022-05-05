import axios from "axios"

export async function getProducts() {
    return axios.get('/api/products/')
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function createProduct(products) {
    return axios.post('/api/products/', products)
        .then(response => response, (error) => {
            console.log(error);
        });
}
export async function deleteProduct(product_id) {
    return axios.delete('/api/products/' + product_id)
        .then(response => response, (error) => {
            console.log(error);
        });
}

