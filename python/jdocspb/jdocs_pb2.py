# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jdocs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jdocs.proto',
  package='jdocspb',
  syntax='proto3',
  serialized_options=b'Z,github.com/digital-dream-labs/api/go/jdocspb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bjdocs.proto\x12\x07jdocspb\x1a\x1cgoogle/api/annotations.proto\"[\n\x04Jdoc\x12\x13\n\x0b\x64oc_version\x18\x01 \x01(\x04\x12\x13\n\x0b\x66mt_version\x18\x02 \x01(\x04\x12\x17\n\x0f\x63lient_metadata\x18\x03 \x01(\t\x12\x10\n\x08json_doc\x18\x04 \x01(\t\"\x17\n\x07\x45\x63hoReq\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\t\"\x18\n\x08\x45\x63hoResp\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\t\"[\n\x0bWriteDocReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05thing\x18\x02 \x01(\t\x12\x10\n\x08\x64oc_name\x18\x03 \x01(\t\x12\x1a\n\x03\x64oc\x18\x04 \x01(\x0b\x32\r.jdocspb.Jdoc\"\xac\x01\n\x0cWriteDocResp\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.jdocspb.WriteDocResp.Status\x12\x1a\n\x12latest_doc_version\x18\x02 \x01(\x04\"R\n\x06Status\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x00\x12\x1c\n\x18REJECTED_BAD_DOC_VERSION\x10\x01\x12\x1c\n\x18REJECTED_BAD_FMT_VERSION\x10\x02\"\x89\x01\n\x0bReadDocsReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05thing\x18\x02 \x01(\t\x12(\n\x05items\x18\x03 \x03(\x0b\x32\x19.jdocspb.ReadDocsReq.Item\x1a\x30\n\x04Item\x12\x10\n\x08\x64oc_name\x18\x01 \x01(\t\x12\x16\n\x0emy_doc_version\x18\x02 \x01(\x04\"\xc0\x01\n\x0cReadDocsResp\x12)\n\x05items\x18\x01 \x03(\x0b\x32\x1a.jdocspb.ReadDocsResp.Item\x1aP\n\x04Item\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.jdocspb.ReadDocsResp.Status\x12\x1a\n\x03\x64oc\x18\x02 \x01(\x0b\x32\r.jdocspb.Jdoc\"3\n\x06Status\x12\r\n\tUNCHANGED\x10\x00\x12\x0b\n\x07\x43HANGED\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\"@\n\x0c\x44\x65leteDocReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05thing\x18\x02 \x01(\t\x12\x10\n\x08\x64oc_name\x18\x03 \x01(\t\"\x0f\n\rDeleteDocResp\"E\n\x13PurgeAccountDocsReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\r\n\x05notes\x18\x03 \x01(\t\"\x16\n\x14PurgeAccountDocsResp\"M\n\x07ViewDoc\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05thing\x18\x02 \x01(\t\x12\x10\n\x08\x64oc_name\x18\x03 \x01(\t\x12\x10\n\x08json_doc\x18\x04 \x01(\t\"%\n\x12ViewAccountDocsReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\".\n\x0cViewDocsResp\x12\x1e\n\x04\x64ocs\x18\x01 \x03(\x0b\x32\x10.jdocspb.ViewDoc2\xe7\x03\n\x05Jdocs\x12P\n\x08WriteDoc\x12\x14.jdocspb.WriteDocReq\x1a\x15.jdocspb.WriteDocResp\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/1/write-doc:\x01*\x12P\n\x08ReadDocs\x12\x14.jdocspb.ReadDocsReq\x1a\x15.jdocspb.ReadDocsResp\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/1/read-docs:\x01*\x12T\n\tDeleteDoc\x12\x15.jdocspb.DeleteDocReq\x1a\x16.jdocspb.DeleteDocResp\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/1/delete-doc:\x01*\x12O\n\x10PurgeAccountDocs\x12\x1c.jdocspb.PurgeAccountDocsReq\x1a\x1d.jdocspb.PurgeAccountDocsResp\x12\x45\n\x0fViewAccountDocs\x12\x1b.jdocspb.ViewAccountDocsReq\x1a\x15.jdocspb.ViewDocsResp\x12L\n\x16ViewAccountDocsWithPII\x12\x1b.jdocspb.ViewAccountDocsReq\x1a\x15.jdocspb.ViewDocsRespB.Z,github.com/digital-dream-labs/api/go/jdocspbb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_WRITEDOCRESP_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='jdocspb.WriteDocResp.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCEPTED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_BAD_DOC_VERSION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_BAD_FMT_VERSION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=382,
  serialized_end=464,
)
_sym_db.RegisterEnumDescriptor(_WRITEDOCRESP_STATUS)

