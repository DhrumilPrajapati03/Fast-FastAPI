# from typing import Any
# from fastapi import FastAPI, status, HTTPException
# from scalar_fastapi import get_scalar_api_reference
# from .schemas import Shipment, ShipmentStatus

# app = FastAPI()

# shipments = {
#     12701:{
#         "weight": 1.5,
#         "content":"wooden desk",
#         "status" :"placed"
#     },
#     12702:{
#         "weight": 2.3,
#         "content":"metal chair",
#         "status" :"shipped"
#     },
#     12703:{
#         "weight": 0.8,
#         "content":"glass vase",
#         "status" :"delivered"
#     },
#     12704:{
#         "weight": 3.1,
#         "content":"plastic container",
#         "status" :"pending"
#     },
#     12705:{
#         "weight": 4.0,
#         "content":"electronics kit",
#         "status" :"in transit"
#     },
#     12706:{
#         "weight": 5.7,
#         "content":"office supplies",
#         "status" :"processing"
#     },
#     12707:{
#         "weight": 6.2,
#         "content":"fabric bolts",
#         "status" :"placed"
#     }
# }


# @app.get("/shipment/latest", status_code=status.HTTP_200_OK)
# def get_latest_shipment()->dict[str, Any]:
#     id = max(shipments.keys())
#     return shipments[id]

# # @app.get("/shipment/{field}")
# # def get_shipment_field(field: str, id: int) -> Any:
# #     return shipments[id][field]

# @app.get("/shipment/{id}")
# def get_shipment(id:int)->dict[str, Any]:

#     if id not in shipments:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="given id doen't exists!!"
#         )
#     return shipments[id]    


# @app.post("/shipment")
# def submit_shipment(shipment: Shipment)-> dict[str, int]:
#     # content = data["content"]
#     # weight = data["weight"]
#     # if weight > 25:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_406_NOT_ACCEPTABLE,
#     #         detail="Maximum weight is 25kg"
#     #     )
    
#     new_id = max(shipments.keys())+1

#     shipments[new_id] = {
#         "content" : shipment.content,
#         "weight"  : shipment.weight,
#         "destination" : shipment.destination,
#         "status"  : "placed"
#     }

#     return {"id": new_id}    

# # @app.put("/shipment")
# # def shipment_update(id: int, content:str, weight: float, status: str)-> dict[str, Any]:
# #     shipments[id] ={
# #         "content": content,
# #         "weight" : weight,
# #         "status": status
# #     }
# #     return shipments[id]

# @ app.patch("/shipment")
# def patch_shipment(id: int,body:dict[str, ShipmentStatus])->dict[str, Any]:#id: int, content: str | None= None, weight: float| None= None, status: str|None= None):
#     # shipment = shipments[id]
#     # if content:
#     #     shipment["content"] = content
#     # if weight:
#     #     shipment["weight"] = weight
#     # if status:
#     #     shipment["status"] = status
#     shipments[id].update(body)
#     # shipments[id] = shipment
#     return shipments[id]

# @app.delete("/shipment")
# def delete_shipment(id: int)-> dict[str, str]:
#     shipments.pop(id)
#     return {"detail": f"shipment with id #{id} is deleted!"}
# # @app.get("/shipment/latest")
# # def get_latest_shipment()->dict[str, Any]:
# #     return{
# #         "id": 25643,
# #         "weight": 1.5,
# #         "content":"wooden desk",
# #         "status" :"placed"
# #     }

# # @app.get("/shipment/{id}")
# # def get_shipment(id:int|float)->dict[str, Any]:
# #     return{
# #         "id": id,
# #         "weight": 1.2,
# #         "content":"wooden table",
# #         "status" :"in transit"
# #     }

# @app.get("/scalar", include_in_schema=False)
# def get_scalar_docs():
#     return get_scalar_api_reference(
#         openapi_url=app.openapi_url,
#         title="Scalar API"
#     )

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from .database import shipments, save

app = FastAPI()

### Shipments datastore as dict
shipments = {
    12701: {"weight": 8.2, "content": "aluminum sheets", "status": "placed", "destination": 11002},
    12702: {"weight": 14.7, "content": "steel rods", "status": "shipped", "destination": 11003},
    12703: {"weight": 11.4, "content": "copper wires", "status": "delivered", "destination": 11002},
    12704: {"weight": 17.8, "content": "iron plates", "status": "in transit", "destination": 11005},
    12705: {"weight": 10.3, "content": "brass fittings", "status": "returned", "destination": 11008},
}


###  a shipment by id
@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int):
    # Check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipments[id]


### Create a new shipment with content and weight
@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate) -> dict[str, int]:
    # Create and assign shipment a new id
    new_id = max(shipments.keys()) + 1
    # Add to shipments dict
    shipments[new_id] = {
        **shipment.model_dump(),
        "id": new_id,
        "status": "placed",
    }
    # Return id for later use
    return {"id": new_id}


### Update fields of a shipment
@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, body: ShipmentUpdate):
    # Update data with given fields
    shipments[id].update(body.model_dump(exclude_none=True))
    save()
    return shipments[id]


### Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    # Remove from datastore
    shipments.pop(id)

    return {"detail": f"Shipment with id #{id} is deleted!"}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
