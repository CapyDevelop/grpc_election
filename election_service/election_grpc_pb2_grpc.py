# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import election_service.election_grpc_pb2 as election__grpc__pb2


class ElectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetElection = channel.unary_unary(
                '/election_grpc.ElectionService/GetElection',
                request_serializer=election__grpc__pb2.Empty.SerializeToString,
                response_deserializer=election__grpc__pb2.GetElectionResponse.FromString,
                )
        self.SetCandidateTmp = channel.unary_unary(
                '/election_grpc.ElectionService/SetCandidateTmp',
                request_serializer=election__grpc__pb2.SetCandidateRequest.SerializeToString,
                response_deserializer=election__grpc__pb2.SetCandidateResponse.FromString,
                )
        self.SetCandidateCapy = channel.unary_unary(
                '/election_grpc.ElectionService/SetCandidateCapy',
                request_serializer=election__grpc__pb2.SetCandidateRequest.SerializeToString,
                response_deserializer=election__grpc__pb2.SetCandidateResponse.FromString,
                )
        self.CheckCandidateTmp = channel.unary_unary(
                '/election_grpc.ElectionService/CheckCandidateTmp',
                request_serializer=election__grpc__pb2.CheckCandidateRequest.SerializeToString,
                response_deserializer=election__grpc__pb2.CheckCandidateResponse.FromString,
                )
        self.CheckCandidateCapy = channel.unary_unary(
                '/election_grpc.ElectionService/CheckCandidateCapy',
                request_serializer=election__grpc__pb2.CheckCandidateRequest.SerializeToString,
                response_deserializer=election__grpc__pb2.CheckCandidateResponse.FromString,
                )


class ElectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetElection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCandidateTmp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCandidateCapy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCandidateTmp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCandidateCapy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ElectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetElection': grpc.unary_unary_rpc_method_handler(
                    servicer.GetElection,
                    request_deserializer=election__grpc__pb2.Empty.FromString,
                    response_serializer=election__grpc__pb2.GetElectionResponse.SerializeToString,
            ),
            'SetCandidateTmp': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCandidateTmp,
                    request_deserializer=election__grpc__pb2.SetCandidateRequest.FromString,
                    response_serializer=election__grpc__pb2.SetCandidateResponse.SerializeToString,
            ),
            'SetCandidateCapy': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCandidateCapy,
                    request_deserializer=election__grpc__pb2.SetCandidateRequest.FromString,
                    response_serializer=election__grpc__pb2.SetCandidateResponse.SerializeToString,
            ),
            'CheckCandidateTmp': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckCandidateTmp,
                    request_deserializer=election__grpc__pb2.CheckCandidateRequest.FromString,
                    response_serializer=election__grpc__pb2.CheckCandidateResponse.SerializeToString,
            ),
            'CheckCandidateCapy': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckCandidateCapy,
                    request_deserializer=election__grpc__pb2.CheckCandidateRequest.FromString,
                    response_serializer=election__grpc__pb2.CheckCandidateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'election_grpc.ElectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ElectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetElection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/election_grpc.ElectionService/GetElection',
            election__grpc__pb2.Empty.SerializeToString,
            election__grpc__pb2.GetElectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCandidateTmp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/election_grpc.ElectionService/SetCandidateTmp',
            election__grpc__pb2.SetCandidateRequest.SerializeToString,
            election__grpc__pb2.SetCandidateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCandidateCapy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/election_grpc.ElectionService/SetCandidateCapy',
            election__grpc__pb2.SetCandidateRequest.SerializeToString,
            election__grpc__pb2.SetCandidateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckCandidateTmp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/election_grpc.ElectionService/CheckCandidateTmp',
            election__grpc__pb2.CheckCandidateRequest.SerializeToString,
            election__grpc__pb2.CheckCandidateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckCandidateCapy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/election_grpc.ElectionService/CheckCandidateCapy',
            election__grpc__pb2.CheckCandidateRequest.SerializeToString,
            election__grpc__pb2.CheckCandidateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
