from fastapi import FastAPI, Body
import json
import os
from typing import List, Dict, Any

# שם הקובץ שבו נשמור את כל ה-JSONים
DATA_FILE = "data.jsonl"

app = FastAPI()


#    פונקצייה שמוסיפה לקובץ שלנו את הקלט כך שכל אובייקט אחד הוא שורה
def append_data_to_file(data: Dict[str, Any]) -> None:
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        json_line = json.dumps(data, ensure_ascii=False)
        f.write(json_line + "\n")


# פונקציה שקוראת את הקובץ ומחזירה את ה-10 נתונים האחרונים שנוספו (או פחות אם אין).
def read_last_data(limit: int = 10) -> List[Dict[str, Any]]:
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    last_lines = lines[-limit:]
    data = [json.loads(line) for line in last_lines]
    return data


# אנדפוינט שמקבל נתונים מהלקוח ומוסיף לקובץ שלנו
@app.post("/data")
async def add_data(data: Dict[str, Any] = Body(...)):
    append_data_to_file(data)
    return {
        "status": "ok",
        "message": "the data was saved",
        "saved_data": data,
    }


#אנדפוינט שמחזיר את 10 הנתונים האחרונים שנשמרו בקובץ data
@app.get("/data/last10")
async def get_last_10_posted():
    data = read_last_data(10)
    return {
        "count": len(data),
        "items": data,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
