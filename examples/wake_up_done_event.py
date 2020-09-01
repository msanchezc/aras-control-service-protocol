from aras_control_service_protocol.emitters import WakeUpEventEmitter
from aras_control_service_protocol.events import WakeUpEvent
from aras_control_service_protocol.messages import Device

CONTROL_SERVICE_IP = "localhost:50052"
DRONE_ID = "APOLO"

drone = Device(
    type=Device.DeviceType.DRONE,
    id=DRONE_ID)

wake_up_event_emitter = WakeUpEventEmitter(CONTROL_SERVICE_IP)
wake_up_event_emitter.emit(
    WakeUpEvent.WAKE_UP_DONE, drone)
