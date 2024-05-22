# Data Testing Project for 'AdventureWorks' Database
The project goal is to perform several tests related to data checks in 3 different tables. 
This project involves creating and documenting test cases, automating these test cases, and generating test results report.

## Project Structure

```
DQE_PyTest_Project/
└── src/
     └── db/
          └── init.py
          └── dbconnection.py
          └── tables.py
     └── errors/
          └── init.py
          └── global_enums.py
└── test-reports/ 
       └── test_results.html.py
└── tests/
       └── init.py
       └── conftest.py
       └── test_person_address.py
       └── test_production_document.py
       └── test_production_unit_measure.py
└── settings.py
└── pytest.ini
└── requirements.txt
└── README.mb
```
### Prerequisites
* Python 3.x
* MSSQL Server
* Required Python packages listed in requirements.txt

### Installation

1. Set up MSSQL "AdventureWorks2012" database locally
2. Create user in MSSQL to connect from Python
3. Install Microsoft ODBC driver for SQL
4. Clone the repository to your local machine

```
git clone
https://github.com/kate1503/DQE_PyTest_Project.git
cd DQE_PyTest_Project
```
5. Install necessary Python packages (listed in requirements.txt)
```
pip install -r requirements.txt
```
6. Create .env file in the root project directory with your MSSQL user credentials and server port
```
DQE_PyTest_Project/
└── .env
...

USERID=your_user
PASSWORD=your_user_password
SERVER_PORT=your_server_port
```

### Running tests
To execute the automated tests and generate a report:
```
pytest --html=test-reports/test_results.html
```
Test report will be stored in the test-reports directory as test_results.html
