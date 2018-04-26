# python3


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.last_finish_time = 0
        self.finish_time = []
        self.data = []

    def process_packet(self, request):
        while (len(self.data) > 0) \
                and (self.finish_time[len(self.data)-1] <= request.arrival_time):
            self.data.pop()
            self.finish_time.pop()

        if len(self.data) == self.size:
            response = Response(True, -1)
        else:
            self.data.insert(0, request)
            if self.last_finish_time < request.arrival_time:
                begin_process_time = request.arrival_time
            else:
                begin_process_time = self.last_finish_time
            response = Response(False, begin_process_time)
            self.finish_time.insert(0, begin_process_time + request.process_time)
            self.last_finish_time += (begin_process_time - self.last_finish_time) + request.process_time

        return response


def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process_packet(request))
    return responses


def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = read_requests(count)

    buffer = Buffer(size)
    responses = process_requests(requests, buffer)

    print_responses(responses)
