import sys
from pathlib import Path

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# הפונצייה קוראת תמונה,מפרידה ערוצי R,G,B ובונה היסטוגרמה לכל ערוץ
def plot_rgb_histogram(image_path: str) -> None:

    img_file = Path(image_path)

    if not img_file.exists():
        print(f"שגיאה: לא נמצאה תמונה: {image_path}")
        return

    # פתיחת התמונה והמרה ל-RGB
    image = Image.open(img_file).convert("RGB")

    # ממירים למערך numpy (גובה, רוחב, 3)
    arr = np.array(image)

    # מפרידים לכל ערוץ
    r = arr[:, :, 0].flatten()
    g = arr[:, :, 1].flatten()
    b = arr[:, :, 2].flatten()

    #  היסטוגרמה
    plt.figure(figsize=(8, 5))
    plt.hist(r, bins=256, range=(0, 255), color="red", alpha=0.5, label="Red")
    plt.hist(g, bins=256, range=(0, 255), color="green", alpha=0.5, label="Green")
    plt.hist(b, bins=256, range=(0, 255), color="blue", alpha=0.5, label="Blue")

    plt.title("RGB Histogram")
    plt.xlabel("Value (0–255)")
    plt.ylabel("Pixel count")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("שימוש:")
        print("python image_histogram.py <image_path>")
        sys.exit(1)

    plot_rgb_histogram(sys.argv[1])
