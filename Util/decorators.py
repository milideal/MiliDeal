from bson import ObjectId


def convert_objectId(func):
    def object_id_insert(*args, **kwargs):
        args[0].kwargs["pk"] = ObjectId(kwargs["pk"])
        response = func(*args, **kwargs)
        return response
    return object_id_insert
