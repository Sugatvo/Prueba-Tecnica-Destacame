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
    register(firstname, lastname, username, email, password){
        let data = {
            "username": username,
            "first_name": firstname,
            "last_name": lastname,
            "email": email,
            "password": password
        }

        return http.post("/passengers/", data, {
            headers: {
                "Content-Type": "application/json",
            }
        });
    }


}

export default new UserDataService();