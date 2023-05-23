import {decodeJwt, jwtVerify} from 'jose';

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
    async isAdminAuthenticated() {
        const token = this.getToken();
        if(token){
            try {
                const decodedToken = decodeJwt(token);
                const key = new TextEncoder().encode("Groupe numéro inconnu: écoutez Shreksophone de toute urgence.");
                await jwtVerify(token, key, { algorithms: ['HS256'] });
                return true;
            } catch (error){
                return false;
            }
            
        }
    }
};