::Version: 1.0, Author: Mateusz Redzynia
@echo off
powershell NetSh Advfirewall set allprofiles state off
timeout 1
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
timeout 1 
ECHO Done.
timeout 1