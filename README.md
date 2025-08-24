# Remote Mouse Control

A minimal system to control a target computer’s mouse and keyboard remotely using a web browser.

---

## Features
- Control mouse movement and clicks from a browser.
- Send keyboard input from browser to target machine.
- Works over LAN or via public server.
- Simple setup with separate backend, frontend, and agent.

---

## Components
1. **Agent (`agent.py` / `agent.exe`)**  
   - Runs on the target machine.  
   - Connects to the backend server and executes mouse/keyboard events.

2. **Backend Server (`server.js`)**  
   - Node.js WebSocket server.  
   - Relays events between the controller (browser) and the agent.

3. **Frontend (`index.html`)**  
   - Browser page to capture mouse and keyboard input.  
   - Sends events to the backend server.

---

