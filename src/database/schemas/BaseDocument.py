from bson.errors import InvalidId
from bson.objectid import ObjectId
from pydantic import BaseModel, BaseConfig, Field
import datetime
import uuid

class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


class BaseDocument(BaseModel):
    id: OID = Field(str(uuid.uuid4()), alias='_id')
    created_timestamp: datetime.datetime = Field(datetime.datetime.utcnow(), alias='_ts')

    class Config(BaseConfig):
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda oid: str(oid),
        }