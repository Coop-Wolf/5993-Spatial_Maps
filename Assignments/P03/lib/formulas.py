from shapely.geometry import shape
import math



class Formulas:
    """
    This class contains functions that are used to calculate the
    distance and direction between the country the user guessed, and the true country.
    """

    @staticmethod
    def bearing_to_compass(angle: float) -> str:
        """Convert bearing to 8-way compass label."""
        labels = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        idx = round(Formulas.normalize_bearing(angle) / 45) % 8
        return labels[idx]

    @staticmethod
    def normalize_bearing(angle: float) -> float:
        """Normalize angle to [0, 360)."""
        return angle % 360.0
    
    @staticmethod
    def initial_bearing(p1, p2) -> float:
        """Compute initial bearing from p1 to p2, both as (lat, lon)."""
        lat1, lon1 = map(math.radians, p1)
        lat2, lon2 = map(math.radians, p2)

        dlon = lon2 - lon1
        x = math.sin(dlon) * math.cos(lat2)
        y = (
            math.cos(lat1) * math.sin(lat2)
            - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        )
        bearing = math.degrees(math.atan2(x, y))
        return Formulas.normalize_bearing(bearing)


    @staticmethod
    def feature_center_shapely(feature):
        """
        Calculate the centroid of a GeoJSON feature using Shapely.
        Returns (latitude, longitude).
        """
        geom = shape(feature["geometry"])
        centroid = geom.centroid
        return (centroid.y, centroid.x)


    @staticmethod
    def haversine_km(p1, p2) -> float:
        """Great-circle distance in kilometers between (lat, lon) points."""
        lat1, lon1 = map(math.radians, p1)
        lat2, lon2 = map(math.radians, p2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return 6371.0 * c


    @staticmethod
    def haversine_miles(p1, p2) -> float:
        """Great-circle distance in miles."""
        return Formulas.haversine_km(p1, p2) * 0.621371