from typing import Iterable
from VPNConnection import VPNConnection


class VPNHandler:
    """
    A base class that defines the interfaces for dealing with a VPN handler
    """

    def get_connections(self, open_only: bool) -> Iterable[VPNConnection]:
        """
        Gets all connections known to the vpn handler, open or closed
        """
        raise NotImplimentedError

    def get_connection_names(self, open_onlt: bool) -> Iterable[str]:
        """
        gets the names of the vpn connections
        """
