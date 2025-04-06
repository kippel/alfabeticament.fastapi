from fastapi import APIRouter, HTTPException
# db
from sqlalchemy.orm import Session
from fastapi.params import Depends
from db.database import get_db
from db.models import User, Monosillabs

router = APIRouter()

@router.get("/test")
def getTest(db: Session = Depends(get_db)):

    user = db.query(User).all()
    print(user)
    
    return {"test": "foo"}


@router.get("/api/monosillabs")
async def getMonosillabs(db: Session = Depends(get_db)):
    """
    Get monosillabs
    """
    monosillabs = db.query(Monosillabs).all()
    
    if not monosillabs:
        raise HTTPException(status_code=404, detail="No monosillabs found")
    
    return {"monosillabs": monosillabs}