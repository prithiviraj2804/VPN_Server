from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship


class WireGuardPeer(Base):
    
    __tablename__ = "wireguard_peers"
    user_id = Column(String, ForeignKey("users.id"))
    peer_name = Column(String, index=True)
    public_key = Column(String, unique=True, index=True)
    private_key = Column(String, unique=True, index=True)
    assigned_ip = Column(String, unique=True, index=True)
