%{
#include "_scriptapi_comment.h"
%}

%rename (Comment_Set) Script::Comment::Set;
%rename (Comment_Get) Script::Comment::Get;
%rename (Comment_GetInfo) Script::Comment::GetInfo;
%rename (Comment_Delete) Script::Comment::Delete;
%rename (Comment_DeleteRange) Script::Comment::DeleteRange;
%rename (Comment_Clear) Script::Comment::Clear;
%rename (Comment_GetList) Script::Comment::GetList;

%include _scriptapi_comment.h

%ListInfo_class(Script::Comment::CommentInfo,CommentInfoList)
