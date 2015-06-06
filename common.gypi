# ����ƽ̨������
#
{
    'conditions' : [
        [ 'OS == "win"',
            {
                'msvs_disabled_warnings': [
                    4204,        # ���棺���˷Ǳ�׼��չ : �ǳ����ۺϳ�ʼֵ�趨��
                    4100,        # ���棺δ���õ��β�
                    4152,        # ���棺���ʽ�еĺ���/����ָ��ת��
                    4200,        # ���棺ʹ���˷Ǳ�׼��չ : �ṹ/�����е����С����
                    4505,        # ���棺δ���õı��غ������Ƴ�(�ֲ����������ˣ���δʹ��)
                    4800,        # ���棺��ֵǿ��Ϊ����ֵ��true����false��(���ܾ���)
                    4201,        # ���棺ʹ���˷Ǳ�׼��չ : �����ƵĽṹ/����
                    4189,   # local veriable is initialized but not referenced
                    4127,        # conditional expression is constant
                    4512,   # assignment operator could not be generated
                    4099,        # type name first seen using 'class' now seen using 'struct'
                    4251,   # 
                ], 
                'msbuild_configuration_attributes': {
                        'CharacterSet': '2',                                                # 1: unicode�ַ��� 2: multi bytes
                        'OutputDirectory': '$(SolutionDir)\\$(Configuration)',                      # $(OutDir)
                          'IntermediateDirectory': '$(OutDir)\\obj\\$(ProjectName)', # $(IntDir)
                },
                #'cflags':['/WX-',], #��ֹ warning treated as error - no 'object' file generated
                'msbuild_settings': {
                        'ClCompile': {
                            'TreatWChar_tAsBuiltInType': 'true',                              #��WChar_t��Ϊ��������
                            'TreatWarningAsError': 'false',                                  #��������Ϊ����
                            'WarningLevel': 'Level4',                                        #����ȼ�
                            'ProgramDataBaseFileName': '$(IntDir)vc$(PlatformToolsetVersion).pdb',                            
                            'PreprocessorDefinitions': ['WIN32','_USING_V110_SDK71_','_WINDOWS'],     #Ԥ����������
                            #'ExceptionHandling': '/EHsc',
                        },
                        'Link': {
                            'MinimumRequiredVersion':'5.01',                                #����֧��XP
                            'SubSystem': 'Console',                                            #����̨
                            #'LinkIncremental': 'true',
                            'ProgramDatabaseFile': '$(OutDir)pdb\\$(TargetName).pdb', #���ɳ������ݿ��ļ�
                            #'GenerateManifest': 'false',
                            'GenerateDebugInformation': 'false',                              #���ɵ�����Ϣ
                            'ImportLibrary' : '$(OutDir)bin\\$(TargetName).lib',         #�������λ��
                            'OutputFile': '$(OutDir)bin\\$(TargetName)$(TargetExt)',    #����ļ�
                            'ImageHasSafeExceptionHandlers': 'false',                        #ӳ����а�ȫ�쳣�������
                            'AdditionalDependencies': [                                            #����������
                                'kernel32.lib',
                                'gdi32.lib',
                                'winspool.lib',
                                'comdlg32.lib',
                                'advapi32.lib',
                                'shell32.lib',
                                'ole32.lib',
                                'oleaut32.lib',
                                'user32.lib',
                                'uuid.lib',
                                'odbc32.lib',
                                'odbccp32.lib',
                                'DelayImp.lib',
                                'winmm.lib',
                                'ws2_32.lib',
                            ],
                        },
                },
                'configurations': {
                    'Debug': {
                        'msbuild_settings': {
                            'ClCompile': {
                                'BasicRuntimeChecks': 'EnableFastChecks',                    #��������ʱ��飨/RTC1��
                                'DebugInformationFormat': 'EditAndContinue',                 # editAndContiue (/ZI)
                                'Optimization': 'Disabled',                                   # optimizeDisabled (/Od)
                                'PreprocessorDefinitions': ['_DEBUG'],                        #Ԥ����������
                                'RuntimeLibrary': 'MultiThreadedDebugDLL',                     # rtMultiThreadedDebug (/MTd)
                                #'RuntimeTypeInfo': 'false',                                  # /GR-
                                'IntrinsicFunctions': 'false'                                #�����ڲ���������
                            },
                            'Link': {
                                'GenerateDebugInformation': 'true',                         #���ɵ�����Ϣ
                            },
                        },
                        'msbuild_configuration_attributes': {
                            'LinkIncremental': 'true',
                            'GenerateManifest': 'false',
                        },
                    },
                    'Release': {
                        'msbuild_settings': {
                            'ClCompile': {
                                'DebugInformationFormat': 'ProgramDatabase',                  # programDatabase (/Zi)
                                'Optimization': 'MaxSpeed',                                    # optimizeDisabled (/O2)
                                'WholeProgramOptimization': 'true',                         #/GL
                                 'PreprocessorDefinitions': ['NDEBUG'],
                                'RuntimeLibrary': 'MultiThreadedDLL',                          # rtMultiThreaded (/MT)
                                #'RuntimeTypeInfo': 'false',                                 # /GR-
                                'IntrinsicFunctions': 'true'                                #�����ڲ��������ǣ�
                            },
                            'Link': {
                                #'LinkIncremental': 'false',
                                #'GenerateManifest': 'true',
                                'GenerateDebugInformation': 'true',                            #���ɵ�����Ϣ
                            },
                        },
                        'msbuild_configuration_attributes': {
                            'LinkIncremental': 'false',                                        #��������������
                            'GenerateManifest': 'false',                                    #������manifest
                        },
                    },
                },
            },
        ],
        ['OS == "android"',{
            'cflags': [
              '-Werror',
            ],
          },
        ],
        ['OS == "ios"',{
            'default_configuration':"Release",
            'xcode_settings': {
                        'SDKROOT': 'iphoneos',
                        'TARGETED_DEVICE_FAMILY': '1,2',
                        'CODE_SIGN_IDENTITY': 'iPhone Developer',
                        'IPHONEOS_DEPLOYMENT_TARGET': '6.0',
                        'ARCHS': '$(ARCHS_STANDARD)',
                        'CLANG_CXX_LANGUAGE_STANDARD':'c++0x',
                },
            'configurations':{

                'Debug':{
                    'defines':[ 'DEBUG'],
                    'xcode_settiings':{
                        "GCC_OPTIMIZATION_LEVEL":"0",
                        "GCC_GENERATE_DEBUGGING_SYMBOLS":"YES",
                    }
                },
                'Release':{
                    'defines':[ 'NDEBUG'],
                    'xcode_settiings':{
                        "GCC_OPTIMIZATION_LEVEL":"3",
                        "GCC_GENERATE_DEBUGGING_SYMBOLS":"NO",
                        "DEAD_CODE_STRIPPING":"YES",
                        "GCC_INLINES_ARE_PRIVATE_EXTERN":"YES",
                    },
                },
            },
          },
        ],
    ]    
}
