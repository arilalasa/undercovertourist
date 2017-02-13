Environemnt:
python  version -- 2.7
django version 1.10.5

To install DB, please do make migrations and sync db to create tables on you local storage app

FOR TEST CASES INSTALL REBAR
pip install rebar

 Run project on your local server and access the project using 
 http://127.0.0.1:8000/undercovertourist/
 
 
Index page --> It has list of tours with respective prices

Details page ---> It has details of the product and gives purchase option if the inventory is greater than 1

purchase page --> Gives a Form with autofill for item id, enter the customer details and submit. This will place order for the product and store in DB

sucess page -- > If quantity entered is less than inventory on hand, it will take us to success page with confirmation code

Fail page --> If quamtity entered is greater than inventory n hand, it will give failure page



