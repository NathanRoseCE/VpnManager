from VPNManager.VPNConnection import VPNConnection, VPNState
import subprocess
import time
import datetime
import os
import signal
import pexpect

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

    def open(self, password: str=None, interactive:bool=True) -> None:
        command = ' '.join(self._generate_ovpn_open_command())
        print(f"running command: {command}")
        child = pexpect.spawn(command)
        start = datetime.datetime.now()
        while True:
            i = child.expect(["Connected", "", "Private key passphrase:"])
            if i == 0:
                print(f"{self._name} connected")
                child.kill()
                break
            elif i == 1:
                child.kill(0)
                raise ValueError("An error occured")
            elif i == 2:
                if not interactive:
                    raise ValueError("Password is required")
                else:
                    if password is None:
                        # todo ask for string
                        pass
                    child.sendline(f'{password}\n')
        self._status = VPNState.OPEN
        
    def _generate_ovpn_open_command(self) -> None:
        """
        generates the ovpn open command
        """
        return [
            "openvpn3",
            "session-start",
            "-c",
            self._config_file_path
        ]
    
    def _generate_ovpn_closed_command(self) -> None:
        """
        generates the ovpn closed command
        """
        return [
            "openvpn3",
            "session-manage",
            "--disconnect",
            "-c",
            self._config_file_path
        ]
    
    def close(self) -> None:
        try:
            output = subprocess.check_output(self._generate_ovpn_closed_command())
        except subprocess.CalledProcessError:
            raise ValueError("Session was not started")
        finally:
            self._status = VPNState.CLOSED
            
        
        
        
