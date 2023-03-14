import json

from . import errors, constants, geometries, feature_collection, feature

GEOMETRY_CLASSES = {
    constants.EntityTypes.point: geometries.Point,
    constants.EntityTypes.line_string: geometries.LineString,
    constants.EntityTypes.polygon: geometries.Polygon,
    constants.EntityTypes.multi_polygon: geometries.MultiPolygon,
    constants.EntityTypes.feature_collection: feature_collection.FeatureCollection,
    constants.EntityTypes.feature: feature.Feature,
}


def load(obj: dict):
    obj_type = obj.get('type')
    if obj_type is None:
        raise ValueError(errors.INVALID_FORMAT)
    if obj_type not in constants.EntityTypes:
        raise ValueError(errors.UNKNOWN_TYPE)
    return GEOMETRY_CLASSES[obj_type].from_dict(obj)


def load_from_string(string_content: str):
    content = json.loads(string_content)
    return load(content)


def load_from_file(path: str):
    file_content = json.load(open(path))
    return load(file_content)
