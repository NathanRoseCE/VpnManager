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

    def status(self) -> VPNState:
        """
        gets the state of the VPN
        """
        raise NotImplimentedError

    def open(self, password: str=None, interactive:bool=True) -> None:
        """
        Opens the vpn conneciton 
        if interactive is set and password is not set will prompt for password if needed
        if interactive is not set, password is None, and a password is required will throw 
        an exception
        """
        raise NotImplimentedError

    def close(self) -> None:
        """
        Closes the vpn connection
        """
        raise NotImplimentedError

    def name(self) -> str:
        """
        gets the human readable name for a vpn connection
        """
        raise NotImplimentedError
