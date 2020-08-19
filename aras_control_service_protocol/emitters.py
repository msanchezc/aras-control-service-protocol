import grpc
from aras_control_service_protocol.generated import aras_control_service_protocol_pb2, aras_control_service_protocol_pb2_grpc
from aras_control_service_protocol.events import TakeOffEvent

class _ControlServiceEmmiter:
    def __init__(self, control_service_ip):
        self.control_service_ip = control_service_ip
        self.channel = grpc.insecure_channel(self.control_service_ip)

    def _emmit(self, stub_method):
        response = stub_method(aras_control_service_protocol_pb2.Empty())
        return response


class TakeOffEventEmmiter(_ControlServiceEmmiter):
    def emmit(self, take_off_event):
        """
        Args:
            take_off_event: An TakeOffEvent instance
        """
        assert isinstance(take_off_event, TakeOffEvent)
        assert "Channel must be READY", self.channel is not None
        stub = aras_control_service_protocol_pb2_grpc.GoToMissionWaitingAreaStub(self.channel)
        if take_off_event == TakeOffEvent.TAKE_OFF_CONNECTED_BUT_FAILED:
            stub_method = stub.Take_Off_Connected_But_Failed
        elif take_off_event == TakeOffEvent.TAKE_OFF_CONNECTION_FAILED:
            stub_method = stub.Take_Off_Connection_Failed
        elif take_off_event == TakeOffEvent.TAKE_OFF_DONE:
            stub_method = stub.Take_Off_Done
        return self._emmit(stub_method)
