class Company:              #Company class or Base class for the employee
    company_name='Amdocs'
    designation_hrs={'Senior_Manager':10,'Manager':9,'Software_Developer':8,'Tester':7,'Accountant':6}
    company_address=''
    company_location=''

class Employee(Company):        #Employee class inherit the Company class ,in this class we have 7 function 1.Accept, 2.Display, 3.Information_by_rno
                                #4.Search, 5.CalculateSal, 6.MaxSal, 7.MinSal
    employee_name=''
    employee_roll_no=0
    employee_department=''
    employee_designation=''
    employee_salary=0
    Details_of_the_Employee_By_rno={}
    dept={'Data_&_Intelligence':[],'Optima':[],'Global Delivery':[],'SmartOps':[]}
    desg={'Senior_Manager':[],'Manager':[],'Software_Developer':[],'Tester':[],'Accountant':[]}
    city={'Pune':[],'Gurgaon':[]}
    def Accept(self,name,rollno,add,loc,dept,desg): #Accept function accept the Details of the employee --->> name, roll number,address, location, department, Designation
        self.employee_name=name
        self.employee_roll_no=rollno
        self.company_address=add
        self.company_location=loc
        self.employee_department=dept
        self.employee_designation=desg
        self.CalculateSal(self.designation_hrs[self.employee_designation])  #Calculate the salary and store it in the designation hour dictionary
        self.Details_of_the_Employee_By_rno[self.employee_roll_no]=[self.employee_name,self.employee_roll_no,self.company_name,self.company_address,self.company_location,self.employee_department,self.employee_designation,self.employee_salary]
        self.dept[self.employee_department].append(self.employee_roll_no)
        self.desg[self.employee_designation].append(self.employee_roll_no)
        self.city[self.company_location].append(self.employee_roll_no)
    def Display(self):         #Display the Details of the employee
        print("Total no of Employees present in record are",len(self.Details_of_the_Employee_By_rno))
        for k in self.Details_of_the_Employee_By_rno.keys():
            print(k,":",self.Details_of_the_Employee_By_rno[k])
    def Information_by_rno(self,rollno): #Showing the information by the roll number
        if rollno in self.Details_of_the_Employee_By_rno.keys():
            print("Employee's name is",self.Details_of_the_Employee_By_rno[rollno][0])
            print(self.Details_of_the_Employee_By_rno[rollno][0],"Roll no is",self.Details_of_the_Employee_By_rno[rollno][1])
            print(self.Details_of_the_Employee_By_rno[rollno][0],"works for Company named",self.Details_of_the_Employee_By_rno[rollno][2])
            print(self.Details_of_the_Employee_By_rno[rollno][0],"Company",self.Details_of_the_Employee_By_rno[rollno][2],"is located at",self.Details_of_the_Employee_By_rno[rollno][3],"in",self.Details_of_the_Employee_By_rno[rollno][4],"City")
            print(self.Details_of_the_Employee_By_rno[rollno][0],"works in Department named",self.Details_of_the_Employee_By_rno[rollno][5])
            print(self.Details_of_the_Employee_By_rno[rollno][0],"Designition is",self.Details_of_the_Employee_By_rno[rollno][6])
            print(self.Details_of_the_Employee_By_rno[rollno][0],"monthly salary is",self.Details_of_the_Employee_By_rno[rollno][7],"Rs")
            print("------------------------------------------------------------------------------")
        else:
            print("Given Employee does not exist as per Company's record");
    def Search(self):     #Search function search the employee details
        n=int(input("Enter the number for which you want to dispaly the information ,1 for Roll No. 2 for Department. 3 for Designation. 4 for City => "))
        if(n==1):         #Search the employee details by the roll number
            r=int(input("Enter value of Roll no => "))
            self.Information_by_rno(r)
        elif(n==2):       #Search the employee details from the deparment name
            d=input("Enter the Department on which you want to display the information => ")
            print()
            print(len(self.dept[d]),"Employees working for",d,"Department are =>")
            print()
            for r in self.dept[d]:
                print(self.Information_by_rno(r))
        elif(n==3):         #Search the employee details from the designation of the employee
            d=input("Enter the Designation on which you want to display the information => ")
            print()
            print(len(self.desg[d]),"Employees working on",d,"Designation are =>")
            print()
            for r in self.desg[d]:
                print(self.Information_by_rno(r))
        elif(n==4):         #Search the employee details from the city of the employee
            d=input("Enter the City on which you want to display the information => ")
            print()
            print(len(self.city[d]),"Employees working in",d,"City are =>")
            print()
            for r in self.city[d]:
                print(self.Information_by_rno(r))
        else:
            print("Invalid Input")
    def CalculateSal(self,hrs):
        self.employee_salary=10000*hrs
        
    def MaxSal(self):    #This function print the employee detail whose salary is maximum 
        print(len(self.desg['Senior_Manager']),"Employees with maximum monthly salary of 100000Rs are =>")
        for r in self.desg['Senior_Manager']:
                print(self.Information_by_rno(r))
    def MinSal(self):    #This function print the employee detail whose salary is minimum
        print(len(self.desg['Accountant']),"Employees with minimum monthly salary of 60000Rs are =>")
        for r in self.desg['Accountant']:
                print(self.Information_by_rno(r))
e=Employee()              #We have created the object of the employee class
n=int(input("Enter total number of Employees"))
for i in range(n):
    name=input("Enter name of Employee")
    rno=int(input("Enter Roll No of Employee"))
    add=input("Enter address of Company for Employee")
    city=input("Enter city of Company of Employee")
    dept=input("Enter department of Employee")
    desg=input("Enter designation of Employee")
    e.Accept(name,rno,add,city,dept,desg)

e.Display();
e.Search()

# e.Accept('Arsh Agrawal',1001,'Tower 2 Magarpatta','Pune','Data_&_Intelligence','Senior_Manager')
# e.Accept('Deepak Kewadiya',1002,'Unitech Infotech','Gurgaon','Optima','Software_Developer')
# e.Accept('Arpit Bamniya',1003,'Tower 4 Magarpatta','Pune','Data_&_Intelligence','Accountant')
# e.Accept('Gokul Ranabhat',1004,'Tower 6 Magarpatta','Pune','Data_&_Intelligence','Manager')
# e.Accept('Govardhan Reddy',1005,'Unitech Infotech','Gurgaon','Global Delivery','Software_Developer')
# e.Accept('Kush Saraswat',1006,'Tower 2 Magarpatta','Pune','Optima','Accountant')
# e.Accept('Harshit Kumar',1007,'Unitech Infotech','Gurgaon','Global Delivery','Tester')
# e.Accept('Amay Dave',1008,'Tower 4 Magarpatta','Pune','SmartOps','Software_Developer')
# e.Accept('Kumar Chitransh',1009,'Tower 6 Magarpatta','Pune','SmartOps','Manager')
