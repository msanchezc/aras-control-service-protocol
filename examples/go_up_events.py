from aras_control_service_protocol.emitters import GoUpEventEmitter
from aras_control_service_protocol.events import GoUpEvent
from aras_control_service_protocol.messages import DroneIdentifier

CONTROL_SERVICE_IP = "localhost:50052"

drone_identifier = DroneIdentifier(
    owner_id="lab", base_id="base_lab", drone_id="apolo")

go_up_emitter = GoUpEventEmitter(CONTROL_SERVICE_IP)

go_up_emitter.emit(GoUpEvent.GO_UP_SET_SETTINGS_FAILED, drone_identifier)
go_up_emitter.emit(GoUpEvent.GO_UP_SET_SETTINGS_DONE, drone_identifier)
go_up_emitter.emit(GoUpEvent.GO_UP_FAILED, drone_identifier)
go_up_emitter.emit(GoUpEvent.GO_UP_DONE, drone_identifier)
