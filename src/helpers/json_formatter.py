from libs.debugger import *


class JsonFormatter():
    def single_elem_to_obj(self, obj, keys):
        obj = list(obj[0])
        if not keys:
            keys = [x for x in range(len(obj))]

        return dict(zip(keys, obj))

    def elems_to_obj(self, obj, keys):
        obj = list(obj)

        # all elemets in object must have same size
        if not keys:
            keys = [x for x in range(len(obj[0]))]

        formatted_obj = []
        for elem in obj:
            formatted_obj.append(dict(zip(keys, elem)))

        return formatted_obj


jf = JsonFormatter()
