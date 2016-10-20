from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ..._base.Three import ThreeWidget


class PointLightHelper(ThreeWidget):
    """PointLightHelper
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Helpers/PointLightHelper 
    """
    
    _view_name = Unicode('PointLightHelperView').tag(sync=True)
    _model_name = Unicode('PointLightHelperModel').tag(sync=True)

