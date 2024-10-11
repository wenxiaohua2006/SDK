class pd_file_type_error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


pass
import os
import time
try:
    import tkinter as tk
except ImportError:
    os.system("pip install tkinter")

'''消息弹窗提示'''
def show_message_box(title:str,add:str,type:str='info')->None:
    """传入参数：标题、内容、类型（默认info提示）"""
    from tkinter import messagebox
    root = tk.Tk()
    root.wm_attributes('-topmost',1)
    # 隐藏主窗口  
    root.withdraw()
    if type == 'error':
        messagebox.showerror(title, add)
    elif type == 'info':
        messagebox.showinfo(title, add)
    root.destroy()

'''排序算法'''
def listsort(arry,aser:str='top',js:str='xz'):
    newarry = arry
    if js == 'xz':
        for i in range(len(arry)):
            for i2 in range(len(arry)):
                if aser == 'top':
                    if arry[i] < arry[i2]:
                        arry[i],arry[i2] = arry[i2],arry[i]
                elif aser == 'bottom':
                    if arry[i] > arry[i2]:
                        arry[i],arry[i2] = arry[i2],arry[i]
    elif js == 'mp':
        for i2 in range(len(arry)):
            for i in range(1,len(arry)):
                if aser == 'top':
                    if arry[i] < arry[i-1]:
                        arry[i],arry[i-1] = arry[i-1],arry[i]
                elif aser == 'bottom':
                    if arry[i] > arry[i-1]:
                        arry[i],arry[i-1] = arry[i-1],arry[i]
    return newarry


'''转换字符为二进制'''
def char_to_binary(string)->list:
    """传入参数：字符串"""
    n = []
    for char in string:
    # 获取字符的ASCII码（或Unicode码，对于Python 3.x，str类型已经是Unicode）  
        ascii_value = ord(char)
        # 将ASCII码转换为二进制字符串，使用bin()函数，并去掉前缀'0b'  
        binary_str = bin(ascii_value)[2:]
        n.append(binary_str)
    return n


'''二进制转为字符'''
def binary_to_char(binary_list:list)->str:
    """传入参数：二进制列表例:[1010111,1100101,1101110,1100001]"""
    text = ''
    for i in binary_list:
        binary_str = str(i)
    # 去掉可能的'0b'前缀（尽管在直接转换二进制字符串时通常不会遇到）  
        binary_str = binary_str.lstrip('0b')  
        # 将二进制字符串转换为整数（即ASCII码或Unicode码点）  
        ascii_value = int(binary_str, 2)
        # 使用chr()函数将整数转换回字符  
        char = chr(ascii_value)
        text += char
    return text

'''png转换ico图片'''
def png_to_ico(width:int=64,height:int=64,img_path:str=None,box:bool=False)->None:
    """传入参数：宽、高、图片路径默认窗口打开,若填入按照填入路径打开图片、是否进行弹窗提示"""
    try:
        from PIL import Image
    except ImportError:
        os.system("pip install Pillow")
    from os.path import isfile, splitext
    from tkinter import filedialog
    # 创建一个新的Tkinter窗口，但不显示它
    root = tk.Tk()
    root.withdraw()
    if img_path==None:
        img_path = filedialog.askopenfilename(title="选择图片文件")# 打开一个文件选择对话框，用户选择图片文件
    if not isfile(img_path):# 检查所选文件是否存在
        print(f"文件不存在: {img_path}")
    else:
        img = Image.open(img_path)          # 打开图片文件
        icon_sizes = [(width, height)]      # 定义图标大小
        base_name = splitext(img_path)[0]   # 提取图像文件基本名称（不包括扩展名）
        icon_filename = f"{base_name}.ico"
        img.save(icon_filename, sizes=icon_sizes)
        if box == True:
            show_message_box('消息提示','转换成功',type='info')


'''mp4视频转gif'''
def mp4_to_gif(mp4_path:str,save_gif:str,width:int=400,height:int=400,fps:int=15)->None:
    """传入参数：mp4文件路径、保存gif文件路径、宽、高、帧率"""
    try:
        from moviepy.editor import VideoFileClip
    except ImportError:
        os.system("pip install moviepy")
    clip = VideoFileClip(mp4_path,target_resolution=(width,height))
    clip.write_gif(save_gif+'.gif',fps=fps)  #设置为每秒15帧


