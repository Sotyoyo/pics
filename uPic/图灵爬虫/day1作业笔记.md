## 解mcode过程

1. 确定url为`http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007` method为`POST`
2. 粘贴headers 

![1]('/1.jpg')

![2]('2.png')

3. 不论是用启动器还是XHR断点找到请求发送的位置都是在3956行
4. 搜索mcode关键字，发现搜不到
5. 只能搜索所有js文件，发现`mcode=indexcode.getResCode()`
6. 但是这个是另外一个1067的接口请求，根本没有调用
7. 无奈只好搜索所有js文件中带有`p_sysapi1007`的相关代码，终于找到位置
8. 找到getResCode方法两处定义
```
w.getResCode = function() {
    var e = Math.floor((new Date).getTime() / 1e3);
    return window.JSonToCSV.missjson("" + e)
}
```

```
var indexcode={
		getResCode:function(){
			var time=Math.floor(new Date().getTime()/1000); 
            return window.JSonToCSV.missjson(""+time);
		}
}
```
9. 把JsonToCSV这个方法拷贝下来，删除不要的，并且略作调整。
10. 第一次测试，提示缺少必要参数
11. 尝试改变mcode重新发送请求，发现报错无授权访问，证明mcode没错
12. 发现是自己忘记传data了。。。
