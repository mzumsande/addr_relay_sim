import random

from network import Network

NUM_LISTEN_NODES = 10000
NUM_PRIV_NODES = 50000
NUM_HOPS = 20
NUM_SAMPLES = 5
NUM_NODES = NUM_LISTEN_NODES + NUM_PRIV_NODES


def sim_addr_relay(network, bh_freq):
    # print("Starting addr relay")
    # step 1: a private node self-advertises
    startnode = network.nodes[NUM_LISTEN_NODES + random.randint(0, NUM_PRIV_NODES-1)]
    processNodes = set(startnode.outbounds)
    tempSet = set()
    knowsAddr = [0]*NUM_NODES

    for i in range(NUM_HOPS):
        for n in processNodes:
            # already processed? Then skip
            if(knowsAddr[n] == 1):
                continue
            knowsAddr[n] = 1
            allPeers = network.nodes[n].outbounds | network.nodes[n].inbounds
            relay_to = random.sample(allPeers, 2)
            for r in relay_to:
                if(random.uniform(0, 1) > bh_freq):
                    tempSet.add(r)
        processNodes = tempSet.copy()
        tempSet.clear()
    return knowsAddr.count(1)/NUM_NODES


def main():
    bh_values = [0.0, 0.1, 0.2, 0.3, 0.35, 0.4]
    print("#blackholes nodes_reached")
    for bh_freq in bh_values:
        samples = []
        for i in range(NUM_SAMPLES):
            network = Network(NUM_LISTEN_NODES, NUM_PRIV_NODES)
            pct = sim_addr_relay(network, bh_freq)
            samples.append(pct)
        print(f"{bh_freq} {sum(samples)/NUM_SAMPLES}")


if __name__ == "__main__":
    main()
