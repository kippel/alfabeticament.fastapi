from sqlalchemy.orm import Session
from fastapi.params import Depends
from db.database import get_db

from db.models import Monosillabs, MonoUser


class Seeds:

    @staticmethod
    def seed_monosilleb(db: Session = Depends(get_db)):
        
        monosillabs = db.query(Monosillabs).all()
        
        for r in monosillabs:
            
            db.delete(r)
            db.commit()

    @staticmethod
    def seed_monouser(db: Session = Depends(get_db)):
        monouser = db.query(MonoUser).all()
        
        for r in monouser:
            print(r)
            db.delete(r)
            db.commit()
        
    
    @staticmethod
    def seed_monosilleb_bar(monosillabs: list ,db: Session = Depends(get_db)):
        
        for r in monosillabs:
            
            mon = Monosillabs(
                nom=r['name'],
                order=r['order']
            )
            db.add(mon)
            db.commit()

    @staticmethod
    def seed_monouser_bar(monouser: list ,db: Session = Depends(get_db)):
        
        for r in monouser:
            
            mon = MonoUser(
                nom=r['nom'],
                icon=r['icon'],
                owner_id=r['owner_id']
            )
            db.add(mon)
            db.commit()