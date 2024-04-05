from fastapi import APIRouter

router = APIRouter()


@router.post("/", status_code=201)
async def create_contact_endpoint():
    pass


@router.get("/{contact_id}")
async def read_contact_endpoint():
    pass


@router.get("/", response_model_exclude_none=True)
async def read_contacts_endpoint():
    pass
