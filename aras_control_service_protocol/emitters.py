import grpc

from aras_control_service_protocol.events import (
    TakeOffEvent, GoUpEvent, ArasEvent, WakeUpEvent
)
from aras_control_service_protocol.actions import (
    TakeOffAction, GoUpAction
)
from aras_control_service_protocol.messages import (
    Device, GoUpMessage, Empty, StartInfo
)
from aras_control_service_protocol._stubs import (
    ControlServiceEventsStub,
    ControlServiceActionsStub
)


class _ControlServiceEmiter:
    def __init__(self, control_service_ip):
        self.control_service_ip = control_service_ip
        self.channel = grpc.insecure_channel(self.control_service_ip)


# ------------------------ Events emitters -----------------------------#

class WakeUpEventEmitter(_ControlServiceEmiter):
    def emit(self, wake_up_event, drone):
        """
        Args:
            wake_up_event: An WakeUpEvent instance
            drone: An Device instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(drone, Device)
        assert isinstance(wake_up_event, WakeUpEvent)

        stub = ControlServiceEventsStub(self.channel)

        if wake_up_event == WakeUpEvent.WAKE_UP_DONE:
            response = stub.Wake_Up_Done(drone)
        return response


class TakeOffEventEmitter(_ControlServiceEmiter):
    def emit(self, take_off_event, drone):
        """
        Args:
            take_off_event: An TakeOffEvent instance
            drone: An Device instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(drone, Device)
        assert isinstance(take_off_event, TakeOffEvent)

        stub = ControlServiceEventsStub(self.channel)

        if take_off_event == TakeOffEvent.TAKE_OFF_CONNECTED_BUT_FAILED:
            response = stub.Take_Off_Connected_But_Failed(drone)
        elif take_off_event == TakeOffEvent.TAKE_OFF_CONNECTION_FAILED:
            response = stub.Take_Off_Connection_Failed(drone)
        elif take_off_event == TakeOffEvent.TAKE_OFF_DONE:
            response = stub.Take_Off_Done(drone)
        return response


class GoUpEventEmitter(_ControlServiceEmiter):
    def emit(self, go_up_event, drone):
        """
        Args:
            go_up_event: An GoUpEvent instance
            drone: An Device instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(drone, Device)
        assert isinstance(go_up_event, GoUpEvent)

        stub = ControlServiceEventsStub(self.channel)

        if go_up_event == GoUpEvent.GO_UP_FAILED:
            response = stub.Go_Up_Failed(drone)
        elif go_up_event == GoUpEvent.GO_UP_SET_SETTINGS_FAILED:
            response = stub.Go_Up_Set_Settings_Failed(drone)
        elif go_up_event == GoUpEvent.GO_UP_SET_SETTINGS_DONE:
            response = stub.Go_Up_Set_Settings_Done(drone)
        elif go_up_event == GoUpEvent.GO_UP_DONE:
            response = stub.Go_Up_Done(drone)
        return response

# ------------------------ Actions emitters ------------------------------#


class TakeOffActionEmitter(_ControlServiceEmiter):
    def emit(self, take_off_action, drone):
        """
        Args:
            take_off_action: An TakeOffAction instance
            drone: An Device instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(drone, Device)
        assert isinstance(take_off_action, TakeOffAction)

        stub = ControlServiceActionsStub(self.channel)

        if take_off_action == TakeOffAction.START_TAKE_OFF:
            response = stub.StartTakeoff(drone)
        return response


class GoUpActionEmitter(_ControlServiceEmiter):
    def emit(self, go_up_action, go_up_message):
        """
        Args:
            go_up_action: An GoUpAction instance
            go_up_message: An GoUpMessage instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(go_up_message, GoUpMessage)
        assert isinstance(go_up_action, GoUpAction)

        stub = ControlServiceActionsStub(self.channel)

        if go_up_action == GoUpAction.START_GO_UP:
            response = stub.StartGoUp(go_up_message)
        return response


class ArasEventEmitter(_ControlServiceEmiter):
    def emit(self, aras_event, start_info):
        """
        Args:
            aras_event: An ArasEvent instance
            start_info: An StartInfo instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(aras_event, ArasEvent)
        assert isinstance(start_info, StartInfo)

        stub = ControlServiceEventsStub(self.channel)

        if aras_event == ArasEvent.START_CONTROL_SERVICE_REQUESTED:
            response = stub.StartControlService(start_info)
        if aras_event == ArasEvent.STOP_CONTROL_SERVICE_REQUESTED:
            response = stub.StopControlService(Empty())


class MissionActionEmitter(_ControlServiceEmiter):
    def emit(self, mission_action, mission_data):
        """
        Args:
            mission_action: An MissionAction instance
            mission_data: An MissionData instance
        """
        assert "Channel must be READY", self.channel is not None
        assert isinstance(mission_data, MissionData)
        assert isinstance(mission_action, MissionAction)

        stub = ControlServiceActionsStub(self.channel)

        if mission_data == MissionAction.START_MISSION:
            response = stub.StartMission(mission_data)
        return response
