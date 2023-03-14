import abc
import json

from geopy import distance
from shapely import geometry

from .base_entity import BaseEntity
from .constants import EntityTypes


class BaseGeometry(BaseEntity, abc.ABC):
    def __init__(self, entity_type, geom):
        super().__init__(entity_type)
        self._geometry = geom

    def to_geojson(self) -> dict:
        return self._geometry.__geo_interface__

    @classmethod
    def from_dict(cls, obj: dict):
        obj_coordinate = obj.get('coordinates')
        return cls(obj_coordinate)

    @classmethod
    def from_string(cls, string: str):
        obj = json.loads(string)
        return cls.from_dict(obj)

    @classmethod
    def from_file(cls, path: str):
        obj = json.load(open(path))
        return cls.from_dict(obj)


class Point(BaseGeometry):
    def __init__(self, point):
        self.x, self.y = point
        super().__init__(
            EntityTypes.point,
            geometry.Point(self.x, self.y),
        )

    def to_circle(self, radius, max_point=36) -> geometry.Polygon:
        dist = distance.distance(meters=radius)
        coordinates = [(d.longitude, d.latitude)
                       for d in (
                           dist.destination(point=[self.x, self.y], bearing=i)
                           for i in range(0, 360, 360 // max_point or 1)
                       )]
        return Polygon(coordinates)

    def to_square(self, size):
        size_x, size_y = size


class LineString(BaseGeometry):
    def __init__(self, points):
        self.points = points
        super().__init__(
            EntityTypes.line_string,
            geometry.LineString(self.points),
        )


class Polygon(BaseGeometry):
    def __init__(self, polygon):
        self.polygon = polygon
        super().__init__(
            EntityTypes.polygon,
            geometry.Polygon(self.polygon[0], holes=self.polygon[1:]),
        )


class MultiPolygon(BaseGeometry):
    def __init__(self, polygons):
        self.polygons = polygons
        super().__init__(
            EntityTypes.multi_polygon,
            geometry.MultiPolygon((
                geometry.Polygon(polygon[0], holes=polygon[1:])
                for polygon in self.polygons
            )),
        )
