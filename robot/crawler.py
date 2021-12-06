from bs4 import BeautifulSoup
import re
import requests

def search_web(item):
	# search website
	search_url = 'https://www.boohee.com/food/search?keyword='

	search = search_url + item

	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"}

	html = requests.get(search, headers = headers)

	bs_obj = BeautifulSoup(html.text, 'html.parser')

	match = bs_obj.find('a', target='_blank')

	# food website
	food_url = 'https://www.boohee.com' + match['href']

	html = requests.get(food_url, headers=headers)

	bs_obj = BeautifulSoup(html.text, 'html.parser')

	match = bs_obj.find('ul').find('a').text

	recipe = {}
	response = ''
	if(re.match('.*菜',match)):
		nutrition_content = bs_obj.find('div', class_="nutr-tag").find_all('span', class_="dd")
		"""
		calorie = re.findall(r'(?<=热量\(大卡\)).*(\n)', nutrition_content)
		print(calorie[0])
		carbohydrate = re.findall(r'(?<=碳水化合物\(克\)).*(\n)', nutrition_content)[0]
		fat = re.findall(r'(?<=脂肪\(克\)).*(\n)', nutrition_content)[0]
		protein = re.findall(r'(?<=蛋白质\(克\)).*(\n)', nutrition_content)[0]
		"""

		ingredients = bs_obj.find('div', class_="widget-more").find('div', class_="content").find_all('a')
		ingredient_list = []
		for i in ingredients:
			ingredient_list.append(i.text)
		recipe['ingredient'] = ingredient_list
		recipe['calorie'] = nutrition_content[2].text
		recipe['carbohydrate'] = nutrition_content[3].text
		recipe['fat'] = nutrition_content[4].text
		recipe['protein'] = nutrition_content[5].text
		
	else:
		nutrition_content = bs_obj.find('div', class_="nutr-tag").find_all('span', class_="dd")
		recipe['calorie'] = nutrition_content[2].text
		recipe['carbohydrate'] = nutrition_content[3].text
		recipe['fat'] = nutrition_content[4].text
		recipe['protein'] = nutrition_content[5].text
		#response = '卡路里为'+recipe['calorie']+'大卡,碳水化合物为'+recipe['carbohydrate']+'g,脂肪为'+recipe['fat']+'g,蛋白质为'+recipe['protein']+'g。'
	return recipe
