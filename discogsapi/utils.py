

def get_search_obj(obj):
    if isinstance(obj, str):
        out = { "q" : obj}
    else:
        out = obj
    return out