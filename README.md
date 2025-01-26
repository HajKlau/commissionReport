# Commission Report app

Create commission report for directors and sales representatives from database using Dash.

The Commission Report Project is an application that automates the process of calculating and visualizing monthly commissions for agencies and their directors. It uses a PostgreSQL database to store the data required for calculations. Based on this data, queries are generated, and the results are presented as interactive charts and tables using Pandas, Dash and Plotly. The project was inspired by prior professional experience, where a lack of automation significantly hindered similar analyses. This application makes the process faster, more transparent, and fully automated. Currently, this is an initial version of the application, which will be expanded with additional features in the future.

## Prerequisites
To properly run the application, you need a PostgreSQL database set up with the following specifications:

### Database Structure

The database should include the following tables:

#### directors
| directorid | directorfirstname | directorlastname | directorhiredate |
|------------|-------------------|------------------|------------------|
- **directorid** – primary key, unique identifier for the director (integer, auto-generated),
- **directorfirstname** – first name of the director (text, up to 255 characters),
- **directorlastname** – last name of the director (text, up to 255 characters),
- **directorhiredate** – the hire date of the director (date).

### agencies

2. agencies
3. sales_representatives
4. sales



    
do uruchomienia programu potrzebny bedzie rowneiz zainstalowany python w wersji min 3.11.

[Create Table Query](queries/createTables.sql "Create Table Query")


![Share in commissions](screenshots/share_in_commissions.png "Share in commissions")
## Running the app

1.Clone the repository from GitHub:
```
git@github.com:HajKlau/commissionReport.git
```
2. Navigate to the project directory:
```
 cd commissionReport
```
3.Running the app:
```
python3 commissionApp.py
```
