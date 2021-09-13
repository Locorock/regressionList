import sys
import os
import winreg as reg

cwd = os.getcwd()
python_exe = sys.executable

key_path = r"SystemFileAssociations\\.csv\\shell\\YGOtoEDO"
key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, 'Import to EDOPro')

key2 = reg.CreateKeyEx(key, r'command')
reg.SetValue(key2, '', reg.REG_SZ, python_exe+f' "{cwd}\\collectionToBanlist.py" "%1"')