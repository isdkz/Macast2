import _winapi
import json
from multiprocessing.connection import PipeConnection
url = 'http://aqqmusic.tc.qq.com/M500003nXAwD2Gh0w9.mp3?guid=fffffffffbf4773d\
000001951a7bc7ef&vkey=668423EC081AD449B5F9C1629343A86087A37DEDF0C0103FE2ABB86\
53D311246BBCB7005918FD4743083667D03921EE77A4153290F91575A__v2b9aaf3c&uin=1713\
925910&redirect=1&fromtag=111042'
data = {"command": ['loadfile', url, 'replace', -1, 'start=30,fullscreen=yes']}
msg = json.dumps(data) + '\n'
handler = _winapi.CreateFile(
                        r"\\.\pipe\macast_mpvsocket4978",
                        _winapi.GENERIC_READ | _winapi.GENERIC_WRITE, 0,
                        _winapi.NULL, _winapi.OPEN_EXISTING,
                        _winapi.FILE_FLAG_OVERLAPPED, _winapi.NULL)
ipc_sock = PipeConnection(handler)
ipc_sock.send_bytes(msg.encode())
ipc_sock.recv_bytes()
