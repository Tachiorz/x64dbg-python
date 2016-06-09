from .. import _x64dbg


class SymbolType:
    Function = _x64dbg.Function
    Import = _x64dbg.Import
    Export = _x64dbg.Export


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Symbol_GetList(list_info)
    if result:
        return _x64dbg.SymbolInfoList(list_info)
    return None
