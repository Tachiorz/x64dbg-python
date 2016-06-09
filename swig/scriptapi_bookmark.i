%{
#include "_scriptapi_bookmark.h"
%}

%typemap(in) duint {
  $1 = (int) PyLong_AsLong($input);
}

%rename (Bookmark_Set) Script::Bookmark::Set;
%rename (Bookmark_Get) Script::Bookmark::Get;
%rename (Bookmark_GetInfo) Script::Bookmark::GetInfo;
%rename (Bookmark_Delete) Script::Bookmark::Delete;
%rename (Bookmark_DeleteRange) Script::Bookmark::DeleteRange;
%rename (Bookmark_Clear) Script::Bookmark::Clear;
%rename (Bookmark_GetList) Script::Bookmark::GetList;

%include _scriptapi_bookmark.h

%ListInfo_class(Script::Bookmark::BookmarkInfo,BookmarkInfoList)
