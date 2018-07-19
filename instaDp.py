"""********************************************************************
Author: Raghu cheekatla
Source code : github.com/raghu5rvm
Date: 20 Jul 2018 6:45:00 IST

"""
import urllib
import requests
import bs4
import string
import json
import sys, os
import webbrowser

flag = 1

while (flag!=0):
	insta_id = raw_input("Enter instagram userId:::")

	#insta_id = 'raghsalt'

	link = 'https://www.instagram.com/'+insta_id+'/'

	data = requests.get(link)

	print data

	data_bs4 = bs4.BeautifulSoup(data.text,'html5lib')

	#country_link_final = country_link_bs4.select('.country-selection__single-lang > a')

	try:
		scripts = data_bs4.select('script')

		shared_data = str(scripts[3])

		shared_data = shared_data.split("window._sharedData =")

		shared_data = shared_data[1]

		shared_data = shared_data[1:-10]

		#print shared_data

		d = json.loads(shared_data)

		uid = d['entry_data']["ProfilePage"][0]["graphql"]["user"]["id"]
		
		user_info_link = 'https://i.instagram.com/api/v1/users/'+uid+'/info/'
		
		print user_info_link
		
		user_info = requests.get(user_info_link)
		
		user_info_json = json.loads(user_info.text)
		
		user_image = user_info_json['user']['hd_profile_pic_url_info']['url']
		
		user_name = user_info_json['user']['full_name']
		
		print user_name
		
		print user_image		
		
		urllib.urlretrieve(user_image,insta_id+'/'+insta_id+".jpg")
		
		print("\n\n\t\tFile saved!!!\n\n")
		see = raw_input("Do you wish to view image online?(y/n)::")
		if(see=='y' or see =="Y" or see == "yes" or see == 'Yes' or see=="YES"):
			webbrowser.open(user_image)		
		"""
		curpath = os.path.abspath(os.curdir)

		print curpath
		
		data_dir = os.path.join(curpath,insta_id)
		
		print data_dir
		
		os.mkdir(data_dir)
		file_name = insta_id+"_info.json"
		f = open(os.path.join(data_dir,file_name),"w+")
		f.write(user_info_json)
		f.close();
			"""

	except:
		print ("\n\n\t\t\tWarning!!!\nProblem encountered during information fetch. Please check user name and try again\n\n")
	print ("\n\n*********************************************************\n\n")
	print ("\n1.Find another ")
	print ("\n0.Exit")
	flag= input("\nselect an option::")
