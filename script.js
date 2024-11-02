document.getElementById("send-button").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    if (message) {
        const chatBox = document.getElementById("chat-box");
        
        // Adiciona a mensagem do usuário ao chat
        chatBox.innerHTML += `<div class="user-message">${message}</div>`;

        // Simula uma resposta da IA
        setTimeout(() => {
            chatBox.innerHTML += `<div class="ai-message">Resposta da IA: ${message}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight; // Rola para baixo
        }, 1000);

        input.value = ""; // Limpa o campo de entrada
    }
}
