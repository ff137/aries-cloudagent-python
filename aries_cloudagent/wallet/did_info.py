"""KeyInfo, DIDInfo."""

from typing import NamedTuple

from .did_method import DIDMethod
from .key_type import KeyType

INVITATION_REUSE_KEY = "invitation_reuse"

KeyInfo = NamedTuple(
    "KeyInfo", [("verkey", str), ("metadata", dict), ("key_type", KeyType)]
)
DIDInfo = NamedTuple(
    "DIDInfo",
    [
        ("did", str),
        ("verkey", str),
        ("metadata", dict),
        ("method", DIDMethod),
        ("key_type", KeyType),
    ],
)
