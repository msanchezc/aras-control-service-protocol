from aras_control_service_protocol.emitters import GoUpActionEmitter
from aras_control_service_protocol.actions import GoUpAction
from aras_control_service_protocol.messages import Drone, DroneIdentifier, GoUpMessage

CONTROL_SERVICE_IP = "localhost:50052"
ACCESS_DATA = {"ip": "192.168.50.158"}

drone_identifier = DroneIdentifier(
    owner_id="lab", base_id="base_lab", drone_id="apolo")

drone = Drone(identifier=drone_identifier,
              access_data=str(ACCESS_DATA),
              control_service_ip=CONTROL_SERVICE_IP)

go_up_message = GoUpMessage(drone=drone, altitude=20, roll=5)

go_up_action_emitter = GoUpActionEmitter(CONTROL_SERVICE_IP)
go_up_action_emitter.emit(GoUpAction.START_GO_UP, go_up_message)
