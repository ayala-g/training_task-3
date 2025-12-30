FROM python:3.11

# התקנת ffmpeg בתוך הקונטיינר
RUN apt-get update && apt-get install -y ffmpeg

# תקיית הפרוייקט שלנו
WORKDIR /app

# מעתיקים את כל הקבצים  לתוך תקיית הפרוייקט 
COPY . /app

# מתקינים את ספריות פייתון מה- requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:server", "--host", "0.0.0.0", "--port", "8000"]
