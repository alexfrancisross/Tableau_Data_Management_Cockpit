# Tableau Data Management Cockpit Overview
This Repo Contains The Source Code For The Tableau Data Management Cockpit. Written by @Darren Mcgurran

The Tableau Data Management Cockpit provides enhanced administration views and data sources that are based on the Tableau Catalog Metadata API. The solution uses Python to mine Tableau assets in the Catalog and generates a .hyper file in the /output folder with each of these assets in separate tables:
![image](https://user-images.githubusercontent.com/11485060/207291316-4cc6322c-145d-4edb-bda0-99cfd45bb8f0.png)

There is an accompanying workbook called "Data Management - Tableau Cloud Content v1.2.twb" in the output folder that provides a template for how these tables can be related to generate a data source with the upstream and downstream assets:
![image](https://user-images.githubusercontent.com/11485060/207292672-a2ad264c-b941-4720-b746-46dfd91bb6fc.png)

The workbook contains 3 dashboards:
1. Tableau Data Management Cockpit - provides an overview of utilisation across each site including top projects/publishers, # workbooks over time, popular data sources and databases:
![image](https://user-images.githubusercontent.com/11485060/207293002-00e5f8fd-0cb1-4a5f-be33-92feba74f757.png)
2. Tableau Data Management databases - provides an overview of how databases and database types are being utilised across each site:
![image](https://user-images.githubusercontent.com/11485060/207293277-d48925e2-8e82-4329-912f-b70123f8befd.png)
3. Tableau Data Management Impact Analysis - provides information on external assets and tableau assets, allowing users to identify downstream impact:
![image](https://user-images.githubusercontent.com/11485060/207293725-e7cdd067-04f3-406a-ac58-516ca344e6fe.png)

# Instructions
