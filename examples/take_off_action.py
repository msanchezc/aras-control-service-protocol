from aras_control_service_protocol.emitters import TakeOffActionEmitter
from aras_control_service_protocol.actions import TakeOffAction
from aras_control_service_protocol.messages import Drone, DroneIdentifier

CONTROL_SERVICE_IP = "localhost:50052"
ACCESS_DATA = {"ip": "192.168.50.158"}

drone_identifier = DroneIdentifier(
    owner_id="lab", base_id="base_lab", drone_id="apolo")

drone = Drone(identifier=drone_identifier,
              access_data=str(ACCESS_DATA),
              control_service_ip=CONTROL_SERVICE_IP)

take_off_action_emitter = TakeOffActionEmitter(CONTROL_SERVICE_IP)
take_off_action_emitter.emit(TakeOffAction.START_TAKE_OFF, drone)
