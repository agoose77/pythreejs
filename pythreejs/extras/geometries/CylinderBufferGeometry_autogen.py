from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.BufferGeometry_autogen import BufferGeometry


class CylinderBufferGeometry(BufferGeometry):
    """CylinderBufferGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/CylinderBufferGeometry 
    """
    
    _view_name = Unicode('CylinderBufferGeometryView').tag(sync=True)
    _model_name = Unicode('CylinderBufferGeometryModel').tag(sync=True)

    radiusTop = CFloat(20).tag(sync=True)
    radiusBottom = CFloat(20).tag(sync=True)
    height = CFloat(100).tag(sync=True)
    radiusSegments = CInt(8).tag(sync=True)
    heightSegments = CInt(1).tag(sync=True)
    openEnded = Bool(False).tag(sync=True)
    thetaStart = CFloat(0).tag(sync=True)
    thetaLength = CFloat(6.283185307179586).tag(sync=True)