_READDOCSRESP_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='jdocspb.ReadDocsResp.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNCHANGED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=748,
  serialized_end=799,
)
_sym_db.RegisterEnumDescriptor(_READDOCSRESP_STATUS)


_JDOC = _descriptor.Descriptor(
  name='Jdoc',
  full_name='jdocspb.Jdoc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_version', full_name='jdocspb.Jdoc.doc_version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fmt_version', full_name='jdocspb.Jdoc.fmt_version', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_metadata', full_name='jdocspb.Jdoc.client_metadata', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_doc', full_name='jdocspb.Jdoc.json_doc', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=54,
  serialized_end=145,
)


_ECHOREQ = _descriptor.Descriptor(
  name='EchoReq',
  full_name='jdocspb.EchoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='jdocspb.EchoReq.Data', index=0,
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
  serialized_start=147,
  serialized_end=170,
)


_ECHORESP = _descriptor.Descriptor(
  name='EchoResp',
  full_name='jdocspb.EchoResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='jdocspb.EchoResp.Data', index=0,
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
  serialized_start=172,
  serialized_end=196,
)


_WRITEDOCREQ = _descriptor.Descriptor(
  name='WriteDocReq',
  full_name='jdocspb.WriteDocReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='jdocspb.WriteDocReq.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thing', full_name='jdocspb.WriteDocReq.thing', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc_name', full_name='jdocspb.WriteDocReq.doc_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc', full_name='jdocspb.WriteDocReq.doc', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=198,
  serialized_end=289,
)


_WRITEDOCRESP = _descriptor.Descriptor(
  name='WriteDocResp',
  full_name='jdocspb.WriteDocResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='jdocspb.WriteDocResp.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_doc_version', full_name='jdocspb.WriteDocResp.latest_doc_version', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WRITEDOCRESP_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=464,
)


_READDOCSREQ_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='jdocspb.ReadDocsReq.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_name', full_name='jdocspb.ReadDocsReq.Item.doc_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='my_doc_version', full_name='jdocspb.ReadDocsReq.Item.my_doc_version', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=556,
  serialized_end=604,
)

_READDOCSREQ = _descriptor.Descriptor(
  name='ReadDocsReq',
  full_name='jdocspb.ReadDocsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='jdocspb.ReadDocsReq.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thing', full_name='jdocspb.ReadDocsReq.thing', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='jdocspb.ReadDocsReq.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_READDOCSREQ_ITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=604,
)


_READDOCSRESP_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='jdocspb.ReadDocsResp.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='jdocspb.ReadDocsResp.Item.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc', full_name='jdocspb.ReadDocsResp.Item.doc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=666,
  serialized_end=746,
)

_READDOCSRESP = _descriptor.Descriptor(
  name='ReadDocsResp',
  full_name='jdocspb.ReadDocsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='jdocspb.ReadDocsResp.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_READDOCSRESP_ITEM, ],
  enum_types=[
    _READDOCSRESP_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=799,
)


_DELETEDOCREQ = _descriptor.Descriptor(
  name='DeleteDocReq',
  full_name='jdocspb.DeleteDocReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='jdocspb.DeleteDocReq.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thing', full_name='jdocspb.DeleteDocReq.thing', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc_name', full_name='jdocspb.DeleteDocReq.doc_name', index=2,
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
  serialized_start=801,
  serialized_end=865,
)


_DELETEDOCRESP = _descriptor.Descriptor(
  name='DeleteDocResp',
  full_name='jdocspb.DeleteDocResp',
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
  serialized_start=867,
  serialized_end=882,
)


_PURGEACCOUNTDOCSREQ = _descriptor.Descriptor(
  name='PurgeAccountDocsReq',
  full_name='jdocspb.PurgeAccountDocsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='jdocspb.PurgeAccountDocsReq.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='jdocspb.PurgeAccountDocsReq.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notes', full_name='jdocspb.PurgeAccountDocsReq.notes', index=2,
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
  serialized_start=884,
  serialized_end=953,
)


_PURGEACCOUNTDOCSRESP = _descriptor.Descriptor(
  name='PurgeAccountDocsResp',
  full_name='jdocspb.PurgeAccountDocsResp',
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
  serialized_start=955,
  serialized_end=977,
)


_VIEWDOC = _descriptor.Descriptor(
  name='ViewDoc',
  full_name='jdocspb.ViewDoc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='jdocspb.ViewDoc.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thing', full_name='jdocspb.ViewDoc.thing', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc_name', full_name='jdocspb.ViewDoc.doc_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_doc', full_name='jdocspb.ViewDoc.json_doc', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=979,
  serialized_end=1056,
)


