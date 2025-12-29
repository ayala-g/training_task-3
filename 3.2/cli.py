import json
import os
from typing import Any, Dict, List

import typer

DATA_FILE = "cli_data.jsonl"

app = typer.Typer()

#הפונקצייה מוסיפה את הנתונים לקובץ כך שכל נתון אחד בשורה נפרדת
def append_data_to_file(data: Dict[str, Any]):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        json_line = json.dumps(data, ensure_ascii=False)
        f.write(json_line + "\n")


#הפונקציה  קוראת את הקובץ ומחזירה עד 10 נתונים אחרונים.
def read_last10_data(limit: int = 10) -> List[Dict[str, Any]]:
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    last_lines = lines[-limit:]
    return [json.loads(line) for line in last_lines]


#הפקודה מקבלת מהמשתמש מחרוזת שמכילה נתונים במבנה JSON, דרך שורת הפקודה.
#הפקודה ממירה את האובייקט ומוסיפה אותו לקובץ
@app.command()
def add(json_data: str):
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        typer.echo(" שגיאה: מחרוזת ה-JSON אינה תקינה")
        raise typer.Exit(code=1)

    append_data_to_file(data)
    typer.echo("נוסף בהצלחה")
    typer.echo(data)

# פקודה שמחזירה את 10 הנתונים האחרונים שבקובץ.
@app.command("last10")
def last10():
    data = read_last10_data(10)

    if not data:
        typer.echo("עדיין אין נתונים.")
        raise typer.Exit()

    typer.echo(
        json.dumps(
            {"count": len(data), "items": data},
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    app()
