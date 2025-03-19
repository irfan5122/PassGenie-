# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/ASUS/Desktop/py-exe/password_generated_epic_gui/Password_generator.py'],
             pathex=['C:\\Users\\ASUS\\Desktop\\py-exe\\password_generated_epic_gui'],
             binaries=[('C:/Users/ASUS/Desktop/py-exe/password_generated_epic_gui/Password_generator_app_icon.ico', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Password_generator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , uac_admin=True, icon='C:\\Users\\ASUS\\Desktop\\py-exe\\password_generated_epic_gui\\Password_generator_app_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Password_generator')
