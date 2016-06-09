from .. import _x64dbg

Set = _x64dbg.Bookmark_Set
Get = _x64dbg.Bookmark_Get
GetInfo = _x64dbg.Bookmark_GetInfo
Delete = _x64dbg.Bookmark_Delete
DeleteRange = _x64dbg.Bookmark_DeleteRange
Clear = _x64dbg.Bookmark_Clear


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Bookmark_GetList(list_info)
    if result:
        return _x64dbg.BookmarkInfoList(list_info)
    return None
