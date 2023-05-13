export default {
    clear() {
        // todo : implement
    },
    savePlayerName(playerName) {
        window.localStorage.setItem("playerName", playerName);
    },
    getPlayerName() {
        const result = window.localStorage.getItem("playerName");
        return result == null ? "" : result;
    },
    saveScore(score) {
        window.localStorage.setItem("playerScore", score);
    },
    getScore() {
        const result = window.localStorage.getItem("playerScore");
        return result == null ? "0" : result;
    },
    clearScore() {
        if(window.localStorage.getItem("playerScore") != null)
            window.localStorage.removeItem("playerScore");
    },
};