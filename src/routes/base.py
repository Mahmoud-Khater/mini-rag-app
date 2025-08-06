from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter(
	prefix="/api/v1",
	tags=["rag"],
)

@base_router.get("/")
async def welcome():
	app_name = os.getenv('APP_NAME')
	return {
		"APP_NAME" : app_name
	}