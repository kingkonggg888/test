import multiprocessing
import tkinter as tk

processes = []  # เก็บรายการกระบวนการ

def test():
    # ตัวอย่างฟังก์ชันที่ต้องการให้ทำงาน
    while True:
        print("Hello from process:", multiprocessing.current_process().name)

def start_process():
    process = multiprocessing.Process(target=test)
    process.start()
    processes.append(process)  # เพิ่มกระบวนการลงในรายการ

def stop_processes():
    for process in processes:
        process.terminate()
        process.join()
    processes.clear()  # ล้างรายการกระบวนการ

def on_closing():
    stop_processes()
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("MultiProcessing Example")

    start_button = tk.Button(root, text="Start", command=start_process)
    start_button.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

if __name__ == '__main__':
    main()
