import http from "../http-common";

class TripDataService {
    get() {
        return http.get("/trips/");
    }
}

export default new TripDataService();