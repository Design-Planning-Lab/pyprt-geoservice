import argparse
import os
import json
from setbackPerEdge import prt,main



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", "--path", type=str, required=True)
    args = parser.parse_args()

    assert os.path.exists(args.path), "invalid path provided"

    prt.initialize_prt()
    assert prt.is_prt_initialized()
    with open(args.path, "r") as fp:
        data = {"geometry": json.load(fp), "rpkName": "SetbackPerEdge"}
        res = main(data)
    for i in res:
        print(i)
    prt.shutdown_prt()
