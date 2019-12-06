import hashlib
import requests

import sys
import json

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """
    start = timer()

    r = requests.get(url=node + "/full_chain")
    data = r.json()

    my_rand = random.random()
    my_multi = 10 ** random.randint(0,18)
    proof = my_rand * my_multi
    # print(f"start proof: {proof}")
    #  TODO: Your code here
    while valid_proof(last_proof, proof) is False:
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!
    prev_proof = f"{last_hash}".encode()
    prev_proof_hash = hashlib.sha256(prev_proof).hexdigest()
    
    new_proof = f"{proof}".encode()
    new_proof_hash = hashlib.sha256(new_proof).hexdigest()
    
    # if new_proof_hash[:6] == prev_proof_hash[-6:]:
    #     print("\n~~~~~~~~~~~~~~~~~~\n")
    #     print(f'last 6: {prev_proof_hash[-6:]} | first 6: {new_proof_hash[:6]}')
    #     print("\n~~~~~~~~~~~~~~~~~~\n")
        
    return new_proof_hash[:6] == prev_proof_hash[-6:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
