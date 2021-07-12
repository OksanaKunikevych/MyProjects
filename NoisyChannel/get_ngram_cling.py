import json
import socket

# CAPI host and port
CAPI_HOST = 'ngrams.grammarly.com'
CAPI_PORT = 19999


class Client(object):
    def __init__(self, host, port, max_retry_number=5):
        self.host = host
        self.port = port
        self.sock = None
        self.max_retry_number = max_retry_number

    def request(self, request):
        retry_number = -1
        while True:
            try:
                self.sock.sendall(request)
                response_chunks = []
                while True:
                    chunk = self.sock.recv(4096)
                    if not chunk:
                        # print request
                        raise socket.error
                    response_chunks.append(chunk)
                    if chunk.endswith('\n'):
                        return ''.join(response_chunks)
            except (socket.error, AttributeError) as e:
                while True:
                    if retry_number >= self.max_retry_number and \
                                    type(e) is socket.error:
                        raise
                    self.sock = socket.socket()
                    try:
                        self.sock.connect((self.host, self.port))
                    except socket.error as e:
                        continue
                    retry_number += 1
                    break

def get_ngram(request):
    """
    Connect to the CAPI server, send a request and get a response.
    :param text: list of str (sentences)
    :return: list of lists of str (tokenized sentences)
    """
    server = Client(CAPI_HOST, CAPI_PORT)
    response = server.request(request + '\n')
    return response

# print get_ngram("freq:at school"),
# print get_ngram("freq:in school")
# print get_ngram("prob: school")
# print get_ngram("prob:in school")
# print get_ngram("cprob:at school"),
# print get_ngram("cprob:in school")
