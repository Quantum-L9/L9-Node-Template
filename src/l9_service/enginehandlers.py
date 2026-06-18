# <!-- L9_META
# role: sdk_bridge
# version: 1.0.0
# tags: [l9, sdk, transport, handlers]
# /L9_META -->
"""
enginehandlers.py — SOLE SDK BRIDGE for {{node_slug}}.

INVARIANTS (never violate):
  - This is the ONLY file that imports from the L9 SDK transport layer.
  - Every action listed in ENGINESPEC.yaml MUST have exactly one handler here.
  - All handlers MUST accept TransportPacket and return TransportPacket.
  - No direct node-to-node HTTP. Gate is the sole router.
  - No PacketEnvelope imports anywhere in this repo.

Handler skeleton generated from nodespec.yaml § action_contract.
Replace pass bodies with domain logic from src/l9_service/domain/.
"""
from __future__ import annotations

# from l9_sdk.transport import TransportPacket  # Uncomment when SDK is installed
# from l9_sdk.registry import register_handler   # Uncomment when SDK is installed

# ---------------------------------------------------------------------------
# Payload models — define in src/l9_service/models.py or inline below.
# ---------------------------------------------------------------------------
# class {{Action1Request}}(BaseModel): ...
# class {{Action1Response}}(BaseModel): ...


# ---------------------------------------------------------------------------
# Handlers — one per action in ENGINESPEC.yaml
# ---------------------------------------------------------------------------

# @register_handler("{{action_1}}")
# async def handle_{{action_1}}(packet: TransportPacket) -> TransportPacket:
#     """Handle {{action_1}} — {{action_1_description}}"""
#     # TODO: implement domain logic
#     raise NotImplementedError("handle_{{action_1}} not implemented")
