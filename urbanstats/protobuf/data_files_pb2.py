# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_files.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="data_files.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x10\x64\x61ta_files.proto"k\n\x0cStatisticRow\x12\x0f\n\x07statval\x18\x01 \x01(\x02\x12\x0f\n\x07ordinal\x18\x02 \x01(\x05\x12\x17\n\x0foverall_ordinal\x18\x03 \x01(\x05\x12 \n\x18percentile_by_population\x18\x04 \x01(\x02"F\n\rRelatedButton\x12\x10\n\x08longname\x18\x01 \x01(\t\x12\x11\n\tshortname\x18\x02 \x01(\t\x12\x10\n\x08row_type\x18\x03 \x01(\t"L\n\x0eRelatedButtons\x12\x19\n\x11relationship_type\x18\x01 \x01(\t\x12\x1f\n\x07\x62uttons\x18\x02 \x03(\x0b\x32\x0e.RelatedButton"\x93\x01\n\x07\x41rticle\x12\x11\n\tshortname\x18\x01 \x01(\t\x12\x10\n\x08longname\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x14\n\x0c\x61rticle_type\x18\x04 \x01(\t\x12\x1b\n\x04rows\x18\x05 \x03(\x0b\x32\r.StatisticRow\x12 \n\x07related\x18\x06 \x03(\x0b\x32\x0f.RelatedButtonsb\x06proto3',
)


_STATISTICROW = _descriptor.Descriptor(
    name="StatisticRow",
    full_name="StatisticRow",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="statval",
            full_name="StatisticRow.statval",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ordinal",
            full_name="StatisticRow.ordinal",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="overall_ordinal",
            full_name="StatisticRow.overall_ordinal",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="percentile_by_population",
            full_name="StatisticRow.percentile_by_population",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=20,
    serialized_end=127,
)


_RELATEDBUTTON = _descriptor.Descriptor(
    name="RelatedButton",
    full_name="RelatedButton",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="longname",
            full_name="RelatedButton.longname",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shortname",
            full_name="RelatedButton.shortname",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="row_type",
            full_name="RelatedButton.row_type",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=129,
    serialized_end=199,
)


_RELATEDBUTTONS = _descriptor.Descriptor(
    name="RelatedButtons",
    full_name="RelatedButtons",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="relationship_type",
            full_name="RelatedButtons.relationship_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="buttons",
            full_name="RelatedButtons.buttons",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=201,
    serialized_end=277,
)


_ARTICLE = _descriptor.Descriptor(
    name="Article",
    full_name="Article",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="shortname",
            full_name="Article.shortname",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="longname",
            full_name="Article.longname",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="source",
            full_name="Article.source",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="article_type",
            full_name="Article.article_type",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rows",
            full_name="Article.rows",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="related",
            full_name="Article.related",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=280,
    serialized_end=427,
)

_RELATEDBUTTONS.fields_by_name["buttons"].message_type = _RELATEDBUTTON
_ARTICLE.fields_by_name["rows"].message_type = _STATISTICROW
_ARTICLE.fields_by_name["related"].message_type = _RELATEDBUTTONS
DESCRIPTOR.message_types_by_name["StatisticRow"] = _STATISTICROW
DESCRIPTOR.message_types_by_name["RelatedButton"] = _RELATEDBUTTON
DESCRIPTOR.message_types_by_name["RelatedButtons"] = _RELATEDBUTTONS
DESCRIPTOR.message_types_by_name["Article"] = _ARTICLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatisticRow = _reflection.GeneratedProtocolMessageType(
    "StatisticRow",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATISTICROW,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:StatisticRow)
    },
)
_sym_db.RegisterMessage(StatisticRow)

RelatedButton = _reflection.GeneratedProtocolMessageType(
    "RelatedButton",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATEDBUTTON,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:RelatedButton)
    },
)
_sym_db.RegisterMessage(RelatedButton)

RelatedButtons = _reflection.GeneratedProtocolMessageType(
    "RelatedButtons",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATEDBUTTONS,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:RelatedButtons)
    },
)
_sym_db.RegisterMessage(RelatedButtons)

Article = _reflection.GeneratedProtocolMessageType(
    "Article",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARTICLE,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:Article)
    },
)
_sym_db.RegisterMessage(Article)


# @@protoc_insertion_point(module_scope)
