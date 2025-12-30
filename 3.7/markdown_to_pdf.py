import sys
from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# מקבלת נתיב לקובץ markdown (.md) ונתיב לקובץ pdf ליצירה, וממירה ביניהם.
def markdown_to_pdf(md_path: str, pdf_path: str) -> None:
    md_file = Path(md_path)

    # בדיקה שהקובץ באמת קיים
    if not md_file.exists():
        print(f"שגיאה: קובץ markdown לא נמצא: {md_path}")
        return

    # קוראים את תוכן קובץ ה-md
    md_text = md_file.read_text(encoding="utf-8")

    # יצירת קובץ PDF חדש בעזרת reportlab
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    # התחלת כתיבת טקסט בעמוד
    text_object = c.beginText()
    text_object.setTextOrigin(40, height - 50)  # שוליים
    text_object.setFont("Helvetica", 12)

    # כל שורה מה-Markdown נכתבת כטקסט נפרד (plain text)
    for line in md_text.splitlines():
        text_object.textLine(line)

    c.drawText(text_object)
    c.save()

    print(f" נוצר קובץ PDF בהצלחה: {pdf_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("אופן ההרצה:")
        print("python markdown_to_pdf.py <input.md> <output.pdf>")
        sys.exit(1)

    input_md = sys.argv[1]
    output_pdf = sys.argv[2]

    markdown_to_pdf(input_md, output_pdf)
