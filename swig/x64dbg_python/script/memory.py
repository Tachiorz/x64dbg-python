from .. import _x64dbg

Write = _x64dbg.Memory_Write
IsValidPtr = _x64dbg.IsValidPtr
RemoteAlloc = _x64dbg.RemoteAlloc
RemoteFree = _x64dbg.RemoteFree
ReadByte = _x64dbg.ReadByte
WriteByte = _x64dbg.WriteByte
ReadWord = _x64dbg.ReadWord
WriteWord = _x64dbg.WriteWord
ReadDword = _x64dbg.ReadDword
WriteDword = _x64dbg.WriteDword
ReadQword = _x64dbg.ReadQword
WriteQword = _x64dbg.WriteQword
ReadPtr = _x64dbg.ReadPtr
WritePtr = _x64dbg.WritePtr

def Read(addr, data):
    #(duint addr, void* data, duint size, duint* sizeRead)
    return _x64dbg.Read(addr, data)
