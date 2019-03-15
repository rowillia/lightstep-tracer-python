#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from __future__ import absolute_import
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
import six
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def Report(self, auth, request):
    """
    Parameters:
     - auth
     - request
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def Report(self, auth, request):
    """
    Parameters:
     - auth
     - request
    """
    self.send_Report(auth, request)
    return self.recv_Report()

  def send_Report(self, auth, request):
    self._oprot.writeMessageBegin('Report', TMessageType.CALL, self._seqid)
    args = Report_args()
    args.auth = auth
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_Report(self):
    iprot = self._iprot
    if iprot.trans.code != 200:
      raise TApplicationException(TApplicationException, "Report failed: Received a server error")
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = Report_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "Report failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["Report"] = Processor.process_Report

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_Report(self, seqid, iprot, oprot):
    args = Report_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = Report_result()
    result.success = self._handler.Report(args.auth, args.request)
    oprot.writeMessageBegin("Report", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class Report_args:
  """
  Attributes:
   - auth
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'auth', (Auth, Auth.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'request', (ReportRequest, ReportRequest.thrift_spec), None, ), # 2
  )

  def __init__(self, auth=None, request=None,):
    self.auth = auth
    self.request = request

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.auth = Auth()
          self.auth.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.request = ReportRequest()
          self.request.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Report_args')
    if self.auth is not None:
      oprot.writeFieldBegin('auth', TType.STRUCT, 1)
      self.auth.write(oprot)
      oprot.writeFieldEnd()
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 2)
      self.request.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.auth)
    value = (value * 31) ^ hash(self.request)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in six.iteritems(self.__dict__)]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Report_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (ReportResponse, ReportResponse.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = ReportResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Report_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in six.iteritems(self.__dict__)]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
