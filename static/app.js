const form = document.querySelector("#prediction-form");
const button = document.querySelector("#submit-button");
const resultPanel = document.querySelector("#result-panel");
const predictionValue = document.querySelector("#prediction-value");
const passProbability = document.querySelector("#pass-probability");
const failProbability = document.querySelector("#fail-probability");
const riskBadge = document.querySelector("#risk-badge");
const explanationContent = document.querySelector("#explanation-content");
const recommendationsContent = document.querySelector("#recommendations-content");
const studyPlanContent = document.querySelector("#study-plan-content");
const encouragementContent = document.querySelector("#encouragement-content");
const chatForm = document.querySelector("#chat-form");
const chatInput = document.querySelector("#chat-input");
const chatButton = document.querySelector("#chat-button");
const chatMessages = document.querySelector("#chat-messages");
const chatHistory = [];

function renderList(element, items) {
    element.replaceChildren();
    items.forEach((item) => {
        const listItem = document.createElement("li");
        listItem.textContent = item;
        element.appendChild(listItem);
    });
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(form));
    button.disabled = true;
    button.innerHTML = "Generating outlook...";

    try {
        const response = await fetch("/api/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "Unable to generate a prediction.");

        predictionValue.textContent = data.prediction;
        passProbability.textContent = `${data.pass_probability}%`;
        failProbability.textContent = `${data.fail_probability}%`;
        riskBadge.textContent = `${data.risk_level} risk`;
        riskBadge.className = `risk-badge ${data.risk_level.toLowerCase()}`;
        explanationContent.textContent = data.support.explanation;
        renderList(recommendationsContent, data.support.recommendations);
        renderList(studyPlanContent, data.support.study_plan);
        encouragementContent.textContent = data.support.encouragement;
        resultPanel.classList.remove("is-hidden");
        resultPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } catch (error) {
        window.alert(error.message);
    } finally {
        button.disabled = false;
        button.innerHTML = "Generate prediction <span>→</span>";
    }
});

function addChatMessage(content, role) {
    const message = document.createElement("div");
    message.className = `message ${role}-message`;
    message.textContent = content;
    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return message;
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = chatInput.value.trim();
    if (!message) return;

    addChatMessage(message, "user");
    chatHistory.push({ role: "user", content: message });
    chatInput.value = "";
    chatInput.disabled = true;
    chatButton.disabled = true;
    chatButton.textContent = "Sending...";

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message, history: chatHistory.slice(0, -1) })
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "Unable to send your question.");
        addChatMessage(data.reply, "assistant");
        chatHistory.push({ role: "assistant", content: data.reply });
    } catch (error) {
        addChatMessage(error.message, "assistant");
    } finally {
        chatInput.disabled = false;
        chatButton.disabled = false;
        chatButton.innerHTML = "Send <span>↑</span>";
        chatInput.focus();
    }
});
