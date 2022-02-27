import pytest
from VPNManager.OpenVPNConnection import OpenVPNConnection
from VPNManager.VPNConnection import VPNState


@pytest.fixture
def test_vpn_connection():
    yield OpenVPNConnection("test_connection", "/home/nathanrose/ovpn/desk.ovpn")

    
def test_is_this_state_present_no_sessions(test_vpn_connection):
    assert (
        test_vpn_connection._is_this_state_present("No sessions Available") ==
        VPNState.CLOSED
    )
    
def test_is_this_state_present_session_not_present(test_vpn_connection):
    assert (
        test_vpn_connection._is_this_state_present(
            """-----------------------------------------------------------------------------
        Path: /net/openvpn/v3/sessions/96489416sd438s4c22s96fds298a606250ed
     Created: Sun Feb 27 16:44:39 2022                  PID: 63139
       Owner: nathanrose                             Device: tun0
 Config name: /home/nathanrose/ovpn/katalyst/config.conf  (Config not available)
Session name: 99.170.114.34
      Status: Connection, Client connected
-----------------------------------------------------------------------------"""
        ) ==
        VPNState.CLOSED
    )
    
def test_is_this_state_present_session_present(test_vpn_connection):
    assert (
        test_vpn_connection._is_this_state_present(
            """-----------------------------------------------------------------------------
        Path: /net/openvpn/v3/sessions/96489416sd438s4c22s96fds298a606250ed
     Created: Sun Feb 27 16:44:39 2022                  PID: 63139
       Owner: nathanrose                             Device: tun0
 Config name: /home/nathanrose/ovpn/desk.ovpn  (Config not available)
Session name: 99.170.114.34
      Status: Connection, Client connected
-----------------------------------------------------------------------------"""
        ) ==
        VPNState.OPEN
    )
