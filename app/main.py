from typing import Any
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

shipments = {
    12701:{
        "weight": 1.5,
        "content":"wooden desk",
        "status" :"placed"
    },
    12702:{
        "weight": 2.3,
        "content":"metal chair",
        "status" :"shipped"
    },
    12703:{
        "weight": 0.8,
        "content":"glass vase",
        "status" :"delivered"
    },
    12704:{
        "weight": 3.1,
        "content":"plastic container",
        "status" :"pending"
    },
    12705:{
        "weight": 4.0,
        "content":"electronics kit",
        "status" :"in transit"
    },
    12706:{
        "weight": 5.7,
        "content":"office supplies",
        "status" :"processing"
    },
    12707:{
        "weight": 6.2,
        "content":"fabric bolts",
        "status" :"placed"
    }
}


@app.get("/shipment/latest")
def get_latest_shipment()->dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

@app.get("/shipment/{id}")
def get_shipment(id:int|float)->dict[str, Any]:

    if id not in shipments:
        return {"detail":"given id doen't exists!!"}
    return shipments[id]    
# @app.get("/shipment/latest")
# def get_latest_shipment()->dict[str, Any]:
#     return{
#         "id": 25643,
#         "weight": 1.5,
#         "content":"wooden desk",
#         "status" :"placed"
#     }

# @app.get("/shipment/{id}")
# def get_shipment(id:int|float)->dict[str, Any]:
#     return{
#         "id": id,
#         "weight": 1.2,
#         "content":"wooden table",
#         "status" :"in transit"
#     }

# @app.get("/scalar", include_in_schema=False)
# def get_scalar_docs():
#     return get_scalar_api_reference(
#         openapi_url=app.openapi_url,
#         title="Scalar API"
#     )