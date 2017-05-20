import requests
import json
order = []
# product = []
my_dict = []
# id = []
throw = []
total_cookies = 0

for i in range(1,12):
	r = requests.get("https://backend-challenge-fall-2017.herokuapp.com/orders.json?page=" + str(i))
	b=r.json()
	total_cookies = b["available_cookies"]
	order.append(b.get("orders"))

# def id(order2):
# 	id = []
	
# 	for i in range(0,len(order2)):


# 		id.append(order2[i].get("id"))

# 	#j=j+1
	
# 	return id

def fullimentcheck(order):
	unfulfilled = []
	for i in range(0,len(order)):
		if len(order[i])!=0:
			for j in range(0,len(order[i])):
				if order[i][j].get("fulfilled") != True:
					unfulfilled.append(order[i][j])
	return unfulfilled

unfulfilled = fullimentcheck(order)
#print(unfulfilled)

def cookiecheck(unfulfilled):
	#product = []
	for i in range(0,len(unfulfilled)):
		for j in range(0,len(unfulfilled[i].get("products"))):
			# product.append(unfulfilled[i].get("product"))
			var = {}
			# if product[j].get("title") == "Cookie":
			if unfulfilled[i].get("products")[j].get("title")=="Cookie":
				var["ids"] = unfulfilled[i].get("id")
				# var["amounts"] = product[j].get("amount")
				var["amounts"] = unfulfilled[i].get("products")[j].get("amount")
				my_dict.append(var)
	return my_dict

#print(cookiecheck(unfulfilled))
# print(my_dict)

alist = cookiecheck(unfulfilled)
#print(alist)

def bubbleSort(alist):
    for passnum in range(0,len(alist)):
        for i in range(0,len(alist)-1):
            if alist[i].get("amounts")<alist[i+1].get("amounts"):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        x = alist
    return x

sorted_amount_id = bubbleSort(alist)
#print(sorted_amount_id)

def orderfinal(sorted_amount_id):
	cookies = total_cookies
	for i in sorted_amount_id:
		if i.get("amounts") > cookies:
			throw.append(i)
		else:
			cookies = cookies - i.get("amounts")

	return throw

a = orderfinal(sorted_amount_id)
print(a)



