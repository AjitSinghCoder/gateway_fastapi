from pydantic import  BaseModel
from typing import Optional


class Profile(BaseModel):
    profile_type: str
    profile_first_name: str
    # profile_last_name: str
    profile_user_name: str
    profile_email_id: str
    profile_password: str
    
class PrimaryDetails(BaseModel):
    pk: str
    sk: str
    FIRST_NAME: str
    LAST_NAME: str
    USER_NAME: str
    COMPANY: str
    IMAGE: str
    IMAGE_THUMBNAIL: str
    
class Contact(BaseModel):
    pk: str
    sk: str
    CONTACT: dict

class Security(BaseModel):
    pk: str
    sk: str
    LOGIN_EMAIL: str
    LOGIN_PW: str
    TWO_FA_ENABLED: bool
    
class Social(BaseModel):
    pk: str
    sk: str
    SOCIAL: dict


class Clubs(BaseModel):
    pk: str
    sk: str
    CLUBS: dict


class CreditCards(BaseModel):
    pk: str
    sk: str
    CREDIT_CARD: dict

class Billing(BaseModel):
    pk: str
    sk: str
    SUBSCRIPTION: dict

class Login(BaseModel):
    email: str
    password: str

class ForgotPasswordRequest(BaseModel):
    email: str

class VerifyOtpRequest(BaseModel):
    login_email: str
    input_code: int

class UpdatePasswordRequest(BaseModel):
    profile_id: str
    new_password: str

class RefreshToken(BaseModel):
    refresh_token: str


###########################  build ##################################


class BuildersDapPayload(BaseModel):
    builder_id: str
    name: str  # who give dap
    daps: int


class BuilderDapListResponse(BaseModel):
    status: str
    status_code: int
    message: str
    data: list[BuildersDapPayload] = []  # list of BuildersDap


class BuilderDapCreateResponse(BaseModel):
    status: str
    status_code: int
    message: str
    created_at: str
    profile_type: str


class TokenPayload(BaseModel):
    body: str
    profile_type: Optional[str] = None
