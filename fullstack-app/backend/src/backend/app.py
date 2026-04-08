from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(
    title="API Praktikum RSI Kelompok 2",
    description="Dokumentasi API untuk tugas CRUD"
)

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    whatsapp: str
    created_at: str
    updated_at: str

class UserInput(BaseModel):
    first_name: str
    last_name: str
    whatsapp: str
    
class UserUpdate(BaseModel):
    id: int
    first_name: str
    last_name: str
    whatsapp: str

database_user = {}
id_iterator = 0

@app.get("/")
def read_root():
    return {"message": "Server Backend Sedang Berjalan Cuyy!"}

@app.post("/tambah_user")
def tambah_mahasiswa(data_user: UserInput):
    global id_iterator
    while True:
        if id_iterator not in database_user:
            data_baru = User(
                id=id_iterator,
                first_name=data_user.first_name,
                last_name=data_user.last_name,
                whatsapp=data_user.whatsapp,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            
            database_user[id_iterator] = data_baru
            id_iterator += 1 
            return {
                "message": "Data berhasil ditambahkan",
                "data": data_baru
            }
        else:
            id_iterator += 1
            continue
        
@app.put("/edit_user")
def edit_mahasiswa(data_user: UserUpdate):
    if data_user.id in database_user :
        data_lama = database_user[data_user.id]
        data_baru = User(
                id=data_user.id,
                first_name=data_user.first_name,
                last_name=data_user.last_name,
                whatsapp=data_user.whatsapp,
                created_at=data_user.created_at,
                updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        database_user[data_user.id] = data_baru
        return {"message": "Data diubah!", "data lama": data_lama, "data baru" : data_baru}
    else :
        return {"message": "Tidak ada id tersebut di dalam Database User", "id": data_user.id}
    
@app.delete("/hapus_mahasiswa")
def hapus_mahasiswa(id_input : int):
    if id_input in database_user :
        data_dihapus = database_user[id_input]
        del database_user[id_input]
        return {"message": "Data dihapus!", "data": data_dihapus}
    else :
        return {"message": "Tidak ada id tersebut di dalam Database User", "id": id_input}