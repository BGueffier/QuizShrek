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
        if(token){
            try {
                const decodedToken = jwt.verify(token);
                return true;
            } catch(error) {
                this.removeToken();
                return false;
            }
        }
    }
};