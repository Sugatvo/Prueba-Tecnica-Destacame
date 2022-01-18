import http from "../http-common";

class TripDataService {
    get_departure_cities() {
        return http.get("/routes/departure_cities/");
    }
    get_arrival_cities(id) {
        return http.get(`/routes/arrival_cities/?from_station=${id}`)
    }
    get_trips(departure_date, from_station, to_station){
        return http.get(`/trips/?departure_date=${departure_date}&arrival_date=&route__from_station=${from_station}&route__to_station=${to_station}`)
    }
}

export default new TripDataService();