from .. import _x64dbg

Set = _x64dbg.Comment_Set
Get = _x64dbg.Comment_Get
GetInfo = _x64dbg.Comment_GetInfo
Delete = _x64dbg.Comment_Delete
DeleteRange = _x64dbg.Comment_DeleteRange
Clear = _x64dbg.Comment_Clear


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Comment_GetList(list_info)
    if result:
        return _x64dbg.CommentInfoList(list_info)
    return None
