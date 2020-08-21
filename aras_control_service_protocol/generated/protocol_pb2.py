# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eprotocol.proto\"F\n\x0f\x44roneIdentifier\x12\x10\n\x08owner_id\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61se_id\x18\x02 \x01(\t\x12\x10\n\x08\x64rone_id\x18\x03 \x01(\t\"^\n\x05\x44rone\x12$\n\nidentifier\x18\x01 \x01(\x0b\x32\x10.DroneIdentifier\x12\x13\n\x0b\x61\x63\x63\x65ss_data\x18\x02 \x01(\t\x12\x1a\n\x12\x63ontrol_service_ip\x18\x03 \x01(\t\"D\n\x0bGoUpMessage\x12\x15\n\x05\x64rone\x18\x01 \x01(\x0b\x32\x06.Drone\x12\x10\n\x08\x61ltitude\x18\x02 \x01(\x05\x12\x0c\n\x04roll\x18\x03 \x01(\x05\"\x05\n\x03\x41\x43K2V\n\x15\x43ontrolServiceActions\x12\x1c\n\x0cStartTakeoff\x12\x06.Drone\x1a\x04.ACK\x12\x1f\n\tStartGoUp\x12\x0c.GoUpMessage\x1a\x04.ACK2\xe4\x02\n\x14\x43ontrolServiceEvents\x12\x34\n\x1aTake_Off_Connection_Failed\x12\x10.DroneIdentifier\x1a\x04.ACK\x12\x37\n\x1dTake_Off_Connected_But_Failed\x12\x10.DroneIdentifier\x1a\x04.ACK\x12\'\n\rTake_Off_Done\x12\x10.DroneIdentifier\x1a\x04.ACK\x12&\n\x0cGo_Up_Failed\x12\x10.DroneIdentifier\x1a\x04.ACK\x12\x33\n\x19Go_Up_Set_Settings_Failed\x12\x10.DroneIdentifier\x1a\x04.ACK\x12\x31\n\x17Go_Up_Set_Settings_Done\x12\x10.DroneIdentifier\x1a\x04.ACK\x12$\n\nGo_Up_Done\x12\x10.DroneIdentifier\x1a\x04.ACKb\x06proto3'
)




_DRONEIDENTIFIER = _descriptor.Descriptor(
  name='DroneIdentifier',
  full_name='DroneIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='DroneIdentifier.owner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_id', full_name='DroneIdentifier.base_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drone_id', full_name='DroneIdentifier.drone_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=18,
  serialized_end=88,
)


_DRONE = _descriptor.Descriptor(
  name='Drone',
  full_name='Drone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='Drone.identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_data', full_name='Drone.access_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='control_service_ip', full_name='Drone.control_service_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=90,
  serialized_end=184,
)


_GOUPMESSAGE = _descriptor.Descriptor(
  name='GoUpMessage',
  full_name='GoUpMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drone', full_name='GoUpMessage.drone', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='GoUpMessage.altitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roll', full_name='GoUpMessage.roll', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=186,
  serialized_end=254,
)


_ACK = _descriptor.Descriptor(
  name='ACK',
  full_name='ACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=256,
  serialized_end=261,
)

_DRONE.fields_by_name['identifier'].message_type = _DRONEIDENTIFIER
_GOUPMESSAGE.fields_by_name['drone'].message_type = _DRONE
DESCRIPTOR.message_types_by_name['DroneIdentifier'] = _DRONEIDENTIFIER
DESCRIPTOR.message_types_by_name['Drone'] = _DRONE
DESCRIPTOR.message_types_by_name['GoUpMessage'] = _GOUPMESSAGE
DESCRIPTOR.message_types_by_name['ACK'] = _ACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DroneIdentifier = _reflection.GeneratedProtocolMessageType('DroneIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _DRONEIDENTIFIER,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:DroneIdentifier)
  })
_sym_db.RegisterMessage(DroneIdentifier)

Drone = _reflection.GeneratedProtocolMessageType('Drone', (_message.Message,), {
  'DESCRIPTOR' : _DRONE,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:Drone)
  })
_sym_db.RegisterMessage(Drone)

GoUpMessage = _reflection.GeneratedProtocolMessageType('GoUpMessage', (_message.Message,), {
  'DESCRIPTOR' : _GOUPMESSAGE,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:GoUpMessage)
  })
_sym_db.RegisterMessage(GoUpMessage)

ACK = _reflection.GeneratedProtocolMessageType('ACK', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:ACK)
  })
_sym_db.RegisterMessage(ACK)



_CONTROLSERVICEACTIONS = _descriptor.ServiceDescriptor(
  name='ControlServiceActions',
  full_name='ControlServiceActions',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=263,
  serialized_end=349,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartTakeoff',
    full_name='ControlServiceActions.StartTakeoff',
    index=0,
    containing_service=None,
    input_type=_DRONE,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartGoUp',
    full_name='ControlServiceActions.StartGoUp',
    index=1,
    containing_service=None,
    input_type=_GOUPMESSAGE,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLSERVICEACTIONS)

DESCRIPTOR.services_by_name['ControlServiceActions'] = _CONTROLSERVICEACTIONS


_CONTROLSERVICEEVENTS = _descriptor.ServiceDescriptor(
  name='ControlServiceEvents',
  full_name='ControlServiceEvents',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=352,
  serialized_end=708,
  methods=[
  _descriptor.MethodDescriptor(
    name='Take_Off_Connection_Failed',
    full_name='ControlServiceEvents.Take_Off_Connection_Failed',
    index=0,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Take_Off_Connected_But_Failed',
    full_name='ControlServiceEvents.Take_Off_Connected_But_Failed',
    index=1,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Take_Off_Done',
    full_name='ControlServiceEvents.Take_Off_Done',
    index=2,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Go_Up_Failed',
    full_name='ControlServiceEvents.Go_Up_Failed',
    index=3,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Go_Up_Set_Settings_Failed',
    full_name='ControlServiceEvents.Go_Up_Set_Settings_Failed',
    index=4,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Go_Up_Set_Settings_Done',
    full_name='ControlServiceEvents.Go_Up_Set_Settings_Done',
    index=5,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Go_Up_Done',
    full_name='ControlServiceEvents.Go_Up_Done',
    index=6,
    containing_service=None,
    input_type=_DRONEIDENTIFIER,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLSERVICEEVENTS)

DESCRIPTOR.services_by_name['ControlServiceEvents'] = _CONTROLSERVICEEVENTS

# @@protoc_insertion_point(module_scope)
