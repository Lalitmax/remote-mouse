const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });
console.log("✅ WebSocket server running on ws://0.0.0.0:8080");

wss.on("connection", (ws) => {
  console.log("New client connected");

  ws.on("message", (message) => {
    // Broadcast to all connected clients
    wss.clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  ws.on("close", () => {
    console.log("Client disconnected");
  });
});
