from aras_control_service_protocol.emitters import TakeOffActionEmitter
from aras_control_service_protocol.actions import TakeOffAction
from aras_control_service_protocol.messages import Device

DRONE_ID = "apolo"
ACCESS_DATA = {"ip": "192.168.50.158"}


drone = Device(
    type=Device.DeviceType.DRONE,
    id=DRONE_ID,
    access_data=str(ACCESS_DATA))

take_off_action_emitter = TakeOffActionEmitter(CONTROL_SERVICE_IP)
take_off_action_emitter.emit(TakeOffAction.START_TAKE_OFF, drone)
