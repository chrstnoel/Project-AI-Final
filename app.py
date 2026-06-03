from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io

try:
    from logic import hitung_kompos 
    print("File logic.py berhasil disambungkan!")
except ImportError:
    print("File logic.py ditemukan, tapi fungsi 'hitung_kompos' belum ada atau berbeda nama.")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

try:
    model = YOLO("best.pt")
    print("🔥 Otak AI YOLO Berhasil Dimuat!")
except Exception as e:
    print(f"❌ Gagal memuat file best.pt. Pastikan file 'best.pt' sudah kamu copas ke folder yang sama! Error: {e}")

@app.post("/api/scan-kompos")
async def scan_komposisi(file: UploadFile = File(...)):
    try:
  
        image_bytes = await file.read()
        

        image = Image.open(io.BytesIO(image_bytes))
        
        results = model(image)

        detected_ids = []
        for result in results:
            for box in result.boxes:
                detected_ids.append(int(box.cls[0]))

        status_kompos = "Tidak ada objek terdeteksi"
        if detected_ids:
            try:
                status_kompos = hitung_kompos(detected_ids)
            except NameError:
                status_kompos = "Fungsi logic.py terdeteksi, tetapi eksekusi gagal."

        return {
            "status": "success",
            "detected_object_ids": detected_ids,
            "kesimpulan_logika": status_kompos,
            "message": "Data berhasil diproses secara estafet!"
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}