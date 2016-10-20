from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class WireframeGeometry(Geometry):
    """WireframeGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/WireframeGeometry 
    """
    
    _view_name = Unicode('WireframeGeometryView').tag(sync=True)
    _model_name = Unicode('WireframeGeometryModel').tag(sync=True)

