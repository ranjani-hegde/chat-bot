from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from typing import Dict
from models.room import init_db, save_message, get_messages
import shutil
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Create uploads folder
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

init_db()

class ConnectionManager:
    def __init__(self):
        self.rooms: Dict[str, Dict] = {}

    async def connect(self, websocket: WebSocket, room: str, username: str):
        await websocket.accept()
        if room not in self.rooms:
            self.rooms[room] = {}
        self.rooms[room][websocket] = username

    def disconnect(self, websocket: WebSocket, room: str):
        if room in self.rooms:
            self.rooms[room].pop(websocket, None)

    def get_users(self, room: str):
        if room in self.rooms:
            return list(self.rooms[room].values())
        return []

    async def broadcast(self, message: str, room: str):
        if room in self.rooms:
            for connection in list(self.rooms[room].keys()):
                await connection.send_text(message)

    async def broadcast_users(self, room: str):
        users = self.get_users(room)
        if room in self.rooms:
            for connection in list(self.rooms[room].keys()):
                await connection.send_text(f"__users__:{','.join(users)}")

manager = ConnectionManager()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/chat")
def chat(request: Request, username: str, room: str):
    return templates.TemplateResponse(request=request, name="chat.html", context={"username": username, "room": room})

@app.get("/history/{room}")
def history(room: str):
    messages = get_messages(room)
    return [
        {"username": row[0], "message": row[1], "timestamp": row[2]}
        for row in messages
    ]

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return JSONResponse({"url": f"/uploads/{file.filename}", "filename": file.filename, "type": file.content_type})

@app.websocket("/ws/{room}/{username}")
async def websocket_endpoint(websocket: WebSocket, room: str, username: str):
    await manager.connect(websocket, room, username)
    await manager.broadcast(f"🟢 {username} joined the room!", room)
    await manager.broadcast_users(room)
    try:
        while True:
            data = await websocket.receive_text()
            save_message(room, username, data)
            await manager.broadcast(f"{username}: {data}", room)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room)
        await manager.broadcast(f"🔴 {username} left the room.", room)
        await manager.broadcast_users(room)