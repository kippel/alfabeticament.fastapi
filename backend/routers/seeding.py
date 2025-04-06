from fastapi import APIRouter, HTTPException
# db
from sqlalchemy.orm import Session
from fastapi.params import Depends
from db.database import get_db

from run import BASE_DIR

from db.models import Monosillabs
import yaml

from seed.seed import Seeds

router = APIRouter()

@router.get("/test/monosillabs")
def getMonosillabs(db: Session = Depends(get_db)):
    

    Seeds.seed_monosilleb(db)
    Seeds.seed_monouser(db)
    with open("seed/config.yaml", 'r') as file:
        config = yaml.safe_load(file)

    Seeds.seed_monosilleb_bar(config['monosillabs'], db)
    
    Seeds.seed_monouser_bar(config['monouser'], db)
    
    
    return {"monosillabs": "monosillabs"}