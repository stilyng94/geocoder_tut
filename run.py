import geocoder
import time


def geo_reverse(long: float, lat: float, method: str = "reverse"):
    """
    Use arcgis or yahoo service. Offer free services
    :param long:
    :param lat:
    :param method:
    :return: Map
    """
    arcgis_coded = geocoder.arcgis([lat, long], method=method)
    print(f"ArcGis =>> {arcgis_coded.json}\n\n")
    time.sleep(2)
    yahoo_coded = geocoder.arcgis([6.7272385, -1.461295], method="reverse")
    print(f"Yahoo =>> {yahoo_coded.json}\n")


if __name__ == "__main__":
    geo_reverse(-1.461295, 6.7272385)


