from fastapi import APIRouter,Request

router = APIRouter()

@router.get("/clientInfo")
def clientInfo(request: Request):
    return {
        "ip": request.client.host,
        "port": request.client.port,
        "headers": dict(request.headers),
        "cookies": dict(request.cookies)
    }