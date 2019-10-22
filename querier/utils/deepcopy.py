#import copy
#import ujson
#import _pickle as cPickle
import pickle
#import msgpack


def deepcopy(x): #, method='ujson'):        

#    assert method in ('cpickle', 'deepcopy', 'msgpack', 'pickle', 'ujson'),\
#    "cpickle, deepcopy, msgpack, pickle, ujson"
#    
#    h = {"cpickle": (def foo(yy): return cPickle.loads(cPickle.dumps(yy, -1))),
#         "deepcopy": def foo(yy): return copy.deepcopy(yy),
#         "msgpack": def foo(yy): return msgpack.unpackb(msgpack.packb(yy)),
#         "pickle": def foo(yy): return pickle.loads(pickle.dumps(yy, -1)),
#         "ujson": def foo(yy): return ujson.loads(ujson.dumps(yy))}
    
    return pickle.loads(pickle.dumps(x, -1))
