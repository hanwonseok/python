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

    Init_ctrl(mainFrom)
    
    mainFrom.mainloop()

#컨트롤들 초기화
def Init_ctrl(mainFrom):
    canvas = tkinter.Canvas(mainFrom, width=590, height=790, bg="white")
    canvas.pack(padx=5,pady=5)
    for i in range(0, 601, 10):
        if(i % 50 == 0):
            canvas.create_line(i, 0, i, 790, fill="red")            
        else:
            canvas.create_line(i, 0, i, 790, fill="black")            
    
    Init_RoomTitle_Ctrl(mainFrom)
    Init_btnSetting(mainFrom)


#텍스트박스 초기화
def Init_RoomTitle_Ctrl(mainFrom):
    x_location = 50
    
    lbl_RoomTitle = tkinter.Label(mainFrom, text="톡방명")
    lbl_RoomTitle.place(x=x_location, y=50)
    
    txt_roomTitle = tkinter.Entry(mainFrom, text="카카오뱅크")
    txt_roomTitle.place(x=x_location + 50, y=50)


#버튼 초기화
def Init_btnSetting(mainFrom):
    btn_start = tkinter.Button(mainFrom, text="구동시작")
    btn_start.place(x=500, y=20)
    
    btn_end = tkinter.Button(mainFrom, text="구동종료")
    btn_end.place(x=500, y=60)


if __name__ == '__main__':
    show();