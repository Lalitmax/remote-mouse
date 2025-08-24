import websocket, json, pyautogui

def on_message(ws, message):
    try:
        event = json.loads(message)
        if event["type"] == "mousemove":
            screen_width, screen_height = pyautogui.size()
            x = int(event["x"] * screen_width)
            y = int(event["y"] * screen_height)
            pyautogui.moveTo(x, y)
        elif event["type"] == "click":
            pyautogui.click()
        elif event["type"] == "keypress":
            pyautogui.write(event["key"])
    except Exception as e:
        print("Error handling event:", e)

def on_error(ws, error):
    print("WebSocket Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")

def on_open(ws):
    print("Connected to server, waiting for events...")

if __name__ == "__main__":
    # Replace with your backend server's public IP/domain
    ws = websocket.WebSocketApp(
        "ws://YOUR_SERVER_IP:8080",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
