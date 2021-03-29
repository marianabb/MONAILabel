# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapp.proto\"1\n\x10InferenceRequest\x12\r\n\x05image\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x01(\t\"2\n\x11InferenceResponse\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x01(\t\"\x1f\n\x0cTrainRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"\x1f\n\rTrainResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2n\n\x03\x41pp\x12\x37\n\x0cRunInference\x12\x11.InferenceRequest\x1a\x12.InferenceResponse\"\x00\x12.\n\x0bRunTraining\x12\r.TrainRequest\x1a\x0e.TrainResponse\"\x00\x62\x06proto3'
)




_INFERENCEREQUEST = _descriptor.Descriptor(
  name='InferenceRequest',
  full_name='InferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='InferenceRequest.image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='InferenceRequest.params', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=13,
  serialized_end=62,
)


_INFERENCERESPONSE = _descriptor.Descriptor(
  name='InferenceResponse',
  full_name='InferenceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='InferenceResponse.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='InferenceResponse.params', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=64,
  serialized_end=114,
)


_TRAINREQUEST = _descriptor.Descriptor(
  name='TrainRequest',
  full_name='TrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='TrainRequest.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=116,
  serialized_end=147,
)


_TRAINRESPONSE = _descriptor.Descriptor(
  name='TrainResponse',
  full_name='TrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='TrainResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=149,
  serialized_end=180,
)

DESCRIPTOR.message_types_by_name['InferenceRequest'] = _INFERENCEREQUEST
DESCRIPTOR.message_types_by_name['InferenceResponse'] = _INFERENCERESPONSE
DESCRIPTOR.message_types_by_name['TrainRequest'] = _TRAINREQUEST
DESCRIPTOR.message_types_by_name['TrainResponse'] = _TRAINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InferenceRequest = _reflection.GeneratedProtocolMessageType('InferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEREQUEST,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:InferenceRequest)
  })
_sym_db.RegisterMessage(InferenceRequest)

InferenceResponse = _reflection.GeneratedProtocolMessageType('InferenceResponse', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCERESPONSE,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:InferenceResponse)
  })
_sym_db.RegisterMessage(InferenceResponse)

TrainRequest = _reflection.GeneratedProtocolMessageType('TrainRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINREQUEST,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:TrainRequest)
  })
_sym_db.RegisterMessage(TrainRequest)

TrainResponse = _reflection.GeneratedProtocolMessageType('TrainResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINRESPONSE,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:TrainResponse)
  })
_sym_db.RegisterMessage(TrainResponse)



_APP = _descriptor.ServiceDescriptor(
  name='App',
  full_name='App',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=182,
  serialized_end=292,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunInference',
    full_name='App.RunInference',
    index=0,
    containing_service=None,
    input_type=_INFERENCEREQUEST,
    output_type=_INFERENCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunTraining',
    full_name='App.RunTraining',
    index=1,
    containing_service=None,
    input_type=_TRAINREQUEST,
    output_type=_TRAINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APP)

DESCRIPTOR.services_by_name['App'] = _APP

# @@protoc_insertion_point(module_scope)