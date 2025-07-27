"""
This is the main entrypoint
"""

from fastap import FastAPI, HTTPException, status
from .db import models
from .api import api

VERSION=1.0
app = fastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return "OK"

@app.get("/status", status_code=status.HTTP_200_OK)
def get_stores():
    return { "status": "healthy", "version":VERSION }

# Stores
@app.get("/stores/{store_id}")
def get_store():
    req = api.store_by_id(store_id)
    if req != {}:
        return req
    raise HTTPException( status_code=status.HTTP_404_NOT_FOUND)

@app.post("/stores", status_code=status.HTTP_201_CREATED)
def add_store(store: models.Store):
    try:
        api.add_new_store( store )
    except HTTPException as ex:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail=err ) from None

@app.delete("/store/{store_id}", status_code=status.HTTP_201_CREATED)
def delete_store(store_id: int ):
    try:
        api.delete_store(store_id)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="store not found ") from None
    except Exceltion as ex:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail=ex) from None

        
