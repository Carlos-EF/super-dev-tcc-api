from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.infrastructure.connection import get_session
from tcc.api.schemas.clients_schemas import CreateClientRequest, EditClientRequest, PaginatedClientResponse, ClientResponse


router = APIRouter(
    prefix='/clients',
    tags=['Clients'],
)