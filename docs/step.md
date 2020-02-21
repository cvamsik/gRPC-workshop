## Steps:

1. Inside the work directory, create a proto file with messages and methods. It's best to keep proto files separated 
  inside a directory
  ```
    eg:
    
    syntax="proto3";

    // The greeting service definition.
    service Greeter {
      // Sends a greeting
      rpc SayHello (HelloRequest) returns (HelloReply) {}
    }

    // The request message containing the user's name.
    message HelloRequest {
      string name = 1;
    }

    // The response message containing the greetings
    message HelloReply {
      string message = 1;
    }
   ```
    
2. Generate client and server side codes for specific language.
```
    Python example(example.proto is inside the protos directory):
    python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/example.proto
```

3. Create the server and specify the port.

4. Create the client with channel listening to the server port. Create the client stub and call the server method.

5. Start the server

6. Run the client code
