# Rendering  


レンダリングちょっと苦労したので、とりあえずメモ  

---  

### レンダリングの流れ  

Geometry  
↓ (Houdini)  
.exr // 00001 - 01234  
↓ (Houdini MPlayer) // convert etr to jpg  
.jpg // 1 - 1234  
↓ (Python, PIL) // crop image
.jpg // 00001 - 01234  
↓ (ffmpeg)  
MP4  


---  

### フォルダ構成  

毎度毎度ちまちま設定を整えるのが面倒なのでこんな感じで、  

- Projectname  
  - Projectname.hipnc  
  - render // 書き出される etr  
  - JPG // etr から jpg に変換  
  - cropped // jpg から必要な部分をクロップ  
  - ImgCrop.py // クロップするスクリプト  


---  


### Ref  


