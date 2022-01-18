import http from "../http-common";

class UserDataService {
    login(username, password, token) {
        let data = JSON.stringify({
            username: username,
            password: password
        })
        return http.post("/login/", data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            }
        });
    }
    logout() {
        return http.get("/logout/");
    }
}

export default new UserDataService();