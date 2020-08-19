from aras_control_service_protocol.emitters import TakeOffEventEmitter
from aras_control_service_protocol.events import TakeOffEvent
from aras_control_service_protocol.messages import DroneIdentifier

CONTROL_SERVICE_IP = "localhost:1234"

drone_identifier = DroneIdentifier(
    owner_id="lab", base_id="base_lab", drone_id="apolo")

take_off_emiter = TakeOffEventEmitter(CONTROL_SERVICE_IP)
take_off_emiter.emit(
    TakeOffEvent.TAKE_OFF_CONNECTED_BUT_FAILED, drone_identifier)
take_off_emiter.emit(TakeOffEvent.TAKE_OFF_CONNECTION_FAILED, drone_identifier)
take_off_emiter.emit(TakeOffEvent.TAKE_OFF_DONE, drone_identifier)
