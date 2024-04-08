query_schema = 'CREATE SCHEMA IF NOT EXISTS `abc_company` DEFAULT CHARACTER SET utf8 ;'

employees = '''CREATE TABLE EMPLOYEES (
	employee_number int not null primary key,
    gender varchar (5),
    date_birth year
    );'''

employee_details ='''CREATE TABLE EMPLOYEE_DETAILS (
	employee_number int not null,
    department varchar (45),
	job_role varchar (45),
	job_level int,
	job_involvement int, 
	years_at_company int, 
	years_in_current_role int, 
	years_since_last_promotion int, 
	years_with_current_manager int, 
	training_times_last_year int, 
	remote_work bool, 
	performance_rating int,  
	attrition bool,
	marital_status varchar (45),
	distance_from_home int unsigned ,
	education  int, 
	education_field varchar (45),
	total_working_years int,  
	num_companies_worked int,
	constraint FK_employee_number2
		foreign key (employee_number) 
        references EMPLOYEES(employee_number) on delete cascade on update restrict
    );'''

economic = '''CREATE TABLE ECONOMIC (
	employee_number int not null,
    monthly_income float,
	hourly_rate float, 
	monthly_rate float, 
	daily_rate float,
	percent_salary_hike float,
	stock_option_level float, 
	business_travel varchar (45), 
	over_time bool, 
    constraint FK_employee_number3
		foreign key (employee_number) 
        references EMPLOYEES(employee_number) on delete cascade on update restrict
    );'''

satisfaction = '''CREATE TABLE SATISFACTION (
	employee_number int not null,
	environment_satisfaction int, 
	job_satisfaction int,
	relationship_satisfaction int, 
	work_life_balance int, 
	  constraint FK_employee_number4
		foreign key (employee_number) 
        references EMPLOYEES(employee_number) on delete cascade on update restrict
    );'''