from aras_control_service_protocol.emitters import TakeOffActionEmitter
from aras_control_service_protocol.actions import TakeOffAction
from aras_control_service_protocol.messages import Drone, DroneAccessData, DroneIdentifier, GoUpMessage

CONTROL_SERVICE_IP = "localhost:50052"

drone_identifier = DroneIdentifier(
    owner_id="lab", base_id="base_lab", drone_id="apolo")
drone_access_data = DroneAccessData(data='{"hello": world}')
drone = Drone(identifier=drone_identifier, access_data=drone_access_data)
go_up_message = GoUpMessage(drone=drone, altitude=20, roll=5)

take_off_action_emiter = TakeOffActionEmitter(CONTROL_SERVICE_IP)
take_off_action_emiter.emit(TakeOffAction.START_TAKE_OFF, drone)
