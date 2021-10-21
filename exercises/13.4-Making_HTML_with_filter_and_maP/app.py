all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(item):
	if item["sexy"]:
		return item["label"]
new_list=list(filter(generate_li, all_colors))	
print(new_list)	
def filter_colors(item):
    
	return "<li>"+item['label']+"</li>"
new_list2=list(map(filter_colors,new_list))	
print (new_list2)
sex=""
for i in new_list2:
	sex+=i
print(sex)	

