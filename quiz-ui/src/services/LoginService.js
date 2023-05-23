// import jwt from 'jsonwebtoken';

export default {
    
    removeToken() {
        window.localStorage.removeItem('jwt_token');
    },
    getToken() {
        return localStorage.getItem('jwt_token');
    },
    saveToken(token) {
        window.localStorage.setItem('jwt_token', token);
    },
    isAdminAuthenticated() {
        const token = this.getToken();
        // if(token){
        //     jwt.verify(token, "Groupe numéro inconnu: écoutez Shreksophone de toute urgence.").then(() => {
        //         return true;
        //     })
        //     .catch(() => {
        //         return false;
        //     });
        // }
    }
};