import grpc
import greet_pb2_grpc
import greet_pb2
from concurrent import futures

class Greeter(greet_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return greet_pb2.HelloReply(message='Hello, %s!' % request.name)

    # def SayHelloAgain(self, request, context):
    #     return greet_pb2_grpc.HelloReply(message='Hello again, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()