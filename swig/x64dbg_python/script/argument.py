from .. import _x64dbg

Add = _x64dbg.Argument_Add
GetInfo = _x64dbg.Argument_GetInfo
Overlaps = _x64dbg.Argument_Overlaps
Delete = _x64dbg.Argument_Delete
DeleteRange = _x64dbg.Argument_DeleteRange
Clear = _x64dbg.Argument_Clear


class ArgumentGet:
    def __init__(self, t):
        self.start = t[0]
        self.end = t[1]
        self.instructionCount = t[2]


def Get(addr):
    res = _x64dbg.Argument_Get(addr, None, None, None)
    if res:
        return ArgumentGet(res[1:])
    else:
        return None


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Argument_GetList(list_info)
    if result:
        return _x64dbg.ArgumentInfoList(list_info)
    return None
