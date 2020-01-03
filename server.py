import os
import subprocess

import psutil
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from pathlib import Path


app = FastAPI()


@app.post("/helloworld")
def read_root():
    return {"Hello": "World"}


@app.post("/start_show")
async def start_show(request: Request):
    try:
        request_body = await request.json()
        print(request_body)
        year = request_body['queryResult']['parameters']['year']
        print(f"parameter year from request: {year}")
        validate_param(year)

        kill_ifview_process()
        generate_file_list(year)
        generate_bat_file(year)
        run_ifview(year)
        return {
            "fulfillmentText": "Slideshow started"
        }
    except:
        return {
            "fulfillmentText": "Something went wrong. Please try with a valid year"
        }


def validate_param(year: str):
    if not 2009 <= int(year) <= 2030:
        raise ValueError(f"invalid year received: {year}. expected 2009 to 2030")


def kill_ifview_process():
    PROCNAME = "i_view64.exe"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()


"""
generate (overwrite) file list for given year
"""
def generate_file_list(year: str):
    media_path = "D:\\pcloud_sync"
    print(f"re-generating file list for {year}")
    if year == '2009':
        years = range(2002, 2010)
    else:
        years = [year]
    # combine all 2002 to 2009
    file_list_all = []
    for a_year in years:
        file_list_all += list(Path(f"{media_path}\\{a_year}").glob('**/*.*'))
    file_list = sorted([str(f) for f in file_list_all if not 'txt' in str(f)])
    print(len(file_list))
    if not file_list:
        raise ValueError(f"no file found for year {year}")
    with open(f"filelist/{year}.txt", "w") as f:
        for file in file_list:
            f.write(f"{file}\n")


"""
generate (overwrite) the bat file on desktop
"""
def generate_bat_file(year: str):
    print(f"re-generating bat file for {year}")
    desktop_path = "C:\\Users\\bin\\Desktop"
    ifview_path = "C:\\Program Files\\IrfanView\\i_view64.exe"
    filelist_path = os.getcwd() + "\\filelist\\" + f"{year}.txt" 
    with open(f"{desktop_path}\\{year}.bat", "w") as f:
        f.write(f'"{ifview_path}" /slideshow={filelist_path} /reloadonloop')


def run_ifview(year: str):
    cmd = [f"C:\\Users\\bin\\Desktop\\{year}.bat"]
    subprocess.Popen(cmd)
