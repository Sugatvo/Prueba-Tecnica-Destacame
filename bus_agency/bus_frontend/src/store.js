import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        csrf: "",
        isAuthenticated: false,
        username: "",
        id: ""
    }
})