from fastapi import FastAPI
import subprocess

server = FastAPI()

@server.get("/run-ffmpeg")
def run_ffmpeg():
    
    result = subprocess.run(
        ["ffmpeg", "-version"],
        capture_output=True,
        text=True
    )
    return {"output": result.stdout}
