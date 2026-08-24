from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from tcc.core.auth_security import extract_supabase_error_message, extract_supabase_session, extract_supabase_user, normalize_email, supabase_user_id, verify_supabase_token
from tcc.infrastructure.connection import supabase
from tcc.infrastructure.models.users_model import UserModel