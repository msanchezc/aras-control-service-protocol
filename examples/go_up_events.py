from aras_control_service_protocol.emitters import GoUpEventEmitter
from aras_control_service_protocol.events import GoUpEvent
from aras_control_service_protocol.messages import Device

CONTROL_SERVICE_IP = "localhost:50052"
DRONE_ID = "apolo"

drone = Device(
    type=Device.DeviceType.DRONE,
    id=DRONE_ID)

go_up_emitter = GoUpEventEmitter(CONTROL_SERVICE_IP)

go_up_emitter.emit(GoUpEvent.GO_UP_SET_SETTINGS_FAILED, drone)
go_up_emitter.emit(GoUpEvent.GO_UP_SET_SETTINGS_DONE, drone)
go_up_emitter.emit(GoUpEvent.GO_UP_FAILED, drone)
go_up_emitter.emit(GoUpEvent.GO_UP_DONE, drone)
