from enum import Enum


class VPNState(Enum):
    """
    A simple enum to hold whether the enum is open or closed
    """
    CLOSED = 0
    OPEN = 1


class VPNConnection:
    """
    A class that is useful for managing a VPN connection
    """

    def status() -> VPNState:
        """
        gets the state of the VPN
        """
        raise NotImplimentedError

    def open() -> None:
        """
        Opens the vpn conneciton
        """
        raise NotImplimentedError

    def close() -> None:
        """
        Closes the vpn connection
        """
        raise NotImplimentedError

    def name() -> str:
        """
        gets the human readable name for a vpn connection
        """
        raise NotImplimentedError
