import http from "../http-common";

class AuthenticationService {
  getCSRF() {
    return http.get("/csrf/");
  }
  getSession() {
    return http.get("/session/");
  }

  whoami() {
    return http.get("/whoami/")
  }
}

export default new AuthenticationService();