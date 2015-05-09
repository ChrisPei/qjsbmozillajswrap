#ifndef __heap_obj_storage_h__
#define __heap_obj_storage_h__

#include "mozjswrap.h"

//
// storeJSObject �� jsObj �� nativeObj ��ʾ�������洢���������� ID
//
OBJID storeJSObject(JS::HandleObject jsObj, JS::HandleObject nativeObj);

//
// ���� nativeObj ���� ID
// 
OBJID jsObj2ID(JS::HandleObject nativeObj);
JSObject* ID2JSObj(OBJID id);
void deleteJSObject(JSObject* jsObj);

#endif // #ifndef __heap_obj_storage_h__