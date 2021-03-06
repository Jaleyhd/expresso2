# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: expresso.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='expresso.proto',
  package='',
  serialized_pb=_b('\n\x0e\x65xpresso.proto\"\x86\x05\n\x03Job\x12\x0c\n\x04name\x18\x19 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x10\n\x08\x64oc_path\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x03(\t\x12\x12\n\x04\x64\x61ta\x18\x05 \x03(\x0b\x32\x04.Arg\x12\x14\n\x06\x63onfig\x18\x06 \x03(\x0b\x32\x04.Arg\x12\x13\n\x0bscript_path\x18\x07 \x01(\t\x12\x12\n\ndepends_on\x18\x08 \x01(\t\x12\x1b\n\x13pre_exec_rules_path\x18\t \x01(\t\x12\x1c\n\x14post_exec_rules_path\x18\n \x01(\t\x12\x1b\n\x13prereq_install_path\x18\x0b \x01(\t\x12\x19\n\x11prereq_check_path\x18\x0c \x01(\t\x12\x10\n\x08log_path\x18\r \x01(\t\x12\x17\n\x0fjob_config_path\x18\x0e \x01(\t\x12\x1d\n\x15job_config_proto_path\x18\x0f \x01(\t\x12\x17\n\x0fparent_doc_path\x18\x10 \x01(\t\x12\x1e\n\x16parent_job_config_path\x18\x11 \x01(\t\x12$\n\x1cparent_job_config_proto_path\x18\x12 \x01(\t\x12\"\n\x1aparent_pre_exec_rules_path\x18\x13 \x01(\t\x12#\n\x1bparent_post_exec_rules_path\x18\x14 \x01(\t\x12\"\n\x1aparent_prereq_install_path\x18\x15 \x01(\t\x12 \n\x18parent_prereq_check_path\x18\x16 \x01(\t\x12\x17\n\x0fparent_log_path\x18\x17 \x01(\t\x12\x1a\n\x12parent_script_path\x18\x18 \x01(\t\"\xf6\x02\n\x03\x41rg\x12\x0c\n\x04name\x18\x0f \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x10\n\x08\x64oc_path\x18\x04 \x01(\t\x12\x19\n\x11\x63onfig_proto_path\x18\x05 \x01(\t\x12\x13\n\x0b\x63onfig_path\x18\x06 \x01(\t\x12\x1b\n\x13pre_exec_rules_path\x18\x07 \x01(\t\x12\x1c\n\x14post_exec_rules_path\x18\x08 \x01(\t\x12\x17\n\x0fparent_doc_path\x18\t \x01(\t\x12\x1a\n\x12parent_config_path\x18\n \x01(\t\x12 \n\x18parent_config_proto_path\x18\x0b \x01(\t\x12\"\n\x1aparent_pre_exec_rules_path\x18\x0c \x01(\t\x12#\n\x1bparent_post_exec_rules_path\x18\r \x01(\t\x12\x16\n\x07io_type\x18\x0e \x01(\t:\x05input\"A\n\rScheduleGraph\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x0cschedule_job\x18\x02 \x03(\x0b\x32\x0c.ScheduleJob\"\x87\x01\n\x0bScheduleJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndepends_on\x18\x02 \x03(\t\x12\x11\n\x03job\x18\x03 \x01(\x0b\x32\x04.Job\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x12\n\nstart_time\x18\x05 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\t\x12\r\n\x05retry\x18\x07 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Job.name', index=0,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Job.type', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='Job.desc', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_path', full_name='Job.doc_path', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='Job.category', index=4,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Job.data', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='Job.config', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_path', full_name='Job.script_path', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depends_on', full_name='Job.depends_on', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_exec_rules_path', full_name='Job.pre_exec_rules_path', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_exec_rules_path', full_name='Job.post_exec_rules_path', index=10,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prereq_install_path', full_name='Job.prereq_install_path', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prereq_check_path', full_name='Job.prereq_check_path', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_path', full_name='Job.log_path', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_config_path', full_name='Job.job_config_path', index=14,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_config_proto_path', full_name='Job.job_config_proto_path', index=15,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_doc_path', full_name='Job.parent_doc_path', index=16,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_job_config_path', full_name='Job.parent_job_config_path', index=17,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_job_config_proto_path', full_name='Job.parent_job_config_proto_path', index=18,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_pre_exec_rules_path', full_name='Job.parent_pre_exec_rules_path', index=19,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_post_exec_rules_path', full_name='Job.parent_post_exec_rules_path', index=20,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_prereq_install_path', full_name='Job.parent_prereq_install_path', index=21,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_prereq_check_path', full_name='Job.parent_prereq_check_path', index=22,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_log_path', full_name='Job.parent_log_path', index=23,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_script_path', full_name='Job.parent_script_path', index=24,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=665,
)


