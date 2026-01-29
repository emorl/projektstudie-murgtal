# Zugriff über CDS API: Library laden
import cdsapi
# fragt indviduellen API key ab, muss individuell angelegt werden; Anleitung:
# https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+Windows
client = cdsapi.Client()
# gesuchter Datensatz
dataset = "derived-era5-single-levels-daily-statistics"

# Definition des Daten_requests, kopiert vom Downloadportal des CDS 
request = {
    "product_type": "reanalysis",
    "variable": ["total_precipitation"],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "daily_statistic": "daily_sum",
    "time_zone": "utc+01:00",
    "frequency": "1_hourly",
    "area": [48.8, 8.2, 48.4, 8.5]
}

# Loop, fragt nacheinander alle Jahre in Zeitraum ab
for year in range(1981, 2024):
    request_copy = request.copy()
    request_copy["year"] = [str(year)]
    # eindeutige Bennenung der einzelnen Jahre  
    filename = f"era5_prec_sum_{year}.nc"
    
    # Fortschrittsanzeige wärend download
    print(f"Downloading year {year} ({year-1980}/{2024-1980})")
    client.retrieve(dataset, request_copy, filename)
    print(f"✓ Completed {filename}")

# siehe oben
client = cdsapi.Client()
# Downloadaufforderung
client.retrieve(dataset, request).download()