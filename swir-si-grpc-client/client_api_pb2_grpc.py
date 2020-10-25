# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import client_api_pb2 as client__api__pb2
import common_structs_pb2 as common__structs__pb2


class PubSubApiStub(object):
    """The definition of API exposed by Sidecar.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/swir_public.PubSubApi/Publish',
                request_serializer=client__api__pb2.PublishRequest.SerializeToString,
                response_deserializer=client__api__pb2.PublishResponse.FromString,
                )
        self.PublishBiStream = channel.stream_stream(
                '/swir_public.PubSubApi/PublishBiStream',
                request_serializer=client__api__pb2.PublishRequest.SerializeToString,
                response_deserializer=client__api__pb2.PublishResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/swir_public.PubSubApi/Subscribe',
                request_serializer=client__api__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=client__api__pb2.SubscribeResponse.FromString,
                )


class PubSubApiServicer(object):
    """The definition of API exposed by Sidecar.
    """

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishBiStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PubSubApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=client__api__pb2.PublishRequest.FromString,
                    response_serializer=client__api__pb2.PublishResponse.SerializeToString,
            ),
            'PublishBiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.PublishBiStream,
                    request_deserializer=client__api__pb2.PublishRequest.FromString,
                    response_serializer=client__api__pb2.PublishResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=client__api__pb2.SubscribeRequest.FromString,
                    response_serializer=client__api__pb2.SubscribeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'swir_public.PubSubApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PubSubApi(object):
    """The definition of API exposed by Sidecar.
    """

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/swir_public.PubSubApi/Publish',
            client__api__pb2.PublishRequest.SerializeToString,
            client__api__pb2.PublishResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishBiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/swir_public.PubSubApi/PublishBiStream',
            client__api__pb2.PublishRequest.SerializeToString,
            client__api__pb2.PublishResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/swir_public.PubSubApi/Subscribe',
            client__api__pb2.SubscribeRequest.SerializeToString,
            client__api__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class PersistenceApiStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Store = channel.unary_unary(
                '/swir_public.PersistenceApi/Store',
                request_serializer=client__api__pb2.StoreRequest.SerializeToString,
                response_deserializer=client__api__pb2.StoreResponse.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/swir_public.PersistenceApi/Retrieve',
                request_serializer=client__api__pb2.RetrieveRequest.SerializeToString,
                response_deserializer=client__api__pb2.RetrieveResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/swir_public.PersistenceApi/Delete',
                request_serializer=client__api__pb2.DeleteRequest.SerializeToString,
                response_deserializer=client__api__pb2.DeleteResponse.FromString,
                )


class PersistenceApiServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Store(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersistenceApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Store': grpc.unary_unary_rpc_method_handler(
                    servicer.Store,
                    request_deserializer=client__api__pb2.StoreRequest.FromString,
                    response_serializer=client__api__pb2.StoreResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=client__api__pb2.RetrieveRequest.FromString,
                    response_serializer=client__api__pb2.RetrieveResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=client__api__pb2.DeleteRequest.FromString,
                    response_serializer=client__api__pb2.DeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'swir_public.PersistenceApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersistenceApi(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Store(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/swir_public.PersistenceApi/Store',
            client__api__pb2.StoreRequest.SerializeToString,
            client__api__pb2.StoreResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/swir_public.PersistenceApi/Retrieve',
            client__api__pb2.RetrieveRequest.SerializeToString,
            client__api__pb2.RetrieveResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/swir_public.PersistenceApi/Delete',
            client__api__pb2.DeleteRequest.SerializeToString,
            client__api__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class ServiceInvocationApiStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Invoke = channel.unary_unary(
                '/swir_public.ServiceInvocationApi/Invoke',
                request_serializer=common__structs__pb2.InvokeRequest.SerializeToString,
                response_deserializer=common__structs__pb2.InvokeResponse.FromString,
                )


class ServiceInvocationApiServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Invoke(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceInvocationApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Invoke,
                    request_deserializer=common__structs__pb2.InvokeRequest.FromString,
                    response_serializer=common__structs__pb2.InvokeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'swir_public.ServiceInvocationApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServiceInvocationApi(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/swir_public.ServiceInvocationApi/Invoke',
            common__structs__pb2.InvokeRequest.SerializeToString,
            common__structs__pb2.InvokeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
