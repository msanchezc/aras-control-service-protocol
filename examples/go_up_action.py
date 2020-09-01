from aras_control_service_protocol.emitters import GoUpActionEmitter
from aras_control_service_protocol.actions import GoUpAction
from aras_control_service_protocol.messages import Device, GoUpMessage

CONTROL_SERVICE_IP = "localhost:50052"
ACCESS_DATA = {"ip": "192.168.50.158"}

drone = Device(
    type=Device.DeviceType.DRON, id=DRONE_ID,
    access_data=str(ACCESS_DATA))

go_up_message = GoUpMessage(drone=drone, altitude=20, roll=5)

go_up_action_emitter = GoUpActionEmitter(CONTROL_SERVICE_IP)
go_up_action_emitter.emit(GoUpAction.START_GO_UP, go_up_message)
