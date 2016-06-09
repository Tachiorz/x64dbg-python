from .. import _x64dbg

InfoFromAddr = _x64dbg.InfoFromAddr
InfoFromName = _x64dbg.InfoFromName
BaseFromAddr = _x64dbg.BaseFromAddr
BaseFromName = _x64dbg.BaseFromName
SizeFromAddr = _x64dbg.SizeFromAddr
SizeFromName = _x64dbg.SizeFromName
NameFromAddr = _x64dbg.NameFromAddr
PathFromAddr = _x64dbg.PathFromAddr
PathFromName = _x64dbg.PathFromName
EntryFromAddr = _x64dbg.EntryFromAddr
EntryFromName = _x64dbg.EntryFromName
SectionCountFromAddr = _x64dbg.SectionCountFromAddr
SectionCountFromName = _x64dbg.SectionCountFromName
SectionFromAddr = _x64dbg.SectionFromAddr
SectionFromName = _x64dbg.SectionFromName
GetMainModuleInfo = _x64dbg.GetMainModuleInfo
GetMainModuleBase = _x64dbg.GetMainModuleBase
GetMainModuleSize = _x64dbg.GetMainModuleSize
GetMainModuleEntry = _x64dbg.GetMainModuleEntry
GetMainModuleSectionCount = _x64dbg.GetMainModuleSectionCount
GetMainModuleName = _x64dbg.GetMainModuleName
GetMainModulePath = _x64dbg.GetMainModulePath


def SectionListFromAddr(addr):
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.SectionListFromAddr(addr, list_info)
    if result:
        return _x64dbg.ModuleSectionInfoList(list_info)
    return None


def SectionListFromName(name):
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.SectionListFromName(name, list_info)
    if result:
        return _x64dbg.ModuleSectionInfoList(list_info)
    return None


def GetMainModuleSectionList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.GetMainModuleSectionList(list_info)
    if result:
        return _x64dbg.ModuleSectionInfoList(list_info)
    return None


def GetList():
    list_info = _x64dbg.ListInfo()
    result = _x64dbg.Module_GetList(list_info)
    if result:
        return _x64dbg.ModuleInfoList(list_info)
    return None
