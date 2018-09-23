# Rendering  


レンダリングちょっと苦労したので、とりあえずメモ  

- レンダリングの流れ  
- フォルダ構成  
- Ref.  



---  

### レンダリングの流れ  

Geometry  
↓ (Houdini)  
.exr // 00001 - 01234  
↓ (Houdini MPLAY) // convert etr to jpg  
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


### Ref.  

Mantraによるレンダリングの方法（sidefx）  
[http://www.sidefx.com/ja/docs/houdini/render/render.html](http://www.sidefx.com/ja/docs/houdini/render/render.html)  


カメラのセットアップ（sidefx）  
[http://www.sidefx.com/ja/docs/houdini/render/cameras.html](http://www.sidefx.com/ja/docs/houdini/render/cameras.html)  


Houdini初級編：レンダリング（Born Digital サポート）  
[https://support.borndigital.co.jp/hc/ja/articles/360007012673-Houdini%E5%88%9D%E7%B4%9A%E7%B7%A8-%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0](https://support.borndigital.co.jp/hc/ja/articles/360007012673-Houdini%E5%88%9D%E7%B4%9A%E7%B7%A8-%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0)  


Camera object node（sidefx）  
[http://www.sidefx.com/ja/docs/houdini/nodes/obj/cam.html](http://www.sidefx.com/ja/docs/houdini/nodes/obj/cam.html)  


【Houdini16.5基礎編】12.レンダリング（indyzone）  
[http://houdini.indyzone.jp/blog/%E3%80%90houdini16-5%E5%9F%BA%E7%A4%8E%E7%B7%A8%E3%80%9112-%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0/](http://houdini.indyzone.jp/blog/%E3%80%90houdini16-5%E5%9F%BA%E7%A4%8E%E7%B7%A8%E3%80%9112-%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0/)  







