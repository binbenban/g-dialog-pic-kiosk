import os
import subprocess

import psutil
from fastapi import FastAPI
from starlette.requests import Request


app = FastAPI()


@app.post("/helloworld")
def read_root():
    return {"Hello": "World"}


@app.post("/start_show")
def start_show(request: Request):
    print(request)
    year = 2009
    kill_ifview_process()
    generate_file_list(year)
    generate_bat_file(year)
    run_ifview(year)
    return {
        "result": "startedddddd"
    }


def kill_ifview_process():
    PROCNAME = "i_view64.exe"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()


"""
generate (overwrite) file list for given year
"""
def generate_file_list(year: int):
    print("re-generating file list for {year}")
    pass


"""
generate (overwrite) the bat file on desktop
"""
def generate_bat_file(year: int):
    print("re-generating bat file for {year}")
    if not 2009 <= year <= 2030:
        raise ValueError("invalid year received: {year}. expected 2009 to 2030")

    desktop_path = "C:\\Users\\bin\\Desktop"
    ifview_path = "C:\\Program Files\\IrfanView\\i_view64.exe"
    filelist_path = os.getcwd() + "\\filelist\\" + f"{year}.txt" 
    with open(f"{desktop_path}\\{year}.bat", "w") as f:
        f.write(f'"{ifview_path}" /slideshow={filelist_path} /reloadonloop')


def run_ifview(year: int):
    cmd = [f"C:\\Users\\bin\\Desktop\\{year}.bat"]
    subprocess.Popen(cmd)
