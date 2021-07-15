import json
import socket


# CAPI host and port
CAPI_HOST = ''
CAPI_PORT = 0101


class Client(object):
    def __init__(self, host, port, max_retry_number=5):
        self.host = host
        self.port = port
        self.sock = None
        self.max_retry_number = max_retry_number

    def request(self, request):
        request = bytes(request, "utf-8")
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
                    response_chunks.append(chunk.decode("utf-8"))
                    if chunk.endswith(b'\n'):
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


def form_request(text):
    """
    Form a proper request for CAPI. Ask for tokens only.
    :param text: list of str (sentences)
    :return: dict
    """
    return {"action": "parse",
            "splitIntoParagraphs": False,
            "splitIntoSentences": False,
            "disableLanguageFilters": True,
            "useSpaceTokenizer": False,
            "requestedFields": ["toks", "posTags"],
            "texts": text}


def tokenize(text):
    """
    Connect to the CAPI server, send a request and get a response.
    :param text: list of str (sentences)
    :return: list of lists of str (tokenized sentences)
    """
    server = Client(CAPI_HOST, CAPI_PORT)
    request = json.dumps(form_request(text))
    response = json.loads(server.request(request + '\n'))
    tokenized = []
    for j in range(len(response['texts'])):
        tokenized.append([i['text'] for i in
                          response['texts'][j]['paragraphs'][0]['sentences'][0]['toks']])
    return tokenized


def tag_text(text):
    """
    Connect to the CAPI server, send a request and get a response.
    :param text: list of str (sentences)
    :return: list of lists of tuples (word, tag)
    """
    server = Client(CAPI_HOST, CAPI_PORT)
    request = json.dumps(form_request(text))
    response = json.loads(server.request(request + '\n'))
    # print(response)
    tagged = []
    # print(response['texts'])
    for j in range(len(response['texts'])):
        k = response['texts'][j]['paragraphs'][0]['sentences'][0]['toks']
        tagged.append([(w["text"].lower(), w["tag"]) for w in k])
    return tagged

