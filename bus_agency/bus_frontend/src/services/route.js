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

class RouteDataService {
    get(){
        return http.get(`/routes/`);
    }
    get_by_city(){
        return http.get(`/routes/routes_by_city/`);
    }
    update(id, data){
        return http.update(`/routes/${id}/`, data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }

    patch(id, data){
        return http.patch(`/routes/${id}/`, data, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }
    delete(id){
        return http.delete(`/routes/${id}/`, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    }

}

export default new RouteDataService();