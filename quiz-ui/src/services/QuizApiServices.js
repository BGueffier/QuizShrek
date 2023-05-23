import axios from "axios";
import LoginService from "./LoginService";
const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = LoginService.getToken()) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  async getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", `/questions?position=${position}`);
  },
  async pushScore(playerName, answers){
    return this.call("post", "/participations", {playerName: playerName, answers: answers});
  },
  async login(password){
    return this.call("post", "/login", {password: password});
  },
  async deleteQuestion(id) {
    return this.call("delete", `/questions/${id}`);
  },
  async pushQuestion(title, text, position, image, possibleAnswers) {
    return this.call("post", "/questions", {title: title, text: text, position: position, image: image, possibleAnswers: possibleAnswers});
  },
  async updateQuestion(id,title, text, position, image, possibleAnswers) {
    return this.call("put", `/questions/${id}`, {title: title, text: text, position: position, image: image, possibleAnswers: possibleAnswers});
  }
};