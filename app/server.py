from typing import Callable, Any

routes: dict[str, Callable[[Any], Any]] = {}

def route(path: str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route

@route("/shipment")
def get_shipment():
    return "Shipment<1001, in transit>"

requests: str = ""

while requests != "quit":
    requests = input("> ")

    if requests in routes:
        response = routes[requests]()
        print(response, end="\n\n")
    else:
        print("Not Found")