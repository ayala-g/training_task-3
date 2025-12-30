# המרת קואורדינטות מ-Decimal Degrees ל-Degrees Minutes Seconds

from typing import List, Dict, Any

#  הפונקציה ממירה ערך DD לרשימה: [degrees, minutes, seconds, hemisphere]
def dd_to_dms(value: float, is_lat: bool) -> List[Any]:
    
    if is_lat:
        hemisphere = "N" if value >= 0 else "S"
    else:
        hemisphere = "E" if value >= 0 else "W"

    abs_val = abs(value)

    degrees = int(abs_val)
    minutes_float = (abs_val - degrees) * 60
    minutes = int(minutes_float)
    seconds = round((minutes_float - minutes) * 60, 2)

    return [degrees, minutes, seconds, hemisphere]

#הפונקציה  מקבלת מילון עם dd ומחזירה מילון עם dd + dms
def convert(locations: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:

    result = {}

    for name, data in locations.items():
        dd = data["dd"]

        lon = dd[0]
        lat = dd[1]

        lon_dms = dd_to_dms(lon, is_lat=False)
        lat_dms = dd_to_dms(lat, is_lat=True)

        # אם יש ערך נוסף משאירים אותו
        if len(dd) > 2:
            dms = [lon_dms, lat_dms, dd[2]]
        else:
            dms = [lon_dms, lat_dms]

        result[name] = {
            "dd": dd,
            "dms": dms
        }

    return result


if __name__ == "__main__":
    locations = {
        "anchorage": {
            "dd": [149.90028, 61.2181, 22]
        },
        "los_angeles": {
            "dd": [-118.2437, 34.0522]
        }
    }

    print(convert(locations))
