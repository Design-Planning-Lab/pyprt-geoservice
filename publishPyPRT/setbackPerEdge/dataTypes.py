from typing import TypeVar, Generic, Dict, Any
from shapely import Polygon, LineString
from copy import deepcopy

geomType = TypeVar("geomType", Polygon, LineString)


class Feature(Generic[geomType]):
    @classmethod
    def makePolygon(cls, f):
        assert f["type"] == "Feature"
        assert f["geometry"]["type"] == "Polygon"
        # assume no holes
        # buffer 0 standardizes the exterior ring to be clockwise
        return cls(Polygon(f["geometry"]["coordinates"][0]).buffer(0), f["properties"])

    @classmethod
    def makeLineString(cls, f):
        assert f["type"] == "Feature"
        assert f["geometry"]["type"] == "LineString"
        return cls(LineString(f["geometry"]["coordinates"]), f["properties"])

    def __init__(self, geometry: geomType, properties: Dict[str, Any]):
        self.geometry: geomType = geometry
        self.properties: dict = deepcopy(properties)

    @property
    def geom_type(self):
        return self.geometry.geom_type
