import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

import cartopy.crs as ccrs
import cartopy.feature as cfeature


# City coordinates (latitude, longitude)
# These cities are used as example urban study locations for WRF simulations.
# Coordinates correspond approximately to city centers and can be modified
# for any other study region.

cities = {
    "Delhi": {"lat": 28.642, "lon": 77.182},
    "Hyderabad": {"lat": 17.423, "lon": 78.475},
    "Kolkata": {"lat": 22.571, "lon": 88.364},
    "Mumbai": {"lat": 19.037, "lon": 72.874}
}


# Example WRF nested-domain configuration.
#
# dx   : horizontal grid spacing (km)
# e_we : west-east grid points from namelist.wps
# e_sn : south-north grid points from namelist.wps
#
# Values shown here correspond to a typical four-domain setup:
# d01 = 27 km
# d02 = 9 km
# d03 = 3 km
# d04 = 1 km

domains = {
    "d01": {"dx": 27, "e_we": 110, "e_sn": 110},
    "d02": {"dx": 9,  "e_we": 118, "e_sn": 118},
    "d03": {"dx": 3,  "e_we": 118, "e_sn": 118},
    "d04": {"dx": 1,  "e_we": 112, "e_sn": 112},
}


# ERA5 download boundaries used in the CDS API request:
#
# area = [North, West, South, East]
#
# These limits match the download region used in the ERA5 scripts and
# provide sufficient coverage for WRF simulations centered over major
# Indian cities.

era5 = {
    "north": 55,
    "south": -10,
    "west": 40,
    "east": 120
}


# Create map using PlateCarree projection
# Suitable for visualizing latitude-longitude based datasets.

fig = plt.figure(figsize=(15, 12))

ax = plt.axes(projection=ccrs.PlateCarree())


# Add standard geographic features from Natural Earth datasets
# distributed through Cartopy.

ax.add_feature(
    cfeature.LAND,
    facecolor='whitesmoke'
)

ax.add_feature(
    cfeature.OCEAN,
    facecolor='lightcyan'
)

ax.add_feature(
    cfeature.COASTLINE,
    linewidth=1.2
)

ax.add_feature(
    cfeature.BORDERS,
    linewidth=1.0
)


# Add state/province boundaries from Natural Earth.
# Useful for visual reference when selecting model domains.

states = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='10m',
    facecolor='none'
)

ax.add_feature(
    states,
    edgecolor='gray',
    linewidth=0.5
)


# Draw ERA5 download region.
# The rectangle corresponds to:
# area = [55, 40, -10, 120]

era5_rect = Rectangle(
    (era5["west"], era5["south"]),
    era5["east"] - era5["west"],
    era5["north"] - era5["south"],
    fill=False,
    linestyle='--',
    linewidth=3,
    edgecolor='black',
    transform=ccrs.PlateCarree()
)

ax.add_patch(era5_rect)


# Plot city locations and construct nested WRF domains.
#
# Domain dimensions are estimated from:
#
# width  = dx × e_we
# height = dx × e_sn
#
# Conversion from kilometres to degrees is performed using
# latitude-dependent longitude scaling.

for city, info in cities.items():

    ref_lat = info["lat"]
    ref_lon = info["lon"]

    km_per_deg_lat = 111.0
    km_per_deg_lon = 111.0 * np.cos(np.radians(ref_lat))

    ax.scatter(
        ref_lon,
        ref_lat,
        s=150,
        marker='*',
        color='red',
        transform=ccrs.PlateCarree(),
        zorder=5
    )

    ax.text(
        ref_lon + 0.4,
        ref_lat + 0.4,
        city,
        fontsize=12,
        fontweight='bold',
        transform=ccrs.PlateCarree()
    )

    for domain, dom in domains.items():

        width_km = dom["dx"] * dom["e_we"]
        height_km = dom["dx"] * dom["e_sn"]

        width_deg = width_km / km_per_deg_lon
        height_deg = height_km / km_per_deg_lat

        lon_min = ref_lon - width_deg / 2
        lat_min = ref_lat - height_deg / 2

        rect = Rectangle(
            (lon_min, lat_min),
            width_deg,
            height_deg,
            fill=False,
            linewidth=1.8,
            transform=ccrs.PlateCarree()
        )

        ax.add_patch(rect)


# Label domains for Hyderabad only to avoid clutter.
# Labels indicate approximate nested-domain hierarchy.

label_lat = cities["Hyderabad"]["lat"]
label_lon = cities["Hyderabad"]["lon"]

km_per_deg_lon = 111.0 * np.cos(np.radians(label_lat))

for domain, dom in domains.items():

    width_km = dom["dx"] * dom["e_we"]
    width_deg = width_km / km_per_deg_lon

    lon_min = label_lon - width_deg / 2

    ax.text(
        lon_min,
        label_lat + width_deg / 4,
        domain,
        fontsize=10,
        fontweight='bold',
        transform=ccrs.PlateCarree()
    )


# Add latitude-longitude gridlines for geographic reference.

gl = ax.gridlines(
    draw_labels=True,
    linestyle='--',
    alpha=0.5
)

gl.top_labels = False
gl.right_labels = False


# Map extent covering the ERA5 region and surrounding areas.

ax.set_extent(
    [30, 140, -20, 60],
    crs=ccrs.PlateCarree()
)


# Figure title.

plt.title(
    'WRF Nested Domains for Indian Megacities\nwith ERA5 Download Region',
    fontsize=18,
    pad=20
)


# Save high-resolution figure for documentation and repository use.

plt.savefig(
    'WRF_All_Cities_ERA5_Domain_Map.jpg',
    dpi=300,
    bbox_inches='tight'
)

plt.show()