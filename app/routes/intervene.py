from fastapi import APIRouter
from cognis.reasoning.intervention import generate_intervention

router = APIRouter()

@router.post("/")
def intervene():
    docs = router.state.retriever.invoke("")
    top = docs[0].page_content

    intervention = generate_intervention(
        pattern=top,
        frequency=3
    )

    return {"intervention": intervention}
