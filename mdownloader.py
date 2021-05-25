#!/usr/bin/env python3
import subprocess
import pafy
import os

links = []

def load_list(link_file):
	try:
		os.stat('download')
	except:
		os.mkdir('download') 
	for lines in open(link_file):
		line = lines.strip()
		links.append(line)

def download_file():
	for link in links:
		try:
			video = pafy.new(link)
			audio = video.audiostreams
			audio[1].download(filepath='download/')
		except:
			print('error file'+links.index(link))
			pass
	print('base_downloaded')

def convert_file(output):
	for file in os.listdir('download/'):
		if file.endswith('.webm'):
			music = 'download/'+file
			command= ['ftransc','-f', output, music]
			subprocess.run(command)
	print('base_converted')

def pos_clear():
	for file in os.listdir('download/'):
		if file.endswith('.webm'):
			os.remove('download/'+file)
	print('directory-cleared')

while True:
	file = input('link_file: ')
	outf = input('format: ')
	load_list(file)
	download_file()
	convert_file(outf)
	pos_clear()
	break
