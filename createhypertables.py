from tableauhyperapi import TableDefinition, TableName, SqlType


# Colors used in console prints
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[42m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CONSOLE_SPACER = '  '


def create_tables(hyper_connection, schema, mode):
    # It is important to match the order of the table definitions with the data tables returned
    # in get_data()

    # Create the table definitions
    sites = TableDefinition(
        table_name=TableName(schema, 'Sites'),
        columns=[
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Luid', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Site URI', SqlType.text())
        ]
    )

    databases = TableDefinition(
        table_name=TableName(schema, "Databases"),
        columns=[
            TableDefinition.Column('Database ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Database Luid', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Database Name', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Database Type', SqlType.text()),
            TableDefinition.Column('Connection Type', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Grouped', SqlType.bool()),
            TableDefinition.Column('Controlled Permissions Enabled', SqlType.bool()),
            TableDefinition.Column('Active Warning', SqlType.bool()),
            TableDefinition.Column('Contact ID', SqlType.text()),
            TableDefinition.Column('Contact Name', SqlType.text()),
            TableDefinition.Column('Contact Username', SqlType.text()),
            TableDefinition.Column('Contact Email', SqlType.text()),
            TableDefinition.Column('Host Name', SqlType.text()),
            TableDefinition.Column('Port', SqlType.int()),
            TableDefinition.Column('Extended Connection Type', SqlType.text()),
            TableDefinition.Column('Service', SqlType.text()),
            TableDefinition.Column('File Path', SqlType.text()),
            TableDefinition.Column('Provider', SqlType.text()),
            TableDefinition.Column('File ID', SqlType.text()),
            TableDefinition.Column('File Extension', SqlType.text()),
            TableDefinition.Column('Mime Type', SqlType.text()),
            TableDefinition.Column('Request URL', SqlType.text()),
            TableDefinition.Column('WDC Embedded', SqlType.bool()),
            TableDefinition.Column('Connector URL', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Contact', SqlType.bool())
        ]
    )

    database_assets = TableDefinition(
        table_name=TableName(schema, 'Database Assets'),
        columns=[
            TableDefinition.Column('Database ID', SqlType.text()),
            TableDefinition.Column('Database Name', SqlType.text()),
            TableDefinition.Column('Database Type', SqlType.text()),
            TableDefinition.Column('Database Connection Type', SqlType.text()),
            TableDefinition.Column('Database Certified', SqlType.bool()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Asset ID', SqlType.text()),
            TableDefinition.Column('Asset Name', SqlType.text()),
            TableDefinition.Column('Asset Type', SqlType.text()),
            TableDefinition.Column('Asset Certified', SqlType.bool()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Database Owner ID', SqlType.text()),
            TableDefinition.Column('Database Owner Name', SqlType.text()),
            TableDefinition.Column('Database Owner Username', SqlType.text()),
            TableDefinition.Column('Database Owner Email', SqlType.text())
        ]
    )

    tables = TableDefinition(
        table_name=TableName(schema, "Tables"),
        columns=[
            TableDefinition.Column('Table ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Table Name', SqlType.text()),
            TableDefinition.Column('Table Type', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Embedded', SqlType.bool()),
            TableDefinition.Column('Table Luid', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Schema', SqlType.text()),
            TableDefinition.Column('Full Name', SqlType.text()),
            TableDefinition.Column('Connection Type', SqlType.text()),
            TableDefinition.Column('Contact ID', SqlType.text()),
            TableDefinition.Column('Contact Name', SqlType.text()),
            TableDefinition.Column('Contact Username', SqlType.text()),
            TableDefinition.Column('Contact Email', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Database ID', SqlType.text()),
            TableDefinition.Column('Active Warning', SqlType.bool()),
            TableDefinition.Column('Query', SqlType.text()),
            TableDefinition.Column('Unsupported Custom SQL', SqlType.bool()),
            TableDefinition.Column('Extracted', SqlType.bool()),
            TableDefinition.Column('Virtual Connection ID', SqlType.text()),
            TableDefinition.Column('Extract Last Refresh Datetime', SqlType.timestamp()),
            TableDefinition.Column('Extract Last Refresh Type', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Contact', SqlType.bool())
        ]
    )

    columns = TableDefinition(
        table_name=TableName(schema, "Columns"),
        columns=[
            TableDefinition.Column('Column ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Column Luid', SqlType.text()),
            TableDefinition.Column('Column Name', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Inherited Description', SqlType.text()),
            TableDefinition.Column('Remote Type', SqlType.text()),
            TableDefinition.Column('Nullable', SqlType.bool()),
            TableDefinition.Column('Table ID', SqlType.text()),
            TableDefinition.Column('Database ID', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    column_assets = TableDefinition(
        table_name=TableName(schema, 'Column Assets'),
        columns=[
            TableDefinition.Column('Column ID', SqlType.text()),
            TableDefinition.Column('Column Name', SqlType.text()),
            TableDefinition.Column('Remote Type', SqlType.text()),
            TableDefinition.Column('Table ID', SqlType.text()),
            TableDefinition.Column('Table Name', SqlType.text()),
            TableDefinition.Column('Table Type', SqlType.text()),
            TableDefinition.Column('Certified Table ID', SqlType.text()),
            TableDefinition.Column('Certified Table', SqlType.bool()),
            TableDefinition.Column('Database ID', SqlType.text()),
            TableDefinition.Column('Database Name', SqlType.text()),
            TableDefinition.Column('Database Type', SqlType.text()),
            TableDefinition.Column('Database Connection Type', SqlType.text()),
            TableDefinition.Column('Certified Database ID', SqlType.text()),
            TableDefinition.Column('Certified Database', SqlType.bool()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Has Assets', SqlType.bool()),
            TableDefinition.Column('Asset ID', SqlType.text()),
            TableDefinition.Column('Asset Name', SqlType.text()),
            TableDefinition.Column('Asset Type', SqlType.text()),
            TableDefinition.Column('Project Name', SqlType.text())
        ]
    )

    fields = TableDefinition(
        table_name=TableName(schema, "Fields"),
        columns=[
            TableDefinition.Column('Field ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Field Name', SqlType.text()),
            TableDefinition.Column('Fully Qualified Name', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Inherited Description', SqlType.text()),
            TableDefinition.Column('Hidden', SqlType.bool()),
            TableDefinition.Column('Folder Name', SqlType.text()),
            TableDefinition.Column('Field Type', SqlType.text()),
            TableDefinition.Column('DataSource ID', SqlType.text()),
            TableDefinition.Column('Bin Size', SqlType.text()),
            TableDefinition.Column('Data Type', SqlType.text()),
            TableDefinition.Column('Data Category', SqlType.text()),
            TableDefinition.Column('Role', SqlType.text()),
            TableDefinition.Column('Formula', SqlType.text()),
            TableDefinition.Column('Default Format', SqlType.text()),
            TableDefinition.Column('Semantic Role', SqlType.text()),
            TableDefinition.Column('Aggregation', SqlType.text()),
            TableDefinition.Column('Aggregation Parameter', SqlType.text()),
            TableDefinition.Column('Auto Generated', SqlType.bool()),
            TableDefinition.Column('User Reference', SqlType.bool()),
            TableDefinition.Column('Column ID', SqlType.text()),
            TableDefinition.Column('Remote Field ID', SqlType.text()),
            TableDefinition.Column('Delimiter', SqlType.text()),
            TableDefinition.Column('Combination Type', SqlType.text()),
            TableDefinition.Column('Has Other', SqlType.bool()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    field_assets = TableDefinition(
        table_name=TableName(schema, "Field Assets"),
        columns=[
            TableDefinition.Column('Field ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Field Name', SqlType.text()),
            TableDefinition.Column('Fully Qualified Name', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Inherited Description', SqlType.text()),
            TableDefinition.Column('Field Type', SqlType.text()),
            TableDefinition.Column('DataSource ID', SqlType.text()),
            TableDefinition.Column('DataSource Name', SqlType.text()),
            TableDefinition.Column('DataSource Type', SqlType.text()),
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Workbook Name', SqlType.text()),
            TableDefinition.Column('Sheet ID', SqlType.text()),
            TableDefinition.Column('Sheet Name', SqlType.text()),
            TableDefinition.Column('Dashboard ID', SqlType.text()),
            TableDefinition.Column('Dashboard Name', SqlType.text()),
            TableDefinition.Column('Data Type', SqlType.text()),
            TableDefinition.Column('Column ID', SqlType.text())
        ]
    )

    virtual_connections = TableDefinition(
        table_name=TableName(schema, "Virtual Connections"),
        columns=[
            TableDefinition.Column('Virtual Connection ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Virtual Connection Name', SqlType.text()),
            TableDefinition.Column('Virtual Connection Type', SqlType.text()),
            TableDefinition.Column('Virtual Connection Luid', SqlType.text()),
            TableDefinition.Column('Virtual Connection URI', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Active Warnings', SqlType.bool()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project Vizportal URL ID', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Database Connection Type', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Viz Portal URL ID', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    datasources = TableDefinition(
        table_name=TableName(schema, "Datasources"),
        columns=[
            TableDefinition.Column('Datasource ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Datasource Name', SqlType.text()),
            TableDefinition.Column('Datasource Type', SqlType.text()),
            TableDefinition.Column('Contains Unsupported Custom SQL', SqlType.bool()),
            TableDefinition.Column('User Reference', SqlType.bool()),
            TableDefinition.Column('Extracts', SqlType.bool()),
            TableDefinition.Column('Extract Last Refresh Datetime', SqlType.timestamp()),
            TableDefinition.Column('Extract Last Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Extract Last Incremental Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Datasource Luid', SqlType.text()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project Vizportal URL ID', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Quality Warning', SqlType.bool()),
            TableDefinition.Column('Datasource URI', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Viz Portal URL ID', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    workbooks = TableDefinition(
        table_name=TableName(schema, 'Workbooks'),
        columns=[
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Workbook Luid', SqlType.text()),
            TableDefinition.Column('Workbook Name', SqlType.text()),
            TableDefinition.Column('Contains Unsupported Custom SQL', SqlType.bool()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Updated Datetime', SqlType.timestamp()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project ID', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Workbook URI', SqlType.text()),
            TableDefinition.Column('Viz Portal URL ID', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    datasource_workbooks = TableDefinition(
        table_name=TableName(schema, 'Datasource Workbooks'),
        columns=[
            TableDefinition.Column('Datasource ID', SqlType.text()),
            TableDefinition.Column('Datasource Name', SqlType.text()),
            TableDefinition.Column('Datasource Type', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Workbook Name', SqlType.text()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    dashboards = TableDefinition(
        table_name=TableName(schema, 'Dashboards'),
        columns=[
            TableDefinition.Column('Dashboard ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Dashboard Luid', SqlType.text()),
            TableDefinition.Column('Dashboard Name', SqlType.text()),
            TableDefinition.Column('Path', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Index', SqlType.int()),
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Workbook Luid', SqlType.text()),
            TableDefinition.Column('Workbook Owner ID', SqlType.text()),
            TableDefinition.Column('Workbook Owner Luid', SqlType.text()),
            TableDefinition.Column('Workbook Owner Name', SqlType.text()),
            TableDefinition.Column('Workbook Owner Username', SqlType.text()),
            TableDefinition.Column('Workbook Owner Email', SqlType.text()),
            TableDefinition.Column('View Type', SqlType.text()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    sheets = TableDefinition(
        table_name=TableName(schema, 'Sheets'),
        columns=[
            TableDefinition.Column('Sheet ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Sheet Luid', SqlType.text()),
            TableDefinition.Column('Sheet Name', SqlType.text()),
            TableDefinition.Column('Path', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Index', SqlType.int()),
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Workbook Luid', SqlType.text()),
            TableDefinition.Column('Workbook Owner ID', SqlType.text()),
            TableDefinition.Column('Workbook Owner Luid', SqlType.text()),
            TableDefinition.Column('Workbook Owner Name', SqlType.text()),
            TableDefinition.Column('Workbook Owner Username', SqlType.text()),
            TableDefinition.Column('Workbook Owner Email', SqlType.text()),
            TableDefinition.Column('View Type', SqlType.text()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    views = TableDefinition(
        table_name=TableName(schema, 'Views'),
        columns=[
            TableDefinition.Column('View ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('View Luid', SqlType.text()),
            TableDefinition.Column('View Name', SqlType.text()),
            TableDefinition.Column('Path', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Index', SqlType.int()),
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Workbook Luid', SqlType.text()),
            TableDefinition.Column('Workbook Owner ID', SqlType.text()),
            TableDefinition.Column('Workbook Owner Luid', SqlType.text()),
            TableDefinition.Column('Workbook Owner Name', SqlType.text()),
            TableDefinition.Column('Workbook Owner Username', SqlType.text()),
            TableDefinition.Column('Workbook Owner Email', SqlType.text()),
            TableDefinition.Column('View Type', SqlType.text()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    sheet_fields = TableDefinition(
        table_name=TableName(schema, 'Sheet Fields'),
        columns=[
            TableDefinition.Column('Sheet ID', SqlType.text()),
            TableDefinition.Column('Field ID', SqlType.text())
        ]
    )

    dashboard_sheets = TableDefinition(
        table_name=TableName(schema, 'Dashboard Sheets'),
        columns=[
            TableDefinition.Column('Dashboard ID', SqlType.text()),
            TableDefinition.Column('Sheet ID', SqlType.text())
        ]
    )

    referenced_fields = TableDefinition(
        table_name=TableName(schema, "Fields Referenced"),
        columns=[
            TableDefinition.Column('Field ID', SqlType.text()),
            TableDefinition.Column('Used Fields ID', SqlType.text())
        ]
    )

    metrics = TableDefinition(
        table_name=TableName(schema, "Metrics"),
        columns=[
            TableDefinition.Column('Metric ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Metric Luid', SqlType.text()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Underlying View ID', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Metric Name', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    content_owners = TableDefinition(
        table_name=TableName(schema, "Content Owners"),
        columns=[
            TableDefinition.Column('Content Owner ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Content Owner Luid', SqlType.text()),
            TableDefinition.Column('Name', SqlType.text()),
            TableDefinition.Column('Username', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('User URI', SqlType.text()),
            TableDefinition.Column('Domain', SqlType.text()),
            TableDefinition.Column('Email', SqlType.text())
        ]
    )

    owner_assets = TableDefinition(
        table_name=TableName(schema, "Asset Ownership"),
        columns=[
            TableDefinition.Column('Content Owner ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Name', SqlType.text()),
            TableDefinition.Column('Username', SqlType.text()),
            TableDefinition.Column('Email', SqlType.text()),
            TableDefinition.Column('Domain', SqlType.text()),
            TableDefinition.Column('Asset ID', SqlType.text()),
            TableDefinition.Column('Asset Name', SqlType.text()),
            TableDefinition.Column('Asset Type', SqlType.text()),
            TableDefinition.Column('Asset Subtype', SqlType.text()),
            TableDefinition.Column('Asset Connection Type', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('DQW Type', SqlType.text()),
            TableDefinition.Column('DQW Asset ID', SqlType.text()),
            TableDefinition.Column('DQW Asset Name', SqlType.text()),
            TableDefinition.Column('DQW Asset Type', SqlType.text()),
            TableDefinition.Column('DQC Asset ID', SqlType.text()),
            TableDefinition.Column('DQC Asset Name', SqlType.text()),
            TableDefinition.Column('DQC Asset Type', SqlType.text())
        ]
    )

    flows = TableDefinition(
        table_name=TableName(schema, "Flows"),
        columns=[
            TableDefinition.Column('Flow ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Flow Luid', SqlType.text()),
            TableDefinition.Column('Flow Name', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('URI', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Active Warning', SqlType.bool()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Personal Space URL Link', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Contains Unsupported Custom SQL', SqlType.bool()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Has Description', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool())
        ]
    )

    dqws = TableDefinition(
        table_name=TableName(schema, "Data Quality Warnings"),
        columns=[
            TableDefinition.Column('DQW ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('DQW Luid', SqlType.text()),
            TableDefinition.Column('Author ID', SqlType.text()),
            TableDefinition.Column('Author Display Name', SqlType.text()),
            TableDefinition.Column('Author Name', SqlType.text()),
            TableDefinition.Column('Author Username', SqlType.text()),
            TableDefinition.Column('Author Email', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Active', SqlType.bool()),
            TableDefinition.Column('Severe', SqlType.bool()),
            TableDefinition.Column('Warning Type', SqlType.text()),
            TableDefinition.Column('Message', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Asset ID', SqlType.text())
        ]
    )

    dqcs = TableDefinition(
        table_name=TableName(schema, "Data Quality Certifications"),
        columns=[
            TableDefinition.Column('DQC ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('DQC Luid', SqlType.text()),
            TableDefinition.Column('Author ID', SqlType.text()),
            TableDefinition.Column('Author Display Name', SqlType.text()),
            TableDefinition.Column('Author Name', SqlType.text()),
            TableDefinition.Column('Author Username', SqlType.text()),
            TableDefinition.Column('Author Email', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Active', SqlType.bool()),
            TableDefinition.Column('Message', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Asset ID', SqlType.text())
        ]
    )

    groups = TableDefinition(
        table_name=TableName(schema, 'Groups'),
        columns=[
            TableDefinition.Column('Group ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Domain Name', SqlType.text()),
            TableDefinition.Column('Group Name', SqlType.text()),
            TableDefinition.Column('Minimum Site Role', SqlType.text()),
            TableDefinition.Column('License Mode', SqlType.text())
        ]
    )

    users = TableDefinition(
        table_name=TableName(schema, 'Users'),
        columns=[
            TableDefinition.Column('User ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Name', SqlType.text()),
            TableDefinition.Column('Full Name', SqlType.text()),
            TableDefinition.Column('Email', SqlType.text()),
            TableDefinition.Column('Domain Name', SqlType.text()),
            TableDefinition.Column('Site Role', SqlType.text()),
            TableDefinition.Column('External Auth User ID', SqlType.text()),
            TableDefinition.Column('Auth Setting', SqlType.text()),
            TableDefinition.Column('Last Login Datetime', SqlType.timestamp())
        ]
    )

    group_users = TableDefinition(
        table_name=TableName(schema, 'Group Users'),
        columns=[
            TableDefinition.Column('Group ID', SqlType.text()),
            TableDefinition.Column('User ID', SqlType.text())
        ]
    )

    projects = TableDefinition(
        table_name=TableName(schema, 'Projects'),
        columns=[
            TableDefinition.Column('Project ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Content Permission', SqlType.text()),
            TableDefinition.Column('Parent Project ID', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    parameters = TableDefinition(
        table_name=TableName(schema, "Parameters"),
        columns=[
            TableDefinition.Column('Parameter ID', SqlType.text()),
            TableDefinition.Column('Parameter Name', SqlType.text()),
            TableDefinition.Column('Parent Name', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Workbook ID', SqlType.text()),
            TableDefinition.Column('Datasource ID', SqlType.text())
        ]
    )

    parameter_references = TableDefinition(
        table_name=TableName(schema, "Parameter References"),
        columns=[
            TableDefinition.Column('Parameter ID', SqlType.text()),
            TableDefinition.Column('Field ID', SqlType.text()),
            TableDefinition.Column('Field Type', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text())
        ]
    )

    tags = TableDefinition(
        table_name=TableName(schema, "Tags"),
        columns=[
            TableDefinition.Column('Tag ID', SqlType.text()),
            TableDefinition.Column('Tag Name', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text())
        ]
    )

    tag_assets = TableDefinition(
        table_name=TableName(schema, "Tag Assets"),
        columns=[
            TableDefinition.Column('Asset ID', SqlType.text()),
            TableDefinition.Column('Tag ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text())
        ]
    )

    lenses = TableDefinition(
        table_name=TableName(schema, "Lenses"),
        columns=[
            TableDefinition.Column('Lens ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Lens Luid', SqlType.text()),
            TableDefinition.Column('Lens Name', SqlType.text()),
            TableDefinition.Column('Project Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Viz Portal ID', SqlType.text()),
            TableDefinition.Column('Datasource ID', SqlType.text()),
            TableDefinition.Column('Datasource Name', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Luid', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner URI', SqlType.text()),
            TableDefinition.Column('Owner Domain', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Has Owner', SqlType.bool()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    lens_fields = TableDefinition(
        table_name=TableName(schema, "Lens Fields"),
        columns=[
            TableDefinition.Column('Lens Field ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Lens Field Name', SqlType.text()),
            TableDefinition.Column('Lens Field Description', SqlType.text()),
            TableDefinition.Column('Datasource Field ID', SqlType.text()),
            TableDefinition.Column('Datasource Field Name', SqlType.text()),
            TableDefinition.Column('Datasource Field Type', SqlType.text()),
            TableDefinition.Column('Lens ID', SqlType.text()),
            TableDefinition.Column('Lens Luid', SqlType.text()),
            TableDefinition.Column('Lens Name', SqlType.text()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    ask_data_extensions = TableDefinition(
        table_name=TableName(schema, "Ask Data Extensions"),
        columns=[
            TableDefinition.Column('Ask Data Extension ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Lens ID', SqlType.text()),
            TableDefinition.Column('Lens Name', SqlType.text()),
            TableDefinition.Column('Lens Luid', SqlType.text()),
            TableDefinition.Column('Database ID', SqlType.text()),
            TableDefinition.Column('Database Name', SqlType.text()),
            TableDefinition.Column('Database Luid', SqlType.text())
        ]
    )

    owned_assets = TableDefinition(
        table_name=TableName(schema, 'Owned Assets'),
        columns=[
            TableDefinition.Column('Asset ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Asset Luid', SqlType.text()),
            TableDefinition.Column('Asset Name', SqlType.text()),
            TableDefinition.Column('Asset Type', SqlType.text()),
            TableDefinition.Column('Asset URI', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project ID', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Luid', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner URI', SqlType.text()),
            TableDefinition.Column('Owner Domain', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    all_assets = TableDefinition(
        table_name=TableName(schema, 'All Assets'),
        columns=[
            TableDefinition.Column('Asset ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('Asset Luid', SqlType.text()),
            TableDefinition.Column('Asset Name', SqlType.text()),
            TableDefinition.Column('Asset Type', SqlType.text()),
            TableDefinition.Column('Asset URI', SqlType.text()),
            TableDefinition.Column('Create Datetime', SqlType.timestamp()),
            TableDefinition.Column('Update Datetime', SqlType.timestamp()),
            TableDefinition.Column('Project Name', SqlType.text()),
            TableDefinition.Column('Project ID', SqlType.text()),
            TableDefinition.Column('Container Type', SqlType.text()),
            TableDefinition.Column('Container Name', SqlType.text()),
            TableDefinition.Column('Ownable', SqlType.bool()),
            TableDefinition.Column('Owner ID', SqlType.text()),
            TableDefinition.Column('Owner Luid', SqlType.text()),
            TableDefinition.Column('Owner Name', SqlType.text()),
            TableDefinition.Column('Owner Username', SqlType.text()),
            TableDefinition.Column('Owner URI', SqlType.text()),
            TableDefinition.Column('Owner Domain', SqlType.text()),
            TableDefinition.Column('Owner Email', SqlType.text()),
            TableDefinition.Column('Description', SqlType.text()),
            TableDefinition.Column('Certified', SqlType.bool()),
            TableDefinition.Column('Has Owner', SqlType.bool()),
            TableDefinition.Column('Has Description', SqlType.bool())
        ]
    )

    datasource_filters = TableDefinition(
        table_name=TableName(schema, "Datasource Filters"),
        columns=[
            TableDefinition.Column('Datasource Filter ID', SqlType.text()),
            TableDefinition.Column('Site ID', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('DSF Field ID', SqlType.text()),
            TableDefinition.Column('Field Name', SqlType.text()),
            TableDefinition.Column('Field Type', SqlType.text()),
            TableDefinition.Column('Has User Reference', SqlType.bool()),
            TableDefinition.Column('Formula', SqlType.text()),
            TableDefinition.Column('DSF Datasource ID', SqlType.text()),
            TableDefinition.Column('Datasource Name', SqlType.text()),
            TableDefinition.Column('Datasource LUID', SqlType.text())
        ]
    )

    view_stats = TableDefinition(
        table_name=TableName(schema, "View Stats"),
        columns=[
            TableDefinition.Column('View Stat ID', SqlType.int()),
            TableDefinition.Column('Number of Views', SqlType.int()),
            TableDefinition.Column('View Date', SqlType.timestamp()),
            TableDefinition.Column('Device Type', SqlType.text()),
            TableDefinition.Column('View Luid', SqlType.text()),
            TableDefinition.Column('View Name', SqlType.text()),
            TableDefinition.Column('Site Luid', SqlType.text()),
            TableDefinition.Column('Site Name', SqlType.text()),
            TableDefinition.Column('User Luid', SqlType.text())
        ]
    )

    hist_events = TableDefinition(
        table_name=TableName(schema, "Historic Events"),
        columns=[
            TableDefinition.Column('Hist Event ID', SqlType.int()),
            TableDefinition.Column('Create Date', SqlType.timestamp()),
            TableDefinition.Column('Details', SqlType.text()),
            TableDefinition.Column('Event Duration', SqlType.int()),
            TableDefinition.Column('Worker', SqlType.text()),
            TableDefinition.Column('Is Failure', SqlType.bool()),
            TableDefinition.Column('Hist Event Type ID', SqlType.int()),
            TableDefinition.Column('Hist Event Action Type', SqlType.text()),
            TableDefinition.Column('Hist Event Action Name', SqlType.text()),
            TableDefinition.Column('Hist View ID', SqlType.int()),
            TableDefinition.Column('Hist View Name', SqlType.text()),
            TableDefinition.Column('Hist View Luid', SqlType.text()),
            TableDefinition.Column('Hist Project ID', SqlType.int()),
            TableDefinition.Column('Hist Project Name', SqlType.text()),
            TableDefinition.Column('Hist Project Luid', SqlType.text()),
            TableDefinition.Column('Hist Workbook ID', SqlType.int()),
            TableDefinition.Column('Hist Workbook Name', SqlType.text()),
            TableDefinition.Column('Hist Workbook Luid', SqlType.text()),
            TableDefinition.Column('Hist Actor Site ID', SqlType.int()),
            TableDefinition.Column('Hist Actor Site Name', SqlType.text()),
            TableDefinition.Column('Hist Actor Site Luid', SqlType.text()),
            TableDefinition.Column('Hist Actor User ID', SqlType.int()),
            TableDefinition.Column('Hist Actor User Luid', SqlType.text()),
            TableDefinition.Column('Hist Database ID', SqlType.int()),
            TableDefinition.Column('Hist Database Name', SqlType.text()),
            TableDefinition.Column('Hist Database Luid', SqlType.text()),
            TableDefinition.Column('Hist Datasource ID', SqlType.int()),
            TableDefinition.Column('Hist Datasource Name', SqlType.text()),
            TableDefinition.Column('Hist Datasource Luid', SqlType.text()),
            TableDefinition.Column('Hist Flow ID', SqlType.int()),
            TableDefinition.Column('Hist Flow Name', SqlType.text()),
            TableDefinition.Column('Hist Flow Luid', SqlType.text()),
            TableDefinition.Column('Hist Metric ID', SqlType.int()),
            TableDefinition.Column('Hist Metric Name', SqlType.text()),
            TableDefinition.Column('Hist Metric Luid', SqlType.text()),
            TableDefinition.Column('Hist Table ID', SqlType.int()),
            TableDefinition.Column('Hist Table Name', SqlType.text()),
            TableDefinition.Column('Hist Table Luid', SqlType.text()),
            TableDefinition.Column('Hist Column ID', SqlType.int()),
            TableDefinition.Column('Hist Column Name', SqlType.text()),
            TableDefinition.Column('Hist Column Luid', SqlType.text()),
            TableDefinition.Column('Hist Comment ID', SqlType.int()),
            TableDefinition.Column('Hist Tag ID', SqlType.int()),
            TableDefinition.Column('Hist Target Site ID', SqlType.int()),
            TableDefinition.Column('Hist Target Site Name', SqlType.text()),
            TableDefinition.Column('Hist Target Site Luid', SqlType.text()),
            TableDefinition.Column('Hist Target User ID', SqlType.int()),
            TableDefinition.Column('Hist Capability ID', SqlType.int()),
            TableDefinition.Column('Hist Collection ID', SqlType.int()),
            TableDefinition.Column('Hist Config ID', SqlType.int()),
            TableDefinition.Column('Hist Data Connection ID', SqlType.int()),
            TableDefinition.Column('Hist Data Quality Indicator ID', SqlType.int()),
            TableDefinition.Column('Hist Data Role ID', SqlType.int()),
            TableDefinition.Column('Hist Flow Draft ID', SqlType.int()),
            TableDefinition.Column('Hist Group ID', SqlType.int()),
            TableDefinition.Column('Hist Licensing Role ID', SqlType.int()),
            TableDefinition.Column('Hist Published Connection ID', SqlType.int()),
            TableDefinition.Column('Hist Remote Agent ID', SqlType.int()),
            TableDefinition.Column('Hist Schedule ID', SqlType.int()),
            TableDefinition.Column('Hist Task ID', SqlType.int()),
            TableDefinition.Column('Hist Collection Luid', SqlType.text()),
            TableDefinition.Column('Hist Collection Name', SqlType.text())
        ]
    )

    if mode == "catalog":
        table_definitions_dict = {'Sites': sites, 'Workbooks': workbooks, 'Dashboards': dashboards, 'Sheets': sheets,
                                  'Sheet Fields': sheet_fields, 'Dashboard Sheets': dashboard_sheets, 'Fields': fields,
                                  'Field Assets': field_assets, 'Referenced Fields': referenced_fields,
                                  'Virtual Connections': virtual_connections, 'Datasources': datasources,
                                  'Datasource Workbooks': datasource_workbooks, 'Columns': columns, 'Column Assets':
                                  column_assets, 'Tables': tables, 'Databases': databases, 'Database Assets':
                                  database_assets, 'Views': views, 'Content Owners': content_owners, 'Owner Assets':
                                  owner_assets, 'Metrics': metrics, 'Flows': flows, 'Data Quality Warnings': dqws,
                                  'Data Quality Certifications': dqcs, 'Groups': groups, 'Users': users, 'Group Users':
                                  group_users, 'Projects': projects, 'Parameters': parameters, 'Parameter References':
                                  parameter_references, 'Tags': tags, 'Tag Assets': tag_assets, 'Lenses': lenses,
                                  'Owned Assets': owned_assets, 'All Assets': all_assets, 'Lens Fields': lens_fields,
                                  'Ask Data Extensions': ask_data_extensions, 'Datasource Filters': datasource_filters}
    elif mode == "repo":
        table_definitions_dict = {'View Stats': view_stats, 'Historic Events': hist_events}

    else:
        table_definitions_dict = {'Sites': sites, 'Workbooks': workbooks, 'Dashboards': dashboards, 'Sheets': sheets,
                                  'Sheet Fields': sheet_fields, 'Dashboard Sheets': dashboard_sheets, 'Fields': fields,
                                  'Field Assets': field_assets, 'Referenced Fields': referenced_fields,
                                  'Virtual Connections': virtual_connections, 'Datasources': datasources,
                                  'Datasource Workbooks': datasource_workbooks, 'Columns': columns,
                                  'Column Assets': column_assets,'Tables': tables, 'Databases': databases,
                                  'Database Assets': database_assets, 'Views': views, 'Content Owners': content_owners,
                                  'Owner Assets': owner_assets, 'Metrics': metrics, 'Flows': flows,
                                  'Data Quality Warnings': dqws, 'Data Quality Certifications': dqcs, 'Groups': groups,
                                  'Users': users, 'Group Users': group_users, 'Projects': projects,
                                  'Parameters': parameters, 'Parameter References': parameter_references,
                                  'Tags': tags, 'Tag Assets': tag_assets, 'Lenses': lenses,
                                  'Owned Assets': owned_assets, 'All Assets': all_assets, 'Lens Fields': lens_fields,
                                  'Ask Data Extensions': ask_data_extensions, 'Datasource Filters': datasource_filters,
                                  'View Stats': view_stats, 'Historic Events': hist_events}

    for table_name, table_definition in table_definitions_dict.items():
        print('{0}Creating the {1} table ...{2}'.format(bcolors.OKBLUE, table_definition.table_name, bcolors.ENDC))
        hyper_connection.catalog.create_table(table_definition)

    return table_definitions_dict
