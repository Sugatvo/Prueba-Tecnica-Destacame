import http from "../http-common";

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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
    register(firstname, lastname, username, email, password) {
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

    whoami() {
        return http.get("/whoami/");
    }

    change_password(id, data) {
        return http.put(`/change_password/${id}/`, data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }
}

export default new UserDataService();