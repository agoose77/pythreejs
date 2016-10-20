from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Triangle(ThreeWidget):
    """Triangle
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Triangle 
    """
    
    _view_name = Unicode('TriangleView').tag(sync=True)
    _model_name = Unicode('TriangleModel').tag(sync=True)

    a = Vector3(default=[0,0,0]).tag(sync=True)
    b = Vector3(default=[0,0,0]).tag(sync=True)
    c = Vector3(default=[0,0,0]).tag(sync=True)
