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

class DriverDataService {
    get(){
        return http.get(`/drivers/`);
    }
    update(id, data){
        return http.update(`/drivers/${id}/`, data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }

    patch(id, data){
        return http.patch(`/drivers/${id}/`, data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }
    delete(id){
        return http.delete(`/drivers/${id}/`, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }

    post(firstname, lastname, username, email, password) {
        let data = {
            "username": username,
            "first_name": firstname,
            "last_name": lastname,
            "email": email,
            "password": password
        }

        return http.post("/drivers/", data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }

}

export default new DriverDataService();