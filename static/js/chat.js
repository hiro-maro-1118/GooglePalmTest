document.addEventListener("DOMContentLoaded", function() {
  var chatLog = document.getElementById("chat-log");
  var userInput = document.getElementById("user-input");
  var sendButton = document.getElementById("send-button");

  sendButton.addEventListener("click", sendMessage);
  userInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  });

  // function sendMessage() {
  //   var userMessage = userInput.value;
  //   if (userMessage.trim() === "") {
  //     return;
  //   }

  //   appendMessage("User", userMessage);
  //   userInput.value = "";

  //   // Send user message to the backend for processing
  //   // and receive a response from the ChatGPT model
  //   // You'll need to implement this part based on your backend setup

  //   // Example code to receive a response from the backend
  //   var botResponse = "This is a sample response from the bot.\n";
  //   appendMessage("Bot", botResponse);
  // }

  function sendMessage() {
    var userMessage = userInput.value;
    if (userMessage.trim() === "") {
      return;
    }
  
    appendMessage("User", userMessage);
    userInput.value = "";
  
    // Send user message to the backend for processing
    // and receive a response from the ChatGPT model
    // You'll need to implement this part based on your backend setup
  
    // Example code to receive a response from the backend
    fetch('/process_message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userMessage }),
    })
      .then(response => response.json())
      .then(data => {
        var botResponse = data.response;
        appendMessage("Bot", botResponse);
        chatLog.scrollTop = chatLog.scrollHeight;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  function appendMessage(sender, message) {
    var messageContainer = document.createElement("div");
    var messageElement = document.createElement("div");
    messageElement.innerHTML = "[" + sender + "] " + message.replace(/\n/g, "<br>");
    messageContainer.appendChild(messageElement);
    messageContainer.classList.add(sender.toLowerCase() + "-message");
    chatLog.appendChild(messageContainer);
    chatLog.scrollTop = chatLog.scrollHeight;
  }
});
