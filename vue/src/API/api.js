import Axios from 'axios'

const axios = Axios.create({
    baseURL: 'http://localhost:5000',
})

export default class API {
    static async  getData() {
        const resp = await axios.post('/api/data')
        return resp.data
    }

    static async  addData(id) {
        const resp = await axios.get(`/api/data/${id}`)
        return resp.data
    }
}