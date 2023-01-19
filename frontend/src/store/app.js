// Utilities
import { defineStore } from 'pinia'
import jwt_decode from 'jwt-decode'

export const useAppStore = defineStore('app', {
  state: () => ({
    token: {
      refresh: undefined,
      access: undefined
    }
  }),
  getters: {
    user_id: (state) => {
      if(state.token.access != undefined) return jwt_decode(state.token.access).user_id;
      else return undefined;
    }
  }
})
