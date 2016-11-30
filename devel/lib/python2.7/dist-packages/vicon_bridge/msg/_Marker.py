# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vicon_bridge/Marker.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class Marker(genpy.Message):
  _md5sum = "da6f93747c24b19a71932ae4b040f489"
  _type = "vicon_bridge/Marker"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string marker_name
string subject_name
string segment_name
geometry_msgs/Point translation
bool occluded

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['marker_name','subject_name','segment_name','translation','occluded']
  _slot_types = ['string','string','string','geometry_msgs/Point','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       marker_name,subject_name,segment_name,translation,occluded

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Marker, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.marker_name is None:
        self.marker_name = ''
      if self.subject_name is None:
        self.subject_name = ''
      if self.segment_name is None:
        self.segment_name = ''
      if self.translation is None:
        self.translation = geometry_msgs.msg.Point()
      if self.occluded is None:
        self.occluded = False
    else:
      self.marker_name = ''
      self.subject_name = ''
      self.segment_name = ''
      self.translation = geometry_msgs.msg.Point()
      self.occluded = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.marker_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.subject_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.segment_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3dB.pack(_x.translation.x, _x.translation.y, _x.translation.z, _x.occluded))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.translation is None:
        self.translation = geometry_msgs.msg.Point()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker_name = str[start:end].decode('utf-8')
      else:
        self.marker_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.subject_name = str[start:end].decode('utf-8')
      else:
        self.subject_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segment_name = str[start:end].decode('utf-8')
      else:
        self.segment_name = str[start:end]
      _x = self
      start = end
      end += 25
      (_x.translation.x, _x.translation.y, _x.translation.z, _x.occluded,) = _struct_3dB.unpack(str[start:end])
      self.occluded = bool(self.occluded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.marker_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.subject_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.segment_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3dB.pack(_x.translation.x, _x.translation.y, _x.translation.z, _x.occluded))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.translation is None:
        self.translation = geometry_msgs.msg.Point()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker_name = str[start:end].decode('utf-8')
      else:
        self.marker_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.subject_name = str[start:end].decode('utf-8')
      else:
        self.subject_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segment_name = str[start:end].decode('utf-8')
      else:
        self.segment_name = str[start:end]
      _x = self
      start = end
      end += 25
      (_x.translation.x, _x.translation.y, _x.translation.z, _x.occluded,) = _struct_3dB.unpack(str[start:end])
      self.occluded = bool(self.occluded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3dB = struct.Struct("<3dB")
