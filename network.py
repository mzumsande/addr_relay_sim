import random

NUM_FULL_OUTBOUND = 8
MAX_INBOUNDS = 117


class Network:
    nodes = []

    def __init__(self, nListen, nPrivate):
        # print("Start Creating Network")
        self.nodes = []
        self.size = nListen
        for i in range(nListen):
            node = Node(i)
            self.nodes.append(node)

        # TODO: Implement more peaked degree distributions - should be more realistic
        for i in range(nListen):
            self.add_peers(i, nListen)

        for i in range(nPrivate):
            curNode = nListen + i
            node = Node(curNode)
            self.nodes.append(node)
            self.add_peers(curNode, nListen)

    def add_peers(self, id, nListen):
        numOb = 0
        while(numOb < NUM_FULL_OUTBOUND):
            peer = random.randint(0, nListen-1)
            if (peer != id and len(self.nodes[peer].inbounds) <= MAX_INBOUNDS and peer not in self.nodes[id].outbounds and peer not in self.nodes[id].inbounds):
                self.nodes[id].outbounds.add(peer)
                self.nodes[peer].inbounds.add(id)
                numOb = numOb + 1


class Node:
    def __init__(self, id):
        self.id = id
        self.inbounds = set()
        self.outbounds = set()
