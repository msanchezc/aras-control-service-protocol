#!/usr/bin/bash
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/aras_control_service_protocol.proto
