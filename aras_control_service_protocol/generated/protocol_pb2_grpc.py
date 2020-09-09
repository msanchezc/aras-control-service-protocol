# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aras_control_service_protocol.generated import protocol_pb2 as protocol__pb2


class ControlServiceActionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartTakeoff = channel.unary_unary(
                '/ControlServiceActions/StartTakeoff',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.StartGoUp = channel.unary_unary(
                '/ControlServiceActions/StartGoUp',
                request_serializer=protocol__pb2.GoUpMessage.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.StartMission = channel.unary_unary(
                '/ControlServiceActions/StartMission',
                request_serializer=protocol__pb2.MissionData.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )


class ControlServiceActionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartTakeoff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartGoUp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartMission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlServiceActionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartTakeoff': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTakeoff,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'StartGoUp': grpc.unary_unary_rpc_method_handler(
                    servicer.StartGoUp,
                    request_deserializer=protocol__pb2.GoUpMessage.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'StartMission': grpc.unary_unary_rpc_method_handler(
                    servicer.StartMission,
                    request_deserializer=protocol__pb2.MissionData.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ControlServiceActions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ControlServiceActions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartTakeoff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceActions/StartTakeoff',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartGoUp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceActions/StartGoUp',
            protocol__pb2.GoUpMessage.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartMission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceActions/StartMission',
            protocol__pb2.MissionData.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ControlServiceEventsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartControlService = channel.unary_unary(
                '/ControlServiceEvents/StartControlService',
                request_serializer=protocol__pb2.StartInfo.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.StopControlService = channel.unary_unary(
                '/ControlServiceEvents/StopControlService',
                request_serializer=protocol__pb2.Empty.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.GetControlServiceStatus = channel.unary_unary(
                '/ControlServiceEvents/GetControlServiceStatus',
                request_serializer=protocol__pb2.Empty.SerializeToString,
                response_deserializer=protocol__pb2.Bool.FromString,
                )
        self.Wake_Up_Done = channel.unary_unary(
                '/ControlServiceEvents/Wake_Up_Done',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Take_Off_Connection_Failed = channel.unary_unary(
                '/ControlServiceEvents/Take_Off_Connection_Failed',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Take_Off_Connected_But_Failed = channel.unary_unary(
                '/ControlServiceEvents/Take_Off_Connected_But_Failed',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Take_Off_Done = channel.unary_unary(
                '/ControlServiceEvents/Take_Off_Done',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Go_Up_Failed = channel.unary_unary(
                '/ControlServiceEvents/Go_Up_Failed',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Go_Up_Set_Settings_Failed = channel.unary_unary(
                '/ControlServiceEvents/Go_Up_Set_Settings_Failed',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Go_Up_Set_Settings_Done = channel.unary_unary(
                '/ControlServiceEvents/Go_Up_Set_Settings_Done',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )
        self.Go_Up_Done = channel.unary_unary(
                '/ControlServiceEvents/Go_Up_Done',
                request_serializer=protocol__pb2.Device.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )


class ControlServiceEventsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartControlService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopControlService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetControlServiceStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Wake_Up_Done(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Take_Off_Connection_Failed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Take_Off_Connected_But_Failed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Take_Off_Done(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Go_Up_Failed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Go_Up_Set_Settings_Failed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Go_Up_Set_Settings_Done(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Go_Up_Done(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlServiceEventsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartControlService': grpc.unary_unary_rpc_method_handler(
                    servicer.StartControlService,
                    request_deserializer=protocol__pb2.StartInfo.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'StopControlService': grpc.unary_unary_rpc_method_handler(
                    servicer.StopControlService,
                    request_deserializer=protocol__pb2.Empty.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'GetControlServiceStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetControlServiceStatus,
                    request_deserializer=protocol__pb2.Empty.FromString,
                    response_serializer=protocol__pb2.Bool.SerializeToString,
            ),
            'Wake_Up_Done': grpc.unary_unary_rpc_method_handler(
                    servicer.Wake_Up_Done,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Take_Off_Connection_Failed': grpc.unary_unary_rpc_method_handler(
                    servicer.Take_Off_Connection_Failed,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Take_Off_Connected_But_Failed': grpc.unary_unary_rpc_method_handler(
                    servicer.Take_Off_Connected_But_Failed,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Take_Off_Done': grpc.unary_unary_rpc_method_handler(
                    servicer.Take_Off_Done,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Go_Up_Failed': grpc.unary_unary_rpc_method_handler(
                    servicer.Go_Up_Failed,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Go_Up_Set_Settings_Failed': grpc.unary_unary_rpc_method_handler(
                    servicer.Go_Up_Set_Settings_Failed,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Go_Up_Set_Settings_Done': grpc.unary_unary_rpc_method_handler(
                    servicer.Go_Up_Set_Settings_Done,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
            'Go_Up_Done': grpc.unary_unary_rpc_method_handler(
                    servicer.Go_Up_Done,
                    request_deserializer=protocol__pb2.Device.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ControlServiceEvents', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ControlServiceEvents(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartControlService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/StartControlService',
            protocol__pb2.StartInfo.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopControlService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/StopControlService',
            protocol__pb2.Empty.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetControlServiceStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/GetControlServiceStatus',
            protocol__pb2.Empty.SerializeToString,
            protocol__pb2.Bool.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Wake_Up_Done(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Wake_Up_Done',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Take_Off_Connection_Failed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Take_Off_Connection_Failed',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Take_Off_Connected_But_Failed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Take_Off_Connected_But_Failed',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Take_Off_Done(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Take_Off_Done',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Go_Up_Failed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Go_Up_Failed',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Go_Up_Set_Settings_Failed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Go_Up_Set_Settings_Failed',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Go_Up_Set_Settings_Done(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Go_Up_Set_Settings_Done',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Go_Up_Done(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlServiceEvents/Go_Up_Done',
            protocol__pb2.Device.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
