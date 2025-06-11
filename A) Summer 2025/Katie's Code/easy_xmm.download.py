#this Just downloads things from XMM

import os
from astropy.io import fits
import pandas as pd
from astroquery.esa.xmm_newton import XMMNewton
from sherpa.astro.ui import *
import glob
import tarfile
import requests
from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np

#should you redownload files and overwrite things?
redo_download = True

#Directory to download data into
#dir="/opt/pwdata/katie/xmm"
dir='/Users/kciurleo/Downloads'

#Extract tar file definition
def extract_all_files(tar_file_path, extract_to):
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(extract_to)

def download_full(observation_id):
    #move into download directory
    os.chdir(dir)
    
    #obsid needs to have 10 digits
    obsid = str(observation_id).zfill(10)
    print(f'Downloading {obsid}')

    #Download everything
    try:
        #Don't download it if it's already there
        if redo_download or not os.path.exists(f'{dir}/{obsid}'):
            XMMNewton.download_data(obsid, level='PPS', extension='FTZ')

            #Extract files and delete the big tar
            print(f'Extracting {obsid}')
            extract_all_files(f'{obsid}.tar', '')
            os.remove(f"{obsid}.tar") 
        else:
            print(f'Directory {obsid} already exists. Skipping download.')
    except:
        print(f'ERROR downloading {obsid}.')
    
def download_partial(observation_id, srcno):
    #move into download directory
    os.chdir(dir)
    
    #needs to have 10 digits
    obsid = str(observation_id).zfill(10)
    srcno=int(srcno)

    print(f'Downloading {obsid} source number {srcno}')

    #Download everything
    try:
        #Don't download it if it's already there
        if redo_download or not os.path.exists(f'{dir}/{obsid}'):
            #Download everything for the right source, source must be in hexagesimal
            XMMNewton.download_data(obsid, level='PPS',extension='FTZ', sourceno=f"{srcno:04X}")

            #Extract files and delete
            print(f'Extracting {obsid}')
            extract_all_files(f'{obsid}.tar', '')
            os.remove(f"{obsid}.tar") 
        else:
            print(f'Directory {obsid} already exists. Skipping download.')
    except:
        print(f'ERROR downloading {obsid}.')



def get_fits_info(file):
    #this gets the src num from the fits header of a file, which sometimes doesn't agree
    #also the ra and dec
    hdr = fits.getheader(f'{file}',ext=1)
    return hdr['SRCNUM'], hdr['SRC_RA'], hdr['SRC_DEC']




### Example usage:

download_partial(672780101, 140)
#print(get_fits_info('/Users/kciurleo/Downloads/0672780101/pps/P0672780101PNS021SRSPEC008C.FTZ'))