_VIEWACCOUNTDOCSREQ = _descriptor.Descriptor(
  name='ViewAccountDocsReq',
  full_name='jdocspb.ViewAccountDocsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='jdocspb.ViewAccountDocsReq.user_id', index=0,
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
  serialized_start=1058,
  serialized_end=1095,
)


_VIEWDOCSRESP = _descriptor.Descriptor(
  name='ViewDocsResp',
  full_name='jdocspb.ViewDocsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docs', full_name='jdocspb.ViewDocsResp.docs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1097,
  serialized_end=1143,
)

_WRITEDOCREQ.fields_by_name['doc'].message_type = _JDOC
_WRITEDOCRESP.fields_by_name['status'].enum_type = _WRITEDOCRESP_STATUS
_WRITEDOCRESP_STATUS.containing_type = _WRITEDOCRESP
_READDOCSREQ_ITEM.containing_type = _READDOCSREQ
_READDOCSREQ.fields_by_name['items'].message_type = _READDOCSREQ_ITEM
_READDOCSRESP_ITEM.fields_by_name['status'].enum_type = _READDOCSRESP_STATUS
_READDOCSRESP_ITEM.fields_by_name['doc'].message_type = _JDOC
_READDOCSRESP_ITEM.containing_type = _READDOCSRESP
_READDOCSRESP.fields_by_name['items'].message_type = _READDOCSRESP_ITEM
_READDOCSRESP_STATUS.containing_type = _READDOCSRESP
_VIEWDOCSRESP.fields_by_name['docs'].message_type = _VIEWDOC
DESCRIPTOR.message_types_by_name['Jdoc'] = _JDOC
DESCRIPTOR.message_types_by_name['EchoReq'] = _ECHOREQ
DESCRIPTOR.message_types_by_name['EchoResp'] = _ECHORESP
DESCRIPTOR.message_types_by_name['WriteDocReq'] = _WRITEDOCREQ
DESCRIPTOR.message_types_by_name['WriteDocResp'] = _WRITEDOCRESP
DESCRIPTOR.message_types_by_name['ReadDocsReq'] = _READDOCSREQ
DESCRIPTOR.message_types_by_name['ReadDocsResp'] = _READDOCSRESP
DESCRIPTOR.message_types_by_name['DeleteDocReq'] = _DELETEDOCREQ
DESCRIPTOR.message_types_by_name['DeleteDocResp'] = _DELETEDOCRESP
DESCRIPTOR.message_types_by_name['PurgeAccountDocsReq'] = _PURGEACCOUNTDOCSREQ
DESCRIPTOR.message_types_by_name['PurgeAccountDocsResp'] = _PURGEACCOUNTDOCSRESP
DESCRIPTOR.message_types_by_name['ViewDoc'] = _VIEWDOC
DESCRIPTOR.message_types_by_name['ViewAccountDocsReq'] = _VIEWACCOUNTDOCSREQ
DESCRIPTOR.message_types_by_name['ViewDocsResp'] = _VIEWDOCSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Jdoc = _reflection.GeneratedProtocolMessageType('Jdoc', (_message.Message,), {
  'DESCRIPTOR' : _JDOC,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.Jdoc)
  })
_sym_db.RegisterMessage(Jdoc)

EchoReq = _reflection.GeneratedProtocolMessageType('EchoReq', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQ,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.EchoReq)
  })
_sym_db.RegisterMessage(EchoReq)

EchoResp = _reflection.GeneratedProtocolMessageType('EchoResp', (_message.Message,), {
  'DESCRIPTOR' : _ECHORESP,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.EchoResp)
  })
_sym_db.RegisterMessage(EchoResp)

WriteDocReq = _reflection.GeneratedProtocolMessageType('WriteDocReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDOCREQ,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.WriteDocReq)
  })
_sym_db.RegisterMessage(WriteDocReq)

WriteDocResp = _reflection.GeneratedProtocolMessageType('WriteDocResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDOCRESP,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.WriteDocResp)
  })
_sym_db.RegisterMessage(WriteDocResp)

ReadDocsReq = _reflection.GeneratedProtocolMessageType('ReadDocsReq', (_message.Message,), {

  'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
    'DESCRIPTOR' : _READDOCSREQ_ITEM,
    '__module__' : 'jdocs_pb2'
    # @@protoc_insertion_point(class_scope:jdocspb.ReadDocsReq.Item)
    })
  ,
  'DESCRIPTOR' : _READDOCSREQ,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.ReadDocsReq)
  })
_sym_db.RegisterMessage(ReadDocsReq)
_sym_db.RegisterMessage(ReadDocsReq.Item)