'''mp4视频封面获取'''
def filetopng(mp4_path:str,png_save_path:str)->None:
    """传入参数：mp4文件路径、保存png文件路径"""
    from moviepy.editor import VideoFileClip
    from PIL import Image
    video_path = mp4_path
    try:
    # 使用moviepy加载视频
        clip = VideoFileClip(video_path)
        # 获取第一帧（封面）
        frame = clip.get_frame(0)  # 获取第一秒的第一帧
        # 将NumPy数组转换为Pillow图像对象
        image = Image.fromarray(frame)
        # 保存图像
        image.save(f'{png_save_path}.jpg')
        # 关闭clip释放资源
        clip.close()
    except Exception as e:
        print(e)


'''倒计时'''
def countdown(where:int,arrive:int,title:any)->None:
    """传入参数：开始时间、结束时间、标题"""
    import time
    for quits in range(where,arrive):
        nums = arrive - quits
        print("\r",title,"{}".format(nums),end="")
        time.sleep(1)
    print('\n')


'''进度条'''
def timemi(stop_timme:int=1,title:str='进展进度',stop:any='已完成')->None:
    """传入参数：每秒刷新时间、标题"""
    import time
    ls = ''
    for i in range(1, 101):
        l = 50 - i // 2
        c = '-' * l
        if i == 100:
            ls = stop
        print("\r{}: {}%:{}{}>{}{}{} ".format(title,i,'[',"▓" * (i // 2),c,']',ls), end="")
        time.sleep(stop_timme)


'''获取所有窗口进程信息'''
def get_all_windows()->list:
    """获取所有窗口进程信息无参数值"""
    try:
        import win32gui
    except ImportError:
        os.system("pip install win32gui")
    try:
        import win32process
    except ImportError:
        os.system("pip install win32process")
    try:
        import psutil
    except ImportError:
        os.system("pip install psutil")
    windows_list = []  
    def win_enum_handler(hwnd, extra):  
        if win32gui.IsWindowVisible(hwnd):  
            window_text = win32gui.GetWindowText(hwnd)  
            if window_text:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)  
                try:
                    process = psutil.Process(pid)  
                    process_name = process.name()  # 使用strip()去除可能的空白字符  
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  
                    process_name = "Unknown"
                windows_list.append({'hwnd':hwnd, 'window_text':window_text, 'pid':pid, 'process_name':process_name})  
    win32gui.EnumWindows(win_enum_handler, None)
    return windows_list


'''html网页数据分享展示图'''
def pyecharts_html():
    """无参数值,需代码更改"""
    try:
        from pyecharts.charts import Bar
    except ImportError:
        os.system("pip install pyecharts")
    from pyecharts import options as opts
    # 内置主题类型可查看 pyecharts.globals.ThemeType
    from pyecharts.globals import ThemeType
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        #传入X轴商品数据
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        #传入Y轴商家销售数据
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
        #传入标题及副标题
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    )
    bar.render()



'''静态图表'''
import matplotlib.pyplot as plot
import matplotlib
class mat:
    '''# MAT plot
    - plotname:`bat,pie,plot`
    - xdata,ydata:`you int data and str title`
    - `psong import plot`
    - · 
    - · 
    - ·
    - ydata
    - ·
    - ·
    - ·
    - ·             
    - ·----------------xdata----------
    '''
    def __init__(self,plotname:str,xdata:list|tuple,ydata:list|tuple,Xtitle:str=None,Ytitle:str=None,title:str=None,path:str=None,font:str=None):
        if not font:
            matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        else:
            matplotlib.rcParams['font.sans-serif'] = [font]
        self.X = Xtitle
        self.Y = Ytitle
        self.title = title
        self.plotname = plotname
        self.xdata = xdata
        self.ydata = ydata
        self.path = path
    def psong(self):
        pass
        '''标题'''
        plot.title(self.title)
        '''X轴标题'''
        plot.xlabel(self.X)
        '''Y轴标题'''
        plot.ylabel(self.Y)
        if self.plotname == 'bar':
            '''柱型图'''
            plot.bar(self.xdata,self.ydata)
        elif self.plotname == 'pie':
            '''扇型图'''
            plot.pie(self.xdata,labels=self.ydata,autopct='%1.1f%%', counterclock=False, startangle=90)
        elif self.plotname == 'plot':
            '''折现图'''
            plot.plot(self.xdata,self.ydata)
        if self.path:
            '''保存'''
            plot.savefig(self.path)
        else:
            '''查看'''
            plot.show()
            '''退出/结束'''
        plot.close()




'''AES加密解密,强度高,推荐使用'''
try:
    from cryptography.fernet import Fernet,InvalidToken
except ImportError:
    os.system("pip install cryptography")
class AESCipher:
    def __init__(self):
        pass
    '''加密流程'''
    def encode_text_for_confusion(self,text:str,if_save:bool=False,my_key:bytes=None)->dict:
        """传入参数：text=需要加密的文本\n
        if_save=是否保存密钥\n
        my_key=自定义密钥需要传入字节串类型,例如b'1234567890123456'"""
        if my_key:
            key = my_key
        else:
            key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(text.encode())
        if if_save:
            with open('key.key', 'wb') as file_object:
                file_object.write(key)
            with open('saveText.txt', 'wb') as file_object2:
                file_object2.write(encrypted_data)
            print('OK!key saved to key.key')
        elif not if_save:
            return {'You_AES_key':key,'You_AES_text_data':encrypted_data}
    '''解密流程'''
    def decode_text_from_confusion(self,Text_data:str=None,Text_path:str=None,AESkey:str=None,AESkey_path:str=None,Save_date:bool=False,Save_date_path:str=None)->str:
        """#传入参数:Text_data=需要解密的文本数据\n
        或Text_path=者文本路径、AESkey=AES密钥\n
        或者AESkey_path=AES密钥路径、\n
        Save_date=是否保存解密后数据、\n
        Save_date_path=保存解密后数据路径"""
        #判断用户怎么传入加密数据
        if Text_path!=None:
            with open(Text_path, 'rb') as file_object:
                encoded_bytes = file_object.read()
        elif Text_data!=None:
            encoded_bytes = Text_data
        else:
            print('text is not')
            return -1
        #判断用户怎么传入密钥
        if AESkey!=None:
            key = AESkey
        elif AESkey_path!=None:  
            with open(AESkey_path, 'rb') as file_object:
                key = file_object.read()
        else:
            print('key is not')
            return -2
        #加载密钥
        try:
            keys = Fernet(key)
        except ValueError as f:
            print('请输入规范的AES密钥')
            return f
        #尝试解锁
        try:
            jiemi = keys.decrypt(encoded_bytes)
            if Save_date:
                save_file_path = os.getcwd()+'/AES_text.txt'
                if Save_date_path:
                    save_file_path = Save_date_path
                with open(save_file_path,'wb',encoding='utf-8') as p:
                    p.write(jiemi.decode('utf-8'))
            else:
                return jiemi.decode('utf-8')
        except InvalidToken:
            return 'KeyError'
        

'''AIS加密解密,加密强度不足,不建议使用'''
class AISCipher:
    def __init__(self) -> None:
        pass
    '''加密流程'''
    def encode_text_for_confusion(self,text:str,key:int)->bytes:#传入参数：需要加密的文本、自定义密钥需要传入整数类型,int数值必须在60以上,否则加密强度不足
        assert key > 60,"key值必须为60以上"
        #对文本进行编码以产生乱码效果，key是用于编码的密钥
        encoded_bytes = bytearray()  
        for char in text.encode('utf-8'):  
            encoded_char = (char ^ key) % 256  # 使用异或操作进行编码  
            encoded_bytes.append(encoded_char)  
        return encoded_bytes
    '''加密+写入文件流程'''
    def write_encoded_text_to_file(self,text:str,filename:str,key:int)->dict:#传入参数：需要加密的文本、保存的文件名.txt、自定义密钥需要传入整数类型,int数值必须在60以上,否则加密强度不足
        #"""将编码后的文本写入文件
        encoded_bytes = self.encode_text_for_confusion(text, key)
        with open(filename, 'wb') as f:
            f.write(encoded_bytes)
        return {'AIS_data':encoded_bytes,'key':key}
    '''解密流程'''
    def decode_text_from_confusion(self,encoded_bytes:str, key:int)->str:#传入参数：需要解密的文本数据、自定义密钥需要传入整数类型,解密返回值需自行判断成功与否
        #对编码后的文本进行解码以恢复原始文本
        decoded_bytes = bytearray()
        for char in encoded_bytes:  
            decoded_char = (char ^ key) % 256  # 使用相同的异或操作进行解码
            decoded_bytes.append(decoded_char)  
        try:
            return decoded_bytes.decode('utf-8') 
        except UnicodeDecodeError as fs: 
            t=str(fs)
            print(type(t))
            if t == "' utf-8' codec can't decode byte 0xff in position 0: invalid start byte":
                return '无法展示'
            else:
                print('文件已损坏,Error:',t) 
                return None
    '''解密+读取文件流程'''
    def read_and_decode_text_from_file(self,filename:str,key:int)->str:#传入参数：需要解密的文件名.txt、自定义密钥需要传入整数类型,解密返回值需自行判断成功与否
        #从文件中读取编码后的文本并解码
        with open(filename, 'rb') as f:
            encoded_bytes = f.read()
            txtnum = len(encoded_bytes)
            if txtnum <= 1:
                return('null')
            else:
                return self.decode_text_from_confusion(encoded_bytes, key)


'''键盘监听线程'''
try:
    from pynput.keyboard import Listener
except ImportError:
    os.system("pip install pynput")
try:
    import threading
except ImportError:
    os.system("pip install threading")
class Listener_listen:
    """
    结束线程可以通过RSACipher().stop_event.set()方法释放线程资源\n
    可参考以下代码测试\n
    t = Listener_listen()\n
    def test(key):\n
         print('{0}字符键'.format(key.char()))\n
    t.listen_start(test)\n
    import time\n
    time.sleep(5)\n
    t.stop_event.set()\n
    time.sleep(5)
    """
    def __init__(self) -> None:
        self.stop_event = threading.Event()
        self.thread = None
    '''监听线程启动'''
    def listen_start(self,func)->None:
        """传入一个函数作为监听的线程操作,否则线程无意义,线程自动传入key参数,返回按键值\n
        不允许无限循环监听函数,线程只允许启动一次,否则造成资源浪费\n
        Pass in a function as a listening thread operation, otherwise the thread is meaningless. The thread automatically passes in the key parameter and returns the key value\n
        Infinite loop listening function is not allowed, threads are only allowed to start once, otherwise it will cause resource waste
        """
        if self.thread is None or not self.thread.is_alive():
            def listen():
                with Listener(on_press=func) as listener:#自动向函数传入key类型参数,需要使用char属性转为字符类型
                    self.stop_event.wait()
                    pass
            self.thread = threading.Thread(target=listen, daemon=True)
            self.thread.start()
    def listen_stop(self)->None:
        """结束监听线程"""
        self.stop_event.set()


try:
    import pandas as pd
except ImportError:
    os.system("pip install pandas")
    os.system("pip install openpyxl")
'''pandas数据处理'''
class PdConvert():
    def __init__(self):
        self.FILEDE = None
    '''表格转列表'''
    def pd_list(self,axis:int=0,get_value:str=None,) -> list:
        """传入参数：数据轴、获取列字段数据\n
        axis=数据轴,0为行,1为列\n
        get_value=当选定axis=1时,get_value参数不能为空,必须获取一个列作为引索\n
        返回值：列表
        """

        if axis == 0:
            return [self.FILEDE.loc[u].tolist() for u in range(len(self.FILEDE))]
        elif axis == 1:
            assert get_value, "当选定axis=1时,get_value参数不能为空,必须获取一个列作为引索"
            return self.FILEDE[get_value].tolist()


    '''表格转字典'''
    def pd_dict(self,setindex:str=None,orient:str='index',get_value:list|str=None) -> dict:
        """传入参数：是否以列作为引索、是否以列作为做为该行数据字典键、获取某一列的数据当要获取的数据大于1时使用,列表作为参数"""
        
        if not setindex:
            if not get_value:
                return [self.FILEDE.loc[u].to_dict() for u in range(len(self.FILEDE))]
            elif get_value:
                if orient:
                    return self.FILEDE[get_value].to_dict(orient=orient)
                else:
                    return self.FILEDE[get_value].to_dict()
        elif setindex:
            new_FILEDE = self.FILEDE.set_index(setindex,inplace=False)
            # assert get_value, "当选定setindex作为索引时,get_value参数不能为空,必须获取至少一个列名作为setindex键的对象值"
            if get_value:
                if orient == 'index':
                    return new_FILEDE[get_value].to_dict(orient='index')
                elif not orient:
                    return new_FILEDE[get_value].to_dict()
                elif orient:
                    return new_FILEDE[get_value].to_dict(orient=orient)
            else:
                return new_FILEDE.to_dict(orient=orient)
    '''导入数据'''
    def import_pd_data(self,path:str,pd_data:pd.DataFrame=None,filetype:str='xlsx',sheet_name:str='Sheet1',fillna:bool = False,fillna_value:any=0,self_pd:bool=True) -> pd.DataFrame|None:
        """传入参数：文件路径、文件类型、数据轴、sheet名、是否填充缺失值、填充缺失值、是否以本类数据输出,默认True\n
        - path=文件路径\n
        - pd_data=传入DataFrame数据,默认为空\n
        - filetype=文件类型,默认xlsx\n
        - sheet_name=sheet名,默认Sheet1\n
        - fillna=是否填充缺失值,默认False\n
        - fillna_value=填充缺失值,默认0\n
        - self_pd=已有数据是否作为本类数据还是输出数据,默认True\n
        - 存入：DataFrame数据
        """
        if pd_data:
            assert isinstance(pd_data,pd.DataFrame),"传入DataFrame数据类型错误,请检查"
            self.FILEDE = pd_data
        else:
            if filetype not in ['xlsx','csv']:
                raise pd_file_type_error('只允许xlsx和csv文件')
            if filetype == 'xlsx':
                if not self_pd:
                    return pd.read_excel(path,sheet_name=sheet_name)
                self.FILEDE = pd.read_excel(path,sheet_name=sheet_name)
            elif filetype == 'csv':
                if not self_pd:
                    return pd.read_csv(path)
                self.FILEDE = pd.read_csv(path)
        if fillna:
            self.FILEDE.fillna(fillna_value,inplace=True)

    def pd_cont_function(self,function,pd_data:pd.DataFrame=None) -> pd.DataFrame:
        """
        ## function:
            - 'value_counts':统计各个值出现的次数
            - 'describe':统计数据集的描述性统计指标
            - 'unique':返回唯一值
            - 'nunique':返回唯一值的数量
            - 'count':返回非空值的数量
            - 'max':返回最大值
            - 'min':返回最小值
            - 'fillna':填充缺失值
            - 'dropna':删除缺失值
            - 'drop_duplicates':删除重复值
        """
        data = pd_data
        match function:
            case 'value_counts':
                return data.value_counts(sort=True)
            case 'describe':
                return data.describe()
            case 'unique':
                return data.unique()
            case 'nunique':
                return data.nunique()
            case 'count':
                return data.count()
            case 'max':
                return data.max()
            case'min':
                return data.min()
            case 'fillna':
                return data.fillna(0)
            case 'dropna':
                return data.dropna()
            case 'drop_duplicates':
                return data.drop_duplicates()


'''时间方差计算'''
def timefc(time_str:list,time_format:str,time_conversion=(60 * 60 * 24))->float:#传入参数：方差时间列表(len(list)==2)、时间转换格式、时间转换单位,默认单位为秒
    """
    计算时间差值,返回时间差值单位为秒
    :param time_str: 时间列表,len(list)==2>>>列表传参格式为['2021-01-01 00:00:00','2021-01-02 00:00:00']
    :param time_format: 时间格式>>>传入格式为'%Y-%m-%d %H:%M:%S'
    :param time_conversion: 时间转换单位,默认单位为秒>>>传参格式式(60 * 60 * 24)
    :return: 时间差值
    """
    from datetime import datetime
    date1 = datetime.strptime(time_str[0],time_format)
    date2 = datetime.strptime(time_str[1],time_format)
    print(type(date1))
    delta = date2 - date1
    full_days_difference = delta.total_seconds() / time_conversion
    return full_days_difference



def extract_tags(text,topK,withWeight,allowPOS=None):
    import jieba.analyse as an
    return an.extract_tags(text,topK,withWeight,allowPOS)
    


import sqlite3
'''sqlite数据库简化操作'''
class Sql:
    """you can use this class to create a sqlite database and execute SQL statements."""
    def __init__(self,sqlpath:str):
        self.conn = sqlite3.connect(sqlpath)
        self.cursor = self.conn.cursor()
    def createTable(self,tableName:str,IDisIindexKey:bool=True,SQLTextCent:str=None) -> None:
        """
        >>>CREATE TABLE IF NOT EXISTS YourTableName (\n
        tableName=创建表格\n
        IDisIindexKey=是否以id为索引\n
        >>>id INTEGER PRIMARY KEY,\n
        SQLTextCent=SQL语句,默认为空将创建两个字段Name和Password\n
        >>>Name TEXT NOT NULL,\n
        >>>Password INTEGER NOT NULL\n
        )
        """
        TextCent = """
            Name TEXT NOT NULL,
            Password INTEGER NOT NULL"""
        if IDisIindexKey:
            idindex = 'id INTEGER PRIMARY KEY,'
        if SQLTextCent != None:
            TextCent = SQLTextCent
        self.createTableText = f"""
            CREATE TABLE IF NOT EXISTS {tableName} (
            {idindex}
            {TextCent}
        )
        """
        self.cursor.execute(self.createTableText)
        self.conn.commit()

    def ShowTable(self) -> None:
        """查询语句:\n
        >>>SELECT name FROM sqlite_master WHERE type='table'"""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        print(self.cursor.fetchall())

    def InsertData(self,tableName:str,datatage:str,datavalue:str) -> None:
        """数据插入语句:\n
        tableName = 表格名\n
        datatage = 列名\n
        datavalue = 值\n
        >>>INSERT INTO {YourTableName:users} ({YourColumnName:Name,Password}) VALUES {(YourValue:user1,123456),(YourValue:user2,654321)}
        """
        insertText = f"""
            INSERT INTO {tableName} ({datatage})
            VALUES {datavalue}
        """
        self.cursor.execute(insertText)
        self.conn.commit()

    def DataUpdata(self,tableName:str,set_value_Text:str,where_value_Text:str) -> None:
        """数据更新语句:\n
        >>>UPDATE {tableName:users}\n
        >>>SET {set_value_Text:age = 26}\n
        >>>WHERE {where_value_Text:name = 'Alice}'
        """
        text = f'''
            UPDATE {tableName}
            SET {set_value_Text}
            WHERE {where_value_Text}
        '''
        self.cursor.execute(text)
        self.conn.commit()

    def deleteData(self,tableName:str,where_value_Text:str) -> None:
        """数据删除语句:\n
        >>>DELETE FROM {tableName:users}\n
        >>>WHERE {where_value_Text:name = 'Bob'}
        """
        self.cursor.execute(f'''
            DELETE FROM {tableName}
            WHERE {where_value_Text}
        ''')
        self.conn.commit()

    def SelectData(self,tableName:str,expression:str) -> list:
        """查询表数据语句:\n
        >>>SELECT {expression:*} FROM {tableName:users}
        """
        selectText = f"""
                SELECT {expression} FROM {tableName}
            """
        self.cursor.execute(selectText)
        return self.cursor.fetchall()
    
    def deleteTbale(self,tableName:str) -> None:
        """删除表语句:\n
        >>>DROP TABLE {tableName:users}
        """
        self.cursor.execute(f'''
            DROP TABLE {tableName}
        ''')
        self.conn.commit()

    def conn_close(self):
        self.conn.close()
        return True

'''鼠标点击器'''
def pymove(x:int=None,y:int=None,num:int=1,times:float=0.1)->None:
    """传入x,y坐标,鼠标移动到指定坐标并点击\n
    没有传入参数及获取当前位置点击\n
    点击多少次?间隔多少秒?"""
    import pyautogui
    if not x and y:
        x,y = pyautogui.position()
    pyautogui.moveTo(x,y)
    i = 0
    while i <= num:
        time.sleep(times)
        pyautogui.click()
        i += 1
'''键盘点击器'''
def ket_click(key:list|str|tuple,parallel:bool=True,times:float=0.1):
    """- 列表/元祖或者字符串类型\n
    - 并行按下默认为True,False分别按下按键,按键间隔时间默认为0.1秒\n"""
    import keyboard
    if isinstance(key,list):
        str_key = key
    else:
        str_key = [i for i in key]
    if parallel:
        keyboard.press(str_key)
    else:
        for key_str in str_key:
            keyboard.press(key_str)
            time.sleep(times)


class socket_client:
    def __init__(self):
        pass
    



'''Python文件打包Windows可识别exe文件'''
def py_to_exe():
    try:
        os.system('auto-py-to-exe')
    except:
        os.system('pip install auto-py-to-exe')
    os.system('auto-py-to-exe')


'''使用windos命令行运行powershell脚本'''
try:
    import subprocess
except ImportError:
    os.system("pip install subprocess")
def windows_run_powershell(run_str:str):
    subprocess.run(['powershell',run_str], capture_output=True, text=True)
'''1'''
#--------------------------------------------------------------------------->Functions End<--------------------------------------------------------------------------
#                                                                                               #
    #                                                                                       #
        #                                                                               #
            #                                                                       #
                #                                                               #
                    #                                                       #
                        #                                               #
                            #                                       #
                                #                               #
                                    #                       #
                                        #               #
                                             #      #
                                                #                                                  
#                                                                                               #
    #                                                                                       #
        #                                                                               #
            #                                                                       #
                #                                                               #
                    #                                                       #
                        #                                               #
                            #                                       #
                                #                               #
                                    #                       #
                                        #               #
                                             #      #
                                                #                                                  #                                                                                               #
    #                                                                                       #
        #                                                                               #
            #                                                                       #
                #                                                               #
                    #                                                       #
                        #                                               #
                            #                                       #
                                #                               #
                                    #                       #
                                        #               #
                                             #      #
                                                #                                                  
#--------------------------------------------------------------------------->verify start<--------------------------------------------------------------------------
'''&*%$#@!库签名不允许调用该函数,请勿使用'''
def _BelongTo():
    belong_to = binary_to_char([1010111,1100101,1101110,1011000,1101001,1100001,1101111,1001000,1110101,1100001])
    return belong_to
def _mains():
    list_date = AESCipher().decode_text_from_confusion(Text_data=b'gAAAAABm445I-lWPKoVZGWHcflrcqO6RQZOZLse3fHtIgo1CWAia4nAfpHPEHcH3CZs62E_YMwdCyD2pOizh42ZgwrZPZt-bNHLNEOtso3651CuyrZ144v7NwPANwDr64gutD9R4NOw5PSULPO3LsmCt_0UhbWCX-8svd4cJ7pHdLcdNiZDWO7fUhmhIrt-2rT9Rz_pOijzr',AESkey=b'dONRzSDHakRGvnfdhxo6A6qsd5nVY9pXcUxC5hrEAlg=')
    return list_date
def _test_and_verify():
    A_key = _BelongTo()
    B_key = _mains()
    # for A_key_i,B_key_i2 in zip(A_key,B_key):
    assert A_key != B_key, "Signature mismatch, please download the source code again and install the dependency package!"
if __name__ == '__main__':
    pass
elif __name__ != '__main__':
    _test_and_verify()