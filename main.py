import zmq
from build.gen import openprio_pt_position_data_pb2
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Connect with NDOVLoket")
socket.connect("tcp://pubsub.besteffort.ndovloket.nl:7668")

# Subscribe on openprio messages.
socket.setsockopt_string(zmq.SUBSCRIBE, "/openprio")

def print_content_openprio(msg):
    s, ms = divmod(msg.timestamp, 1000)
    position = "{}".format(msg.position).replace("\n", " ")
    timestamp = "{}.{:03d}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(s)), ms)
    output = "send %s [Vervoerder: %s, Grootwagennummer: %s] positie: %s" % (timestamp, 
        msg.vehicle_descriptor.data_owner_code, msg.vehicle_descriptor.vehicle_number, position)
    print(output)

while True:
    multipart = socket.recv_multipart()
    openprio_message = openprio_pt_position_data_pb2.LocationMessage()
    openprio_message.ParseFromString(multipart[1])
    print_content_openprio(openprio_message)