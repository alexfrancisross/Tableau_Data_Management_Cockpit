# Tableau Data Management Cockpit Overview
This Repo Contains The Source Code For The Tableau Data Management Cockpit (credit to @Darren McGurran)

The Tableau Data Management Cockpit provides enhanced admin views and data sources that are based on the Tableau Catalog Metadata API. The solution uses Python to mine Tableau and External assets in the Catalog and generates a .hyper file with each of these assets in separate tables:
![image](https://user-images.githubusercontent.com/11485060/207291316-4cc6322c-145d-4edb-bda0-99cfd45bb8f0.png)

There is an accompanying workbook called `Data Management Content vx.x.twb` which provides a template for how these tables can be related to generate a data source with the upstream and downstream assets:
![image](https://user-images.githubusercontent.com/11485060/207292672-a2ad264c-b941-4720-b746-46dfd91bb6fc.png)

The workbook contains 3 dashboards:
1. **Tableau Data Management Cockpit** - provides an overview of utilisation across each site including top projects/publishers, # workbooks over time, popular data sources and databases:
![image](https://user-images.githubusercontent.com/11485060/207293002-00e5f8fd-0cb1-4a5f-be33-92feba74f757.png)
2. **Tableau Data Management databases** - provides an overview of how databases and database types are being utilised across each site:
![image](https://user-images.githubusercontent.com/11485060/207293277-d48925e2-8e82-4329-912f-b70123f8befd.png)
3. **Tableau Data Management Impact Analysis** - provides information on external assets and tableau assets, allowing users to identify downstream impact:
![image](https://user-images.githubusercontent.com/11485060/207293725-e7cdd067-04f3-406a-ac58-516ca344e6fe.png)

# Instructions
1. Edit the `settings.json` file located in the `/data` directory to include your Tableau Server/Cloud and personal access token details. Note that the Server Type should be set to either `on_prem` or `cloud` and the `TS_SERVER_URL` variable should reflect the full dns of your Tableau Server / Tableau Cloud Site e.g. `https://prod-uk-a.online.tableau.com`
![image](https://user-images.githubusercontent.com/11485060/207326853-1327abe2-294c-4567-9f9d-af66d04bbd7c.png)
2. Ensure you have a working python 3.x installation with the following packages installed:

`pip install tableauhyperapi`

`pip install tableauserverclient`

`pip install iso8601`

`pip install psycopg2`

3. Run the following command to run the application and generate the output hyper file:

`python main.py`

![image](https://user-images.githubusercontent.com/11485060/207330545-12eeecb0-9de2-461f-8628-cd658cb162bc.png)
4. Open the Tableau Workbook `Data Management Content vx.x.twb` in the `/output` directory and replace the data source with the newly generated hyper file from step 3:
![image](https://user-images.githubusercontent.com/11485060/207334012-bb0091cf-4bec-4422-9063-4651387838bb.png)

