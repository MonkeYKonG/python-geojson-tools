import enum


class EntityTypes(enum.Enum):
    feature_collection = 'FeatureCollection'
    feature = 'Feature'
    point = 'Point'
    line_string = 'LineString'
    polygon = 'Polygon'
    multi_polygon = 'MultiPolygon'
