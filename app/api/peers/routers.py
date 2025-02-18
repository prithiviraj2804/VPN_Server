

from typing import List
from fastapi import APIRouter, Depends

from app.api.peers.schemas import AddPeerRequest, DeletePeer, EditPeer, TransferData
from .services import peer_service
from app.core.database import get_session
from app.utils.httpbearer import get_current_user

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("")
async def get_peers(db: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)):
    result = await peer_service(db).get_all_peers(current_user)
    return result

@router.get("/users/{user_id}")
async def get_peers(user_id: str, db: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)):
    result = await peer_service(db).get_all_peers_by_id(user_id)
    return result


@router.get("/{peer_id}")
async def get_single_peer(peer_id: str, db: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)):
    result = await peer_service(db).get_peer(peer_id)
    return result


@router.post("/{user_id}")
async def add_peers(user_id: str, data: AddPeerRequest, current_user=Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    result = await peer_service(db).add_peer(user_id, data, current_user)
    return result


@router.delete("/{peer_id}")
async def add_peers(peer_id: str, current_user=Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    result = await peer_service(db).remove_peer(peer_id, current_user)
    return result


@router.put("/{peer_id}")
async def edit_peers(peer_id: str, data: EditPeer, current_user=Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    result = await peer_service(db).update_peer(peer_id, data, current_user)
    return result


@router.post("/generate-peer-config/{peer_id}")
async def generate_peer_config(peer_id: str,  db: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)):
    result = await peer_service(db).generate_peer_config(peer_id, current_user)
    return result

@router.get("/transfer-data/{peer_id}")
async def get_transfer_data(peer_id: str, db: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)):
    result = await peer_service(db).get_peer_transfer_data(peer_id)
    return result