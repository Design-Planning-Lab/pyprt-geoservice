from typing import List, Tuple
import shapely
from .dataTypes import Feature, Polygon, LineString


DISTANCE_MAP = {
    "CAT1": 18.0,
    "CAT2": 15.0,
    "CAT3": 12.0,
    "CAT4": 9.0,
    "CAT5": 6.0,
    None: 3.0,  # no category
}


def getSetbackDistsPerEdge(
    edgeAttributesList: List[List[Feature[LineString]]], distanceMap=DISTANCE_MAP
) -> List[float]:
    """Takes in a list of edge attributes and returns the a list of setback distances"""

    def getSetback(roads: List[Feature[LineString]]):
        if len(roads) == 0:
            return distanceMap[None]
        return max(
            distanceMap.get(i.properties["road_cat"], distanceMap[None]) for i in roads
        )

    setbackDistList: List[float] = [getSetback(i) for i in edgeAttributesList]
    return setbackDistList


def computeEdgeAttributes(
    site: Feature[Polygon],
    roads: List[Feature[LineString]],
    attributesList,
    searchDistance=10,
) -> List[List[Feature[LineString]]]:
    """Computes edge attributes of site with roads"""
    site_geom: Polygon = site.geometry
    return getIntersectingRoadsPerEdge(site_geom, roads, searchDistance)


def getIntersectingRoadsPerEdge(
    site_geom: Polygon,
    roads_surrounding: List[Feature[LineString]],
    searchDistance: float,
) -> List[List[Feature[LineString]]]:
    """Takes in a site shapely geometry and roads [{'shape':shapelyLine,'properties':dict}]
    Returns the intersecting roads for each edge --->  [ [road{},road{}] , [], ... ]"""

    vertices_coords: List[Tuple[float, float]] = site_geom.boundary.coords
    site_edges: List[LineString] = [
        LineString([vertices_coords[i], vertices_coords[i + 1]])
        for i in range(len(vertices_coords) - 1)
    ]
    """
    creates a series of search zones projecting from the edges, style 2 = flat cap,
    anticlockwise edges require negative single sided buffer, right of of line == outside of polygon 
    """
    if shapely.is_ccw(site_geom.boundary):
        searchDistance = -abs(searchDistance)
    else:
        searchDistance = abs(searchDistance)
    edgeSearchZones: List[Polygon] = [
        i.buffer(searchDistance, cap_style=2, single_sided=True) for i in site_edges
    ]

    # find roads which intersect in each edgeSearchZones
    intersectingRoadsPerEdge: List[List[Feature[LineString]]] = []
    for s in edgeSearchZones:
        intersectingRoads: List[Feature[LineString]] = [
            r for r in roads_surrounding if r.geometry.intersects(s)
        ]  # nested for
        intersectingRoadsPerEdge.append(intersectingRoads)

    return intersectingRoadsPerEdge
