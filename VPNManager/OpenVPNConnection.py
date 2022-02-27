from VPNManager.VPNConnection import VPNConnection, VPNState
import subprocess

class OpenVPNConnection:
    """
    A handler for an openvpn connection
    """
    def __init__(self, name: str, config_file_path: str) -> None:
        self._name = name
        self._config_file_path = config_file_path
        self._status = self._check_state() 
        

    def _check_state(self) -> VPNState:
        """
        checks the state of the vpn connection
        """
        vpn_connections = subprocess.check_output(['openvpn3', 'sessions-list'])
        return self._is_this_state_present(vpn_connections.decode('utf-8'))
                

    def _is_this_state_present(self, ovpn_sessions_str: str) -> VPNState:
        """
        Checks whether the state is present given a vpn string
        """
        is_active = False
        for line in ovpn_sessions_str.split('\n'):
            if 'Config name:' in line:
                if self._config_file_path in line:
                    is_active = True
        return VPNState.OPEN if is_active else VPNState.CLOSED

