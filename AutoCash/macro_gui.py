import global_variable as g
import tkinter

#구성된 UI로 화면은 표시한다
def show():
    print('-show-시작-------------------------------------------------------')
    try:
        print('이곳이 gui 만들어질곳')
        Init_mainFrom();
        
    except Exception as e:
        print('-show-에러-[', e, ']')
        
    finally:
        print('show-종료----------------------------------------------------')
        
#메인 화면 설정
def Init_mainFrom():
    mainFrom = tkinter.Tk()
    mainFrom.wm_title('AutoCash')
    mainFrom.geometry('600x800')
    
    Init_btnSetting(mainFrom)
    
    mainFrom.mainloop()

#버튼 초기화
def Init_btnSetting(mainFrom):
    btn_start = tkinter.Button(mainFrom, text="구동시작")
    btn_start.location(10, 10)
    btn_start.pack()
    
    btn_end = tkinter.Button(mainFrom, text="구동종료")
    btn_end.location(50, 50)
    btn_end.pack()