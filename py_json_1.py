import json

people='''
{
"Employees" : [
{
"userId":"rirani",
"jobTitleName":"Developer",
"firstName":"Romin",
"lastName":"Irani",
"preferredFullName":"Romin Irani",
"employeeCode":"E1",
"region":"CA",
"phoneNumber":"408-1234567",
"emailAddress":"romin.k.irani@gmail.com"
},
{
"userId":"nirani",
"jobTitleName":"Developer",
"firstName":"Neil",
"lastName":"Irani",
"preferredFullName":"Neil Irani",
"employeeCode":"E2",
"region":"CA",
"phoneNumber":"408-1111111",
"emailAddress":"neilrirani@gmail.com"
},
{
"userId":"thanks",
"jobTitleName":"Program Directory",
"firstName":"Tom",
"lastName":"Hanks",
"preferredFullName":"Tom Hanks",
"employeeCode":"E3",
"region":"CA",
"phoneNumber":"408-2222222",
"emailAddress":"tomhanks@gmail.com"
}
]
}'''

data = json.loads(people)
# print(data)

for i in data['Employees']:
    print(i)
    
new_str=json.dumps(data,indent=2,sort_keys=True)
print(new_str)