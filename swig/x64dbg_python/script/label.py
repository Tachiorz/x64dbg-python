from .. import _x64dbg

Set = _x64dbg.Label_Set
FromString = _x64dbg.FromString
Get = _x64dbg.Label_Get
GetInfo = _x64dbg.Label_GetInfo
Delete = _x64dbg.Label_Delete
DeleteRange = _x64dbg.Label_DeleteRange
Clear = _x64dbg.Label_Clear


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Label_GetList(list_info)
    if result:
        return _x64dbg.LabelInfoList(list_info)
    return None
