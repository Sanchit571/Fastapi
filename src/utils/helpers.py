import jwt 
from src.utils.settings import settings 
from datetime import datetime
from fastapi import HTTPException , status , Request , Depends
from src.user.models import UserModel
from jwt.exceptions import InvalidTokenError
from src.utils.db import get_db
from sqlalchemy.orm import Session 



def is_authenticated(request : Request , db : Session = Depends(get_db)):
    try :
        token = request.headers.get("authorization")
        token = token.split(" ")[-1]

        data = jwt.decode(token , settings.SECRET_KEY , settings.ALGORITHM)
        user_id = data.get("id")
        exp_time = data.get("exp")


        current_time = datetime.now().timestamp()

        if current_time > exp_time :
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "Your session has expiered")

        user = db.query(UserModel).filter(UserModel.id == request.id).first()
        if not user: 
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "You are unauthorized")

        return user 
 
    except InvalidTokenError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "You are unauthorized")