_ARG = _descriptor.Descriptor(
  name='Arg',
  full_name='Arg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Arg.name', index=0,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Arg.type', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='Arg.category', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='Arg.desc', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_path', full_name='Arg.doc_path', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_proto_path', full_name='Arg.config_proto_path', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_path', full_name='Arg.config_path', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_exec_rules_path', full_name='Arg.pre_exec_rules_path', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_exec_rules_path', full_name='Arg.post_exec_rules_path', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_doc_path', full_name='Arg.parent_doc_path', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_config_path', full_name='Arg.parent_config_path', index=10,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_config_proto_path', full_name='Arg.parent_config_proto_path', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_pre_exec_rules_path', full_name='Arg.parent_pre_exec_rules_path', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_post_exec_rules_path', full_name='Arg.parent_post_exec_rules_path', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='io_type', full_name='Arg.io_type', index=14,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("input").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=1042,
)


_SCHEDULEGRAPH = _descriptor.Descriptor(
  name='ScheduleGraph',
  full_name='ScheduleGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ScheduleGraph.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule_job', full_name='ScheduleGraph.schedule_job', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1044,
  serialized_end=1109,
)


_SCHEDULEJOB = _descriptor.Descriptor(
  name='ScheduleJob',
  full_name='ScheduleJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ScheduleJob.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depends_on', full_name='ScheduleJob.depends_on', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job', full_name='ScheduleJob.job', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='ScheduleJob.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='ScheduleJob.start_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='ScheduleJob.end_time', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retry', full_name='ScheduleJob.retry', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1112,
  serialized_end=1247,
)

_JOB.fields_by_name['data'].message_type = _ARG
_JOB.fields_by_name['config'].message_type = _ARG
_SCHEDULEGRAPH.fields_by_name['schedule_job'].message_type = _SCHEDULEJOB
_SCHEDULEJOB.fields_by_name['job'].message_type = _JOB
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['Arg'] = _ARG
DESCRIPTOR.message_types_by_name['ScheduleGraph'] = _SCHEDULEGRAPH
DESCRIPTOR.message_types_by_name['ScheduleJob'] = _SCHEDULEJOB

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), dict(
  DESCRIPTOR = _JOB,
  __module__ = 'expresso_pb2'
  # @@protoc_insertion_point(class_scope:Job)
  ))
_sym_db.RegisterMessage(Job)

Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), dict(
  DESCRIPTOR = _ARG,
  __module__ = 'expresso_pb2'
  # @@protoc_insertion_point(class_scope:Arg)
  ))
_sym_db.RegisterMessage(Arg)

ScheduleGraph = _reflection.GeneratedProtocolMessageType('ScheduleGraph', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULEGRAPH,
  __module__ = 'expresso_pb2'
  # @@protoc_insertion_point(class_scope:ScheduleGraph)
  ))
_sym_db.RegisterMessage(ScheduleGraph)

ScheduleJob = _reflection.GeneratedProtocolMessageType('ScheduleJob', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULEJOB,
  __module__ = 'expresso_pb2'
  # @@protoc_insertion_point(class_scope:ScheduleJob)
  ))
_sym_db.RegisterMessage(ScheduleJob)


# @@protoc_insertion_point(module_scope)
