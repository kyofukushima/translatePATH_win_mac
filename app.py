# ライブラリ読み込み
import streamlit as st
from pathlib import PurePosixPath, Path
# st.write('macのパスをwindowsに変換する')

st.write('入力してcommand(ctrl)+Enterで入力を確定')

win_path = st.text_area('windowsのパスをmacに変換する')
# win_path = Path(PurePosixPath(mac_path)).as_posix()
mac_path = win_path.replace('192.168.1.201','Volumes')
mac_path = mac_path.replace('\\','/')[1:]
st.write(mac_path)



mac_path = st.text_area('macのパスをwindowsに変換する')
# win_path = Path(PurePosixPath(mac_path)).as_posix()
win_path = mac_path.replace('Volumes','192.168.1.201')
win_path = "\\\\" + win_path.replace('/','\\')
st.write(win_path)

