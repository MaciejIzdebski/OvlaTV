import axios from 'axios'
import { useAppStore } from '@/store/app'
export default {
    install: (app, options) => {
        let ax = axios.create({
            baseURL: options.baseUrl
        })

        ax.interceptors.request.use(function (config) {
            let appStore = useAppStore()
            config.headers.Authorization = `Bearer ${appStore.token.access}`
            return config;
          }, function (error) {
            // Do something with request error
            return Promise.reject(error);
          });

        app.config.globalProperties.$axios = ax;
        app.provide('axios', ax);
    }
}