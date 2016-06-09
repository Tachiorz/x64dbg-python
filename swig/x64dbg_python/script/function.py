from .. import _x64dbg

Add = _x64dbg.Function_Add
GetInfo = _x64dbg.Function_GetInfo
Overlaps = _x64dbg.Function_Overlaps
Delete = _x64dbg.Function_Delete
DeleteRange = _x64dbg.Function_DeleteRange
Clear = _x64dbg.Function_Clear


class FunctionGet:
    def __init__(self, t):
        self.start = t[0]
        self.end = t[1]
        self.instructionCount = t[2]


def Get(addr):
    res = _x64dbg.Function_Get(addr, None, None, None)
    if res:
        return FunctionGet(res[1:])
    else:
        return None


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Function_GetList(list_info)
    if result:
        return _x64dbg.FunctionInfoList(list_info)
    return None
