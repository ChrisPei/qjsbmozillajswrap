���� mozjswrap �⣺

------------------------------------------------------------------------
Android (ʹ�� NDK r9c)
------------------------------------------------------------------------

1. �� moz.gyp, ���� js_debug Ϊ false. (line 9)

2. �������ļ���Ϊ jni���������󲼾��������ģ�
jni/
    mozjswrap.cpp
    mozjswrap.h
    Android.mk

3. �����н��뵽 jni ��ִ�����
    sh gen-android.sh

4. �����../libs/armeabi-v7a/libmozjswrap.so



------------------------------------------------------------------------
Windows, Mac, iOS (ʹ�� gyp, python, VisualStudio, XCode)
------------------------------------------------------------------------

1. ��װ python 2.7.x. (Windows�����Ⱥ�ļ�����)

2. �� moz.gyp, ����� iOS������ js_debug ����Ϊ false��Windows �� Mac ����Ϊ true (line 9)

3. ����
Windows: ִ�� gen-msvs2012.bat      ���: ./build/Release/bin/mozjswrap.dll
iOS:     bash gen-ios.sh            ���: ./build/Release-iphoneos/libmozjswrap.a
Mac:     bash gen-mac.sh            ���: ./build/Default/mozjswrap.bundle