ReadDocsResp = _reflection.GeneratedProtocolMessageType('ReadDocsResp', (_message.Message,), {

  'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
    'DESCRIPTOR' : _READDOCSRESP_ITEM,
    '__module__' : 'jdocs_pb2'
    # @@protoc_insertion_point(class_scope:jdocspb.ReadDocsResp.Item)
    })
  ,
  'DESCRIPTOR' : _READDOCSRESP,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.ReadDocsResp)
  })
_sym_db.RegisterMessage(ReadDocsResp)
_sym_db.RegisterMessage(ReadDocsResp.Item)

DeleteDocReq = _reflection.GeneratedProtocolMessageType('DeleteDocReq', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOCREQ,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.DeleteDocReq)
  })
_sym_db.RegisterMessage(DeleteDocReq)

DeleteDocResp = _reflection.GeneratedProtocolMessageType('DeleteDocResp', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOCRESP,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.DeleteDocResp)
  })
_sym_db.RegisterMessage(DeleteDocResp)

PurgeAccountDocsReq = _reflection.GeneratedProtocolMessageType('PurgeAccountDocsReq', (_message.Message,), {
  'DESCRIPTOR' : _PURGEACCOUNTDOCSREQ,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.PurgeAccountDocsReq)
  })
_sym_db.RegisterMessage(PurgeAccountDocsReq)

PurgeAccountDocsResp = _reflection.GeneratedProtocolMessageType('PurgeAccountDocsResp', (_message.Message,), {
  'DESCRIPTOR' : _PURGEACCOUNTDOCSRESP,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.PurgeAccountDocsResp)
  })
_sym_db.RegisterMessage(PurgeAccountDocsResp)

ViewDoc = _reflection.GeneratedProtocolMessageType('ViewDoc', (_message.Message,), {
  'DESCRIPTOR' : _VIEWDOC,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.ViewDoc)
  })
_sym_db.RegisterMessage(ViewDoc)

ViewAccountDocsReq = _reflection.GeneratedProtocolMessageType('ViewAccountDocsReq', (_message.Message,), {
  'DESCRIPTOR' : _VIEWACCOUNTDOCSREQ,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.ViewAccountDocsReq)
  })
_sym_db.RegisterMessage(ViewAccountDocsReq)

ViewDocsResp = _reflection.GeneratedProtocolMessageType('ViewDocsResp', (_message.Message,), {
  'DESCRIPTOR' : _VIEWDOCSRESP,
  '__module__' : 'jdocs_pb2'
  # @@protoc_insertion_point(class_scope:jdocspb.ViewDocsResp)
  })
_sym_db.RegisterMessage(ViewDocsResp)


DESCRIPTOR._options = None

_JDOCS = _descriptor.ServiceDescriptor(
  name='Jdocs',
  full_name='jdocspb.Jdocs',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1146,
  serialized_end=1633,
  methods=[
  _descriptor.MethodDescriptor(
    name='WriteDoc',
    full_name='jdocspb.Jdocs.WriteDoc',
    index=0,
    containing_service=None,
    input_type=_WRITEDOCREQ,
    output_type=_WRITEDOCRESP,
    serialized_options=b'\202\323\344\223\002\021\"\014/1/write-doc:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadDocs',
    full_name='jdocspb.Jdocs.ReadDocs',
    index=1,
    containing_service=None,
    input_type=_READDOCSREQ,
    output_type=_READDOCSRESP,
    serialized_options=b'\202\323\344\223\002\021\"\014/1/read-docs:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteDoc',
    full_name='jdocspb.Jdocs.DeleteDoc',
    index=2,
    containing_service=None,
    input_type=_DELETEDOCREQ,
    output_type=_DELETEDOCRESP,
    serialized_options=b'\202\323\344\223\002\022\"\r/1/delete-doc:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PurgeAccountDocs',
    full_name='jdocspb.Jdocs.PurgeAccountDocs',
    index=3,
    containing_service=None,
    input_type=_PURGEACCOUNTDOCSREQ,
    output_type=_PURGEACCOUNTDOCSRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ViewAccountDocs',
    full_name='jdocspb.Jdocs.ViewAccountDocs',
    index=4,
    containing_service=None,
    input_type=_VIEWACCOUNTDOCSREQ,
    output_type=_VIEWDOCSRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ViewAccountDocsWithPII',
    full_name='jdocspb.Jdocs.ViewAccountDocsWithPII',
    index=5,
    containing_service=None,
    input_type=_VIEWACCOUNTDOCSREQ,
    output_type=_VIEWDOCSRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_JDOCS)

DESCRIPTOR.services_by_name['Jdocs'] = _JDOCS

# @@protoc_insertion_point(module_scope)
