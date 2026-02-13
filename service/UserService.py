class UserService:
    def __init__(self,dbType: str):
        self.dbType = dbType
    
    def get_user(self, user_id: int):
        if(self.dbType == "mysql"):
            return {"user_mysql_id": user_id}
        return {"user_id": user_id}

def get_user_service(dbType: str):
    return UserService(dbType)