# VEX  


---  

# パラメータの読み込み  

```c
int a = chi(path);
float b = chf(path);
```

---  

### 空の Polyline を作る  

addprim の引数 "polyline"  
型指定？めっちゃ大事  

```c
// 空の Polyline
int prim = addprim(0, "polyline");

// ここで空の Polyline に頂点を入れる
int vt = addvertex(0, prim, pt);  


```