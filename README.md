# Goal

goal is to 
- have a digital kiosk (a.k.a. signage) to display pictures and videos in the pcloud
- solution should be simple, robust, and with minimal human intervention

# Design

## Machine
Use an idle NUC running Windows 10 - this gives better configuration capability than Raspberry pi. Also I don't have that much time fiddling with RPi

## Media files
Using windows makes things simple. Install pcloud client, and sync picture folder to a folder on a folder on an attached external hdd. This gets synced automatically

## Running kiosk
Irfanview can do a slideshow of specified directory, including pictures and videos

## Running individual years
Create a file list for each year. Create a batch file to run slideshow for each year, using the corresponding file list.

```
"C:\Program Files\IrfanView\i_view64.exe" /slideshow=D:\slideshow\2009prior.txt /reloadonloop
```

# How to run

## Using batch command
double click on e.g. 2014.bat to start kiosk for that year
ESC to escape

## Google assistant integration
Use voice command to start kiosk for a given year
It will end any existing show, by killilng irfanview process

### notes
Use https endpoint as webhook URL
`https://e4852af1.ngrok.io/start_show`
