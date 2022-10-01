import collections

# DO NOT USE GENSHI'S FLATTEN - it is not a generator and will chew up CPU and RAM 
def flatten(l):
    """
    Flatten all iterables (lists, tuples, dicts, etc), into one lazy generator-stream
    """
    if isinstance(l, dict):
        l = l.items()
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el