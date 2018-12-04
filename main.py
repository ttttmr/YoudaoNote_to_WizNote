import os,shutil

# 有道笔记数据目录
rootpath="/mnt/d/YoudaoNote/"
# 导出的PDF文件夹
rootdir="2018-11-25-23-53"
# 转换后目标文件夹
destdir="Linux_EX_HTML"
# 日志文件
logfile="log.txt"

with open(rootpath+logfile,'a') as f:
    f.write("\n---------- start ---------- \n"+rootpath)
    f.write("\n")

if not os.path.exists(rootpath+destdir):
    os.mkdir(rootpath+destdir)

c_path=os.path.abspath('.')

def pdf2html(f_pdf,outpath):
    # f_pdf.replace('\\','')
    # f_pdf.replace('"','')
    # f_pdf.replace("'",'')
    os.chdir(outpath)
    # out=os.popen(c_path+"\\pdf2htmlEX\\pdf2htmlEX.exe \""+f_pdf+"\""+">> log2.txt")
    # cmd=c_path+"\\pdf2htmlEX\\pdf2htmlEX.exe \"{0}\"".format(f_pdf)
    cmd="pdf2htmlEX \"{0}\"".format(f_pdf)
    os.system(cmd)


for root_dir_abspath,sub_dir_name_list,root_file_name_list in os.walk(rootpath+rootdir):
    dest_abspath=root_dir_abspath.replace(rootdir,destdir,1)
    root_dir_name=os.path.split(root_dir_abspath)[-1]
    with open(rootpath+logfile,'a') as f:
        f.write(root_dir_abspath)
        f.write("\n")
    for root_file_name in root_file_name_list:
        root_file_absname=os.path.join(root_dir_abspath,root_file_name)
        try:
            if os.path.splitext(root_file_name)[-1] == '.pdf':
                pdf2html(root_file_absname,dest_abspath)
                with open(rootpath+logfile,'a') as f:
                    f.write(root_file_absname)
                    f.write("\n")
            else:
                shutil.copyfile(root_file_absname,os.path.join(dest_abspath,root_file_name))
        except:
            try:
                with open(rootpath+logfile,'a') as f:
                    f.write(root_file_absname)
                    f.write(" Fail!!!")
                    f.write("\n")
            except:
                pass
    for sub_dir_name in sub_dir_name_list:
        try:
            os.mkdir(os.path.join(dest_abspath,sub_dir_name))
        except:
            pass