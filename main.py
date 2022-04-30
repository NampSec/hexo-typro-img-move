# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import re
mdlist = []
def listallmd():
    # 在下面的代码行中使用断点来调试脚本。
    filelist = os.listdir(os.getcwd()+ "\\source\\_posts")
    for file in filelist:
        if file.endswith(".md"):
                mdlist.append(file)

# 按间距中的绿色按钮以运行脚本。

def getallpic(mdpath):
     try:
        to_write = []
        with open(mdpath,'r+',encoding='utf-8') as f_obj:
            content = f_obj.readlines()

            exp = re.compile(r"!\[(image.*?)\]\((.*?)\)")
            for i in content:
                pic = []
                pic  = exp.findall(i)
                #未来增加重复判定等
                if len(pic) != 0:
                    temp = mdpath[:-3]
                    os.system("copy" + " " + pic[0][1] + " " + os.getcwd()+"\\source\\_posts\\img")
                    i = i.replace(pic[0][1],"img\\"+ pic[0][1][pic[0][1].rfind("\\") + 1:])
                to_write.append(i)
            f_obj.close()
        os.rename(mdpath,mdpath+".bak")
     except:
         print("文件打开失败，可能是有其他程序占用")
     try:
        with open(mdpath,"w",encoding="utf-8") as ffobj:
            ffobj.writelines(to_write)
            ffobj.close()

     except:
         print("写入新文件失败")


if __name__ == '__main__':
    listallmd()
    if not os.path.exists(os.getcwd()+"\\source\\_posts\\img"):
        os.mkdir(os.getcwd()+"\\source\\_posts\\img")
    print(mdlist)
    for i in mdlist:
        getallpic(os.getcwd()+"\\source\\_posts\\" + i)



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
