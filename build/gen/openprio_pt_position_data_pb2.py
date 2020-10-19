# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openprio_pt_position_data.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openprio_pt_position_data.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1fopenprio_pt_position_data.proto\"\x9a\x01\n\x0fLocationMessage\x12.\n\x12vehicle_descriptor\x18\x01 \x01(\x0b\x32\x12.VehicleDescriptor\x12\x1b\n\x08position\x18\x02 \x01(\x0b\x32\t.Position\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\'\n\x0b\x64oor_status\x18\x04 \x01(\x0e\x32\x12.DoorOpeningStatus\"a\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08\x61\x63\x63uracy\x18\x03 \x01(\x02\x12\r\n\x05speed\x18\x04 \x01(\x02\x12\x0f\n\x07\x62\x65\x61ring\x18\x05 \x01(\x02\"X\n\x11VehicleDescriptor\x12\x17\n\x0f\x64\x61ta_owner_code\x18\x01 \x01(\t\x12\x12\n\nblock_code\x18\x02 \x01(\x05\x12\x16\n\x0evehicle_number\x18\x03 \x01(\x05*6\n\x11\x44oorOpeningStatus\x12\n\n\x06\x43LOSED\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\x0b\n\x07NO_DATA\x10\x02\x62\x06proto3'
)

_DOOROPENINGSTATUS = _descriptor.EnumDescriptor(
  name='DoorOpeningStatus',
  full_name='DoorOpeningStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_DATA', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=381,
  serialized_end=435,
)
_sym_db.RegisterEnumDescriptor(_DOOROPENINGSTATUS)

DoorOpeningStatus = enum_type_wrapper.EnumTypeWrapper(_DOOROPENINGSTATUS)
CLOSED = 0
OPEN = 1
NO_DATA = 2



_LOCATIONMESSAGE = _descriptor.Descriptor(
  name='LocationMessage',
  full_name='LocationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vehicle_descriptor', full_name='LocationMessage.vehicle_descriptor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='LocationMessage.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='LocationMessage.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='door_status', full_name='LocationMessage.door_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=190,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Position.latitude', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Position.longitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='Position.accuracy', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='Position.speed', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bearing', full_name='Position.bearing', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=289,
)


_VEHICLEDESCRIPTOR = _descriptor.Descriptor(
  name='VehicleDescriptor',
  full_name='VehicleDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_owner_code', full_name='VehicleDescriptor.data_owner_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_code', full_name='VehicleDescriptor.block_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_number', full_name='VehicleDescriptor.vehicle_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=379,
)

_LOCATIONMESSAGE.fields_by_name['vehicle_descriptor'].message_type = _VEHICLEDESCRIPTOR
_LOCATIONMESSAGE.fields_by_name['position'].message_type = _POSITION
_LOCATIONMESSAGE.fields_by_name['door_status'].enum_type = _DOOROPENINGSTATUS
DESCRIPTOR.message_types_by_name['LocationMessage'] = _LOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['VehicleDescriptor'] = _VEHICLEDESCRIPTOR
DESCRIPTOR.enum_types_by_name['DoorOpeningStatus'] = _DOOROPENINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationMessage = _reflection.GeneratedProtocolMessageType('LocationMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONMESSAGE,
  '__module__' : 'openprio_pt_position_data_pb2'
  # @@protoc_insertion_point(class_scope:LocationMessage)
  })
_sym_db.RegisterMessage(LocationMessage)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'openprio_pt_position_data_pb2'
  # @@protoc_insertion_point(class_scope:Position)
  })
_sym_db.RegisterMessage(Position)

VehicleDescriptor = _reflection.GeneratedProtocolMessageType('VehicleDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLEDESCRIPTOR,
  '__module__' : 'openprio_pt_position_data_pb2'
  # @@protoc_insertion_point(class_scope:VehicleDescriptor)
  })
_sym_db.RegisterMessage(VehicleDescriptor)


# @@protoc_insertion_point(module_scope)
