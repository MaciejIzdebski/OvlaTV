import axios from 'axios'

export default {
    install: (app, options) => {
        let ax = axios.create({
            baseURL: options.baseUrl,
            headers: {
                Authorization: options.token ? `Bearer ${options.token}` : '',
            }
        })
        app.config.globalProperties.$axios = ax;
        app.provide('axios', ax);
    }
}