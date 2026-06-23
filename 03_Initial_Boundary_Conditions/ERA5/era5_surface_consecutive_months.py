import cdsapi

dataset = "reanalysis-era5-single-levels"

request = {

    "product_type": ["reanalysis"],

    "variable": [

        "10m_u_component_of_wind",
        "10m_v_component_of_wind",

        "2m_dewpoint_temperature",
        "2m_temperature",

        "mean_sea_level_pressure",
        "surface_pressure",

        "sea_surface_temperature",
        "skin_temperature",

        "snow_depth",

        "soil_temperature_level_1",
        "soil_temperature_level_2",
        "soil_temperature_level_3",
        "soil_temperature_level_4",

        "volumetric_soil_water_layer_1",
        "volumetric_soil_water_layer_2",
        "volumetric_soil_water_layer_3",
        "volumetric_soil_water_layer_4",

        "land_sea_mask",
        "sea_ice_cover"
    ],

    "year": ["2023"],

    "month": [
        "04",
        "05"
    ],

    "day": [
        "28",
        "29",
        "30",
        "01",
        "02"
    ],

    "time": [

        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",

        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",

        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",

        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],

    "data_format": "grib",

    "download_format": "unarchived",

    # [North, West, South, East]
    "area": [55, 40, -10, 120]
}

client = cdsapi.Client()

client.retrieve(
    dataset,
    request
).download("ERA5_SURFACE_20230428_20230502_HOURLY.grib")
