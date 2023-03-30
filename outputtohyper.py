import iso8601

from tableauhyperapi import Inserter


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


def write_catalog_to_hyper(tableau_server, hyper_connection, table_definitions, tables_data):
    # Uses the Hyper API to build and insert data into the Hyper file

    server_name = tableau_server.server_address
    # Holder for Site ID to pass to other assets
    site_id = None
    site_name = None

    # Get Table Definitions
    site_table_def = table_definitions.get('Sites')
    database_table_def = table_definitions.get('Databases')
    database_asset_table_def = table_definitions.get('Database Assets')
    table_table_def = table_definitions.get('Tables')
    column_table_def = table_definitions.get('Columns')
    column_asset_table_def = table_definitions.get('Column Assets')
    field_table_def = table_definitions.get('Fields')
    field_asset_table_def = table_definitions.get('Field Assets')
    reference_field_table_def = table_definitions.get('Referenced Fields')
    virtual_connection_table_def = table_definitions.get('Virtual Connections')
    datasource_table_def = table_definitions.get('Datasources')
    project_table_def = table_definitions.get('Projects')
    workbook_table_def = table_definitions.get('Workbooks')
    dashboard_table_def = table_definitions.get('Dashboards')
    datasource_workbooks_table_def = table_definitions.get('Datasource Workbooks')
    sheet_table_def = table_definitions.get('Sheets')
    view_table_def = table_definitions.get('Views')
    sheet_field_table_def = table_definitions.get('Sheet Fields')
    dashboard_sheet_table_def = table_definitions.get('Dashboard Sheets')
    metric_table_def = table_definitions.get('Metrics')
    owner_table_def = table_definitions.get('Content Owners')
    owner_asset_table_def = table_definitions.get('Owner Assets')
    data_quality_warning_table_def = table_definitions.get('Data Quality Warnings')
    parameter_table_def = table_definitions.get('Parameters')
    parameter_reference_table_def = table_definitions.get('Parameter References')
    data_quality_certification_table_def = table_definitions.get('Data Quality Certifications')
    group_table_def = table_definitions.get('Groups')
    user_table_def = table_definitions.get('Users')
    group_user_table_def = table_definitions.get('Group Users')
    tag_table_def = table_definitions.get('Tags')
    tag_asset_table_def = table_definitions.get('Tag Assets')
    flow_table_def = table_definitions.get('Flows')
    owned_asset_table_def = table_definitions.get('Owned Assets')
    lens_table_def = table_definitions.get('Lenses')
    lens_field_table_def = table_definitions.get('Lens Fields')
    ask_data_extension_table_def = table_definitions.get('Ask Data Extensions')
    datasource_filter_table_def = table_definitions.get('Datasource Filters')

    # Get Table Data
    site_data = tables_data.get('Sites')
    database_data = tables_data.get('Databases')
    table_data = tables_data.get('Tables')
    column_data = tables_data.get('Columns')
    field_data = tables_data.get('Fields')
    virtual_connection_data = tables_data.get('Virtual Connections')
    datasource_data = tables_data.get('Datasources')
    project_data = tables_data.get('Projects')
    workbook_data = tables_data.get('Workbooks')
    view_data = tables_data.get('Views')
    metric_data = tables_data.get('Metrics')
    owner_data = tables_data.get('Content Owners')
    data_quality_warning_data = tables_data.get('Data Quality Warnings')
    parameter_data = tables_data.get('Parameters')
    data_quality_certification_data = tables_data.get('Data Quality Certifications')
    group_data = tables_data.get('Groups')
    user_data = tables_data.get('Users')
    tag_data = tables_data.get('Tags')
    flow_data = tables_data.get('Flows')
    lens_data = tables_data.get('Lenses')
    lens_field_data = tables_data.get('Lens Fields')
    ask_data_extension_data = tables_data.get('Ask Data Extensions')
    datasource_filter_data = tables_data.get('Datasource Filters')

    # Insert into Site tables
    if site_data is not None:
        site_id, site_name = insert_into_site_tables(hyper_connection, site_data, site_table_def)

    # Insert into one or more Database related tables
    if database_data is not None:
        insert_into_database_tables(hyper_connection, site_id, site_name, database_data, database_table_def,
                                    database_asset_table_def)

    # Insert into one or more Table related tables
    if table_data is not None:
        insert_into_table_tables(hyper_connection, site_id, site_name, table_data, table_table_def)

    # Insert into one or more Column related tables
    if column_data is not None:
        insert_into_column_tables(hyper_connection, site_id, site_name, column_data, column_table_def,
                                  column_asset_table_def)

    # Insert into one or more Field related tables
    if field_data is not None:
        insert_into_field_tables(hyper_connection, site_id, site_name, field_data, field_table_def,
                                 reference_field_table_def, field_asset_table_def)

    if virtual_connection_data is not None:
        insert_into_virtual_connection_tables(hyper_connection, site_id, site_name, virtual_connection_data,
                                              virtual_connection_table_def)
        insert_into_asset_tables(hyper_connection, server_name, site_id, site_name, virtual_connection_data,
                                 owned_asset_table_def)

    # Insert into one or more Datasource related tables
    if datasource_data is not None:
        insert_into_datasource_tables(hyper_connection, site_id, site_name, datasource_data, datasource_table_def,
                                      datasource_workbooks_table_def)
        insert_into_asset_tables(hyper_connection, server_name, site_id, site_name, datasource_data,
                                 owned_asset_table_def)

    # Insert into one or more Project related tables
    if project_data is not None:
        insert_into_project_tables(hyper_connection, site_id, site_name, project_data, project_table_def)

    # Insert into one or more Workbook related tables
    if workbook_data is not None:
        insert_into_workbook_tables(hyper_connection, site_id, site_name, workbook_data, workbook_table_def)
        insert_into_asset_tables(hyper_connection, server_name, site_id, site_name, workbook_data,
                                 owned_asset_table_def)

    # Insert into one or more Dashboard and Sheet related tables
    if view_data is not None:
        insert_into_view_tables(hyper_connection, site_id, site_name, view_data, dashboard_table_def, sheet_table_def,
                                sheet_field_table_def, dashboard_sheet_table_def, view_table_def)

    # Insert into one or more Metric related tables
    if metric_data is not None:
        insert_into_metric_tables(hyper_connection, site_id, site_name, metric_data, metric_table_def)
        insert_into_asset_tables(hyper_connection, server_name, site_id, site_name, metric_data, owned_asset_table_def)

    # Insert into one or more User related tables
    if owner_data is not None:
        insert_into_owner_tables(hyper_connection, site_id, site_name, owner_data, owner_table_def,
                                 owner_asset_table_def)

    # Insert into one or more Data Quality related tables
    if data_quality_warning_data is not None:
        insert_into_dqw_tables(hyper_connection, site_id, site_name, data_quality_warning_data,
                               data_quality_warning_table_def)

    # Insert into one or more Parameter related tables
    if parameter_data is not None:
        insert_into_parameter_tables(hyper_connection, site_id, site_name, parameter_data, parameter_table_def,
                                     parameter_reference_table_def)

    # Insert into one or more Data Quality Certification related tables
    if data_quality_certification_data is not None:
        insert_into_dqc_tables(hyper_connection, site_id, site_name, data_quality_certification_data,
                               data_quality_certification_table_def)

    # Insert into one or more User related tables
    if user_data is not None:
        insert_into_user_tables(hyper_connection, site_id, site_name, user_data, user_table_def)

    # Insert into one or more Group related tables
    if group_data is not None:
        insert_into_group_tables(tableau_server, hyper_connection, site_id, site_name, group_data, group_table_def,
                                 group_user_table_def)

    # Insert into one or more Parameter related tables
    if tag_data is not None:
        insert_into_tag_tables(hyper_connection, site_id, site_name, tag_data, tag_table_def, tag_asset_table_def)

    # Insert into one or more Flow related tables
    if flow_data is not None:
        insert_into_flow_tables(hyper_connection, site_id, site_name, flow_data, flow_table_def)
        insert_into_asset_tables(hyper_connection, server_name, site_id, site_name, flow_data, owned_asset_table_def)

    # Insert into one or more Lenses related tables
    if lens_data is not None:
        insert_into_lens_tables(hyper_connection, site_id, site_name, lens_data, lens_table_def)
        insert_into_asset_tables(hyper_connection, server_name, site_id, site_name, lens_data, owned_asset_table_def)

    # Insert into one or more Lens Fields related tables
    if lens_field_data is not None:
        insert_into_lens_field_tables(hyper_connection, site_id, site_name, lens_field_data, lens_field_table_def)

    # Insert into one or more Ask Data Extensions related tables
    if ask_data_extension_data is not None:
        insert_into_ask_data_extension_tables(hyper_connection, site_id, site_name, ask_data_extension_data,
                                              ask_data_extension_table_def)

    # Insert into one or more Datasource Filters related tables
    if datasource_filter_data is not None:
        insert_into_datasource_filter_tables(hyper_connection, site_id, site_name, datasource_filter_data,
                                             datasource_filter_table_def)


def insert_into_site_tables(hyper_connection, site_data_df, site_table_definition):
    # Create list to hold data rows
    site_rows = []
    site_id = None
    site_name = None
    # Get all data to insert into Hyper. There should only be one site here.
    for row in site_data_df:
        asset_id = row.get('id')
        luid = row.get('luid')
        name = row.get('name')
        uri = row.get('uri')

        row_to_add = [asset_id, luid, name, uri]
        site_rows.append(row_to_add)
        site_id = asset_id
        site_name = name

    update_hyper(hyper_connection, site_rows, site_table_definition)

    return site_id, site_name


def insert_into_database_tables(hyper_connection, site_id, site_name, database_data, database_table_definition,
                                database_asset_table_definition):
    database_rows = []
    database_asset_rows = []

    for row in database_data:
        asset_id = row.get('id')
        luid = row.get('luid')
        viz_portal_id = row.get('vizportalId')
        name = row.get('name')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        type_name = row.get('__typename')
        connection_type = row.get('connectionType')
        certified = row.get('isCertified')
        grouped = row.get('isGrouped')
        controlled_permissions_enabled = row.get('isControlledPermissionsEnabled')
        has_active_warning = row.get('hasActiveWarning')
        has_contact = False
        if row['contact']:
            has_contact = True
            contact_id = row['contact'].get('id')
            contact_name = row['contact'].get('name')
            contact_username = row['contact'].get('username')
            contact_email = row['contact'].get('email')
        else:
            contact_id = None
            contact_name = None
            contact_username = None
            contact_email = None
        if 'hostName' in row:
            host_name = row.get('hostName')
        else:
            host_name = None
        if 'port' in row:
            port = row.get('port')
        else:
            port = None
        if 'extendedConnectionType' in row:
            extended_connection_type = row.get('extendedConnectionType')
        else:
            extended_connection_type = None
        if 'service' in row:
            service = row.get('service')
        else:
            service = None
        if 'filePath' in row:
            file_path = row.get('filePath')
        else:
            file_path = None
        if 'provider' in row:
            provider = row.get('provider')
        else:
            provider = None
        if 'fileExtension' in row:
            file_extension = row.get('fileExtension')
        else:
            file_extension = None
        if 'fileID' in row:
            file_id = row.get('fileID')
        else:
            file_id = None
        if 'mimeType' in row:
            mime_type = row.get('mimeType')
        else:
            mime_type = None
        if 'requestUrl' in row:
            request_url = row.get('requestUrl')
        else:
            request_url = None
        if 'isEmbedded' in row:
            is_embedded = row.get('isEmbedded')
        else:
            is_embedded = None
        if 'connectorUrl' in row:
            connector_url = row.get('connectorUrl')
        else:
            connector_url = None
        if 'downstreamWorkbooks' in row:
            for asset_instance in row.get('downstreamWorkbooks'):
                asset_row_to_add = [asset_id, name, type_name, connection_type, certified, site_id, site_name,
                                    asset_instance.get('id'), asset_instance.get('name'),
                                    'Workbooks', asset_instance.get('isCertified'),
                                    asset_instance.get('projectName'), contact_id, contact_name, contact_username,
                                    contact_email]
                database_asset_rows.append(asset_row_to_add)
        if 'downstreamFlows' in row:
            for asset_instance in row.get('downstreamFlows'):
                asset_row_to_add = [asset_id, name, type_name, connection_type, certified, site_id, site_name,
                                    asset_instance.get('id'), asset_instance.get('name'),
                                    'Flows', asset_instance.get('isCertified'),
                                    asset_instance.get('projectName'), contact_id, contact_name, contact_username,
                                    contact_email]
                database_asset_rows.append(asset_row_to_add)
        if 'downstreamDatasources' in row:
            for asset_instance in row.get('downstreamDatasources'):
                asset_row_to_add = [asset_id, name, type_name, connection_type, certified, site_id, site_name,
                                    asset_instance.get('id'), asset_instance.get('name'),
                                    'Data Sources', asset_instance.get('isCertified'),
                                    asset_instance.get('projectName'), contact_id, contact_name, contact_username,
                                    contact_email]
                database_asset_rows.append(asset_row_to_add)
        if 'downstreamMetrics' in row:
            for asset_instance in row.get('downstreamMetrics'):
                asset_row_to_add = [asset_id, name, type_name, connection_type, certified, site_id, site_name,
                                    asset_instance.get('id'), asset_instance.get('name'),
                                    'Metrics', asset_instance.get('isCertified'),
                                    asset_instance.get('projectName'), contact_id, contact_name, contact_username,
                                    contact_email]
                database_asset_rows.append(asset_row_to_add)
        if 'downstreamLenses' in row:
            for asset_instance in row.get('downstreamLenses'):
                asset_row_to_add = [asset_id, name, type_name, connection_type, certified, site_id, site_name,
                                    asset_instance.get('id'), asset_instance.get('name'),
                                    'Lenses', asset_instance.get('isCertified'),
                                    asset_instance.get('projectName'), contact_id, contact_name, contact_username,
                                    contact_email]
                database_asset_rows.append(asset_row_to_add)
        if 'downstreamVirtualConnections' in row:
            for asset_instance in row.get('downstreamVirtualConnections'):
                asset_row_to_add = [asset_id, name, type_name, connection_type, certified, site_id, site_name,
                                    asset_instance.get('id'), asset_instance.get('name'),
                                    'VirtualConnections', asset_instance.get('isCertified'),
                                    asset_instance.get('projectName'), contact_id, contact_name, contact_username,
                                    contact_email]
                database_asset_rows.append(asset_row_to_add)


        row_to_add = [asset_id, site_id, site_name, luid, viz_portal_id, name, description, type_name, connection_type,
                      certified, grouped, controlled_permissions_enabled, has_active_warning, contact_id, contact_name,
                      contact_username, contact_email, host_name, port, extended_connection_type, service, file_path,
                      provider, file_extension, file_id, mime_type, request_url, is_embedded, connector_url,
                      has_description, has_contact]

        database_rows.append(row_to_add)

    update_hyper(hyper_connection, database_rows, database_table_definition)
    update_hyper(hyper_connection, database_asset_rows, database_asset_table_definition)


def insert_into_table_tables(hyper_connection, site_id, site_name, table_data, table_definition):
    table_rows = []
    for row in table_data:
        asset_id = row.get('id')
        name = row.get('name')
        type_name = row.get('__typename')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        embedded = row.get('isEmbedded')
        if 'luid' in row:
            luid = row.get('luid')
        else:
            luid = None
        if 'vizPortalId' in row:
            viz_portal_id = row.get('vizPortalId')
        else:
            viz_portal_id = None
        if 'schema' in row:
            schema = row.get('schema')
        else:
            schema = None
        if 'fullName' in row:
            full_name = row.get('fullName')
        else:
            full_name = None
        if 'connectionType' in row:
            connection_type = row.get('connectionType')
        else:
            connection_type = None
        has_contact = False
        contact_id = None
        contact_name = None
        contact_username = None
        contact_email = None
        if 'contact' in row:
            if row['contact']:
                has_contact = True
                contact_id = row['contact'].get('id')
                contact_name = row['contact'].get('name')
                contact_username = row['contact'].get('username')
                contact_email = row['contact'].get('email')
        if 'isCertified' in row:
            is_certified = row.get('isCertified')
        else:
            is_certified = None
        database_id = None
        if 'database' in row:
            # database could be null if we could not parse the custom SQL
            if row['database']:
                database_id = row['database'].get('id')
        if 'hasActiveWarning' in row:
            active_warning = row.get('hasActiveWarning')
        else:
            active_warning = None
        if 'query' in row:
            sql_query = row.get('query')
        else:
            sql_query = None
        if 'isUnsupportedCustomSql' in row:
            is_unsupported_custom_sql = row.get('isUnsupportedCustomSql')
        else:
            is_unsupported_custom_sql = None
        if 'isExtracted' in row:
            is_extracted = row.get('isExtracted')
        else:
            is_extracted = None
        if 'extractLastRefreshType' in row:
            extract_last_refreshed_type = row.get('extractLastRefreshType')
        else:
            extract_last_refreshed_type = None
        if 'extractLastRefreshAt' in row:
            extract_last_refreshed_at = row.get('extractLastRefreshAt')
        else:
            extract_last_refreshed_at = None
        if 'owner' in row:
            if row['owner']:
                contact_id = row['owner'].get('id')
        if 'virtualConnection' in row:
            if row['virtualConnection']:
                virtual_connection_id = row['virtualConnection'].get('id')
            else:
                virtual_connection_id = None
        else:
            virtual_connection_id = None
        row_to_add = [asset_id, site_id, site_name, name, type_name, description, embedded, luid, viz_portal_id,
                      schema, full_name, connection_type, contact_id, contact_name, contact_username, contact_email,
                      is_certified, database_id, active_warning, sql_query, is_unsupported_custom_sql, is_extracted,
                      virtual_connection_id, extract_last_refreshed_at, extract_last_refreshed_type, has_description,
                      has_contact]
        table_rows.append(row_to_add)

    update_hyper(hyper_connection, table_rows, table_definition)


def insert_into_column_tables(hyper_connection, site_id, site_name, column_data, column_table_definition,
                              column_asset_table_definition):
    # Insert the results into Hyper

    column_rows = []
    column_asset_rows = []

    for row in column_data:
        asset_id = row.get('id')
        viz_portal_id = row.get('vizportalId')
        luid = row.get('luid')
        name = row.get('name')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        description_inherited = None
        remote_type = row.get('remoteType')
        nullable = row.get('isNullable')
        table_id = None
        table_name = None
        table_type = None
        certified_table_id = None
        certified_table = None
        database_id = None
        database_name = None
        database_type = None
        database_connection_type = None
        certified_database_id = None
        certified_database = None
        if row['table']:
            table_id = row['table'].get('id')
            table_name = row['table'].get('name')
            table_type = row['table'].get('__typename')
            certified_table = row['table'].get('isCertified')
            if certified_table:
                certified_table_id = table_id
            if 'database' in row['table']:
                if row['table']['database']:
                    database_id = row['table']['database'].get('id')
                    database_name = row['table']['database'].get('name')
                    database_connection_type = row['table']['database'].get('connectionType')
                    database_type = row['table']['database'].get('__typename')
                    certified_database = row['table']['database'].get('isCertified')
                    if certified_database:
                        certified_database_id = database_id
        row_to_add = [asset_id, site_id, site_name, viz_portal_id, luid, name, description, description_inherited,
                      remote_type, nullable, table_id, database_id, has_description]
        column_rows.append(row_to_add)

        has_assets = False
        if 'downstreamWorkbooks' in row:
            for asset_instance in row.get('downstreamWorkbooks'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Workbooks', asset_instance.get('projectName')]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamDashboards' in row:
            for asset_instance in row.get('downstreamDashboards'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Dashboards', ""]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamSheets' in row:
            for asset_instance in row.get('downstreamSheets'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Sheets', ""]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamFlows' in row:
            for asset_instance in row.get('downstreamFlows'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Flows', asset_instance.get('projectName')]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamDatasources' in row:
            for asset_instance in row.get('downstreamDatasources'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Data Sources', asset_instance.get('projectName')]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamMetrics' in row:
            for asset_instance in row.get('downstreamMetrics'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Metrics', asset_instance.get('projectName')]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamLenses' in row:
            for asset_instance in row.get('downstreamLenses'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'Lenses', asset_instance.get('projectName')]
                column_asset_rows.append(asset_row_to_add)
        if 'downstreamVirtualConnections' in row:
            for asset_instance in row.get('downstreamVirtualConnections'):
                has_assets = True
                asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                    certified_table, database_id, database_name, database_type,
                                    database_connection_type, certified_database_id,
                                    certified_database, site_id, site_name, has_assets, asset_instance.get('id'),
                                    asset_instance.get('name'), 'VirtualConnections', asset_instance.get('projectName')]
                column_asset_rows.append(asset_row_to_add)
        if not has_assets:
            asset_row_to_add = [asset_id, name, remote_type, table_id, table_name, table_type, certified_table_id,
                                certified_table, database_id, database_name, database_type, database_connection_type,
                                certified_database_id, certified_database, site_id, site_name, has_assets, None, None,
                                None, None ]
            column_asset_rows.append(asset_row_to_add)

    update_hyper(hyper_connection, column_rows, column_table_definition)
    update_hyper(hyper_connection, column_asset_rows, column_asset_table_definition)


def insert_into_field_tables(hyper_connection, site_id, site_name, field_data, field_table_definition,
                             referenced_field_table_definition, field_asset_table_definition):
    # Create the data holders
    field_rows = []
    referenced_field_rows = []
    field_asset_rows = []

    for row in field_data:
        asset_id = row.get('id')
        name = row.get('name')
        fully_qualified_name = row.get('fullyQualifiedName')
        has_description = False
        description = row.get('description')
        if description == '':
            pass
        else:
            has_description = True
        description_inherited = None
        hidden = row.get('isHidden')
        folder_name = row.get('folderName')
        type_name = row.get('__typename')
        if 'binSize' in row:
            bin_size = row.get('binSize')
        else:
            bin_size = None
        if 'dataType' in row:
            data_type = row.get('dataType')
        else:
            data_type = None
        if 'dataCategory' in row:
            data_category = row.get('dataCategory')
        else:
            data_category = None
        if 'role' in row:
            role = row.get('role')
        else:
            role = None
        if 'formula' in row:
            formula = row.get('formula')
        else:
            formula = None
        if 'defaultFormat' in row:
            default_format = row.get('defaultFormat')
        else:
            default_format = None
        if 'semanticRole' in row:
            semantic_role = row.get('semanticRole')
        else:
            semantic_role = None
        if 'aggregation' in row:
            aggregation = row.get('aggregation')
        else:
            aggregation = None
        if 'aggregationParameter' in row:
            aggregation_parameter = row.get('aggregationParameter')
        else:
            aggregation_parameter = None
        if 'isAutoGenerated' in row:
            auto_generated = row.get('isAutoGenerated')
        else:
            auto_generated = None
        if 'columns' in row:
            if row['columns']:
                column_id = row['columns'][0].get('id')
            else:
                column_id = None
        else:
            column_id = None
        remote_field_id = None
        if 'hasUserReference' in row:
            has_user_reference = row.get('hasUserReference')
        else:
            has_user_reference = None
        if 'delimiter' in row:
            delimiter = row.get('delimiter')
        else:
            delimiter = None
        if 'combinationType' in row:
            combination_type = row.get('combinationType')
        else:
            combination_type = None
        if 'hasOther' in row:
            has_other = row.get('hasOther')
        else:
            has_other = None
        # Get all Field ID for fields used in calculation
        if 'fields' in row:
            for referenced_field in row['fields']:
                referenced_field_row_to_add = [asset_id, referenced_field.get('id')]
                referenced_field_rows.append(referenced_field_row_to_add)
        # Get related datasource, sheet, dashboard, workbook info
        datasource_id = None
        datasource_name = None
        datasource_type = None
        sheet_id = None
        sheet_name = None
        dashboard_id = None
        dashboard_name = None
        workbook_id = None
        workbook_name = None
        if row['datasource']:
            datasource_id = row['datasource'].get('id')
            datasource_name = row['datasource'].get('name')
            datasource_type = row['datasource'].get('__typename')
        if 'sheets' in row:
            for sheet_instance in row.get('sheets'):
                sheet_id = sheet_instance.get('id')
                sheet_name = sheet_instance.get('name')
                if 'workbook' in sheet_instance:
                    if sheet_instance.get('workbook'):
                        workbook_instance = sheet_instance.get('workbook')
                        workbook_id = workbook_instance.get('id')
                        workbook_name = workbook_instance.get('name')
                if 'containedInDashboards' in sheet_instance:
                    if sheet_instance.get('containedInDashboards'):
                        for dashboard_instance in sheet_instance.get('containedInDashboards'):
                            dashboard_id = dashboard_instance.get('id')
                            dashboard_name = dashboard_instance.get('name')

                            asset_row_to_add = [asset_id, site_id, site_name, name, fully_qualified_name, description,
                                        description_inherited, type_name, datasource_id, datasource_name, datasource_type,
                                        workbook_id,  workbook_name, sheet_id, sheet_name, dashboard_id, dashboard_name, data_type,
                                        column_id]

                            field_asset_rows.append(asset_row_to_add)
                    else:
                        asset_row_to_add = [asset_id, site_id, site_name, name, fully_qualified_name, description,
                                            description_inherited, type_name, datasource_id, datasource_name,
                                            datasource_type,
                                            workbook_id, workbook_name, sheet_id, sheet_name, dashboard_id, dashboard_name,
                                            data_type,                                       column_id]

                    field_asset_rows.append(asset_row_to_add)

        asset_row_to_add = [asset_id, site_id, site_name, name, fully_qualified_name, description,
                            description_inherited, type_name, datasource_id, datasource_name, datasource_type,
                            workbook_id, workbook_name, sheet_id, sheet_name, dashboard_id, dashboard_name,
                            data_type,
                            column_id]

        field_asset_rows.append(asset_row_to_add)

        row_to_add = [asset_id, site_id, site_name, name, fully_qualified_name, description, description_inherited,
                      hidden, folder_name, type_name, datasource_id, bin_size, data_type, data_category, role, formula,
                      default_format, semantic_role, aggregation, aggregation_parameter, auto_generated,
                      has_user_reference, column_id, remote_field_id, delimiter, combination_type, has_other,
                      has_description]

        field_rows.append(row_to_add)



    update_hyper(hyper_connection, field_rows, field_table_definition)
    update_hyper(hyper_connection, referenced_field_rows, referenced_field_table_definition)
    update_hyper(hyper_connection, field_asset_rows, field_asset_table_definition)


def insert_into_virtual_connection_tables(hyper_connection, site_id, site_name, virtual_connection_data,
                                          virtual_connection_table_definition):
    virtual_connection_rows = []
    for row in virtual_connection_data:
        asset_id = row.get('id')
        name = row.get('name')
        type_name = row.get('__typename')
        if 'luid' in row:
            luid = row.get('luid')
        else:
            luid = None
        if 'connectionType' in row:
            connection_type = row.get('connectionType')
        else:
            connection_type = None
        if 'projectName' in row:
            project_name = row.get('projectName')
        else:
            project_name = None
        if 'projectVizportalUrlId' in row:
            project_vizportal_url_id = row.get('projectVizportalUrlId')
        else:
            project_vizportal_url_id = None
        if 'containerType' in row:
            container_type = row.get('containerType')
        else:
            container_type = None
        if 'containerName' in row:
            container_name = row.get('containerName')
        else:
            container_name = None
        has_owner = False
        if 'owner' in row:
            has_owner = True
            owner_id = row['owner'].get('id')
            owner_name = row['owner'].get('name')
            owner_username = row['owner'].get('username')
            owner_email = row['owner'].get('email')
        else:
            owner_id = None
            owner_name = None
            owner_username = None
            owner_email = None
        if 'isCertified' in row:
            is_certified = row.get('isCertified')
        else:
            is_certified = None
        has_description = False
        if 'description' in row:
            description = row.get('description')
            if description != '':
                has_description = True
        else:
            description = None
        if 'hasActiveWarning' in row:
            has_active_warning = row.get('hasActiveWarning')
        else:
            has_active_warning = None
        if 'uri' in row:
            uri = row.get('uri')
        else:
            uri = None
        if 'vizportalId' in row:
            vizportal_id = row.get('vizportalId')
        else:
            vizportal_id = None
        if 'vizportalUrlId' in row:
            vizportal_url_id = row.get('vizportalUrlId')
        else:
            vizportal_url_id = None
        created_at = None
        if row['createdAt']:
            created_at = iso8601.parse_date(row.get('createdAt'))
        updated_at = None
        if row['updatedAt']:
            updated_at = iso8601.parse_date(row.get('updatedAt'))

        row_to_add = [asset_id, site_id, site_name, name, type_name, luid, uri, is_certified, has_active_warning,
                      description, project_name, project_vizportal_url_id, container_type, container_name,
                      connection_type, owner_id, owner_name, owner_username, owner_email, vizportal_id,
                      vizportal_url_id, created_at, updated_at, has_description, has_owner]
        virtual_connection_rows.append(row_to_add)

    update_hyper(hyper_connection, virtual_connection_rows, virtual_connection_table_definition)


def insert_into_datasource_tables(hyper_connection, site_id, site_name, datasource_data, datasource_table_definition,
                                  datasource_workbooks_table_definition):
    # Create holder for datasource data
    datasource_rows = []
    datasource_workbook_rows = []
    for row in datasource_data:
        asset_id = row.get('id')
        name = row.get('name')
        type_name = row.get('__typename')
        contains_unsupported_custom_sql = row.get('containsUnsupportedCustomSql')
        has_user_reference = row.get('hasUserReference')
        has_extracts = row.get('hasExtracts')
        extract_last_refresh_time = None
        if row.get('extractLastRefreshTime'):
            extract_last_refresh_time = iso8601.parse_date(row.get('extractLastRefreshTime'))
        extract_last_update_time = None
        if row.get('extractLastUpdateTime'):
            extract_last_update_time = iso8601.parse_date(row.get('extractLastUpdateTime'))
        extract_last_incremental_update_time = None
        if row.get('extractLastIncrementalUpdateTime'):
            extract_last_incremental_update_time = iso8601.parse_date(row.get('extractLastIncrementalUpdateTime'))
        if 'luid' in row:
            luid = row.get('luid')
        else:
            luid = None
        if 'projectVizportalUrlId' in row:
            project_vizportal_url_id = row.get('projectVizportalUrlId')
        else:
            project_vizportal_url_id = None
        if 'containerType' in row:
            container_type = row.get('containerType')
        else:
            container_type = None
        if 'containerName' in row:
            container_name = row.get('containerName')
        else:
            container_name = None
        has_owner = False
        if 'owner' in row:
            has_owner = True
            owner_id = row['owner'].get('id')
            owner_name = row['owner'].get('name')
            owner_username = row['owner'].get('username')
            owner_email = row['owner'].get('email')
        else:
            owner_id = None
            owner_name = None
            owner_username = None
            owner_email = None
        if 'isCertified' in row:
            is_certified = row.get('isCertified')
        else:
            is_certified = None
        has_description = False
        if 'description' in row:
            description = row.get('description')
            if description != '':
                has_description = True
        else:
            description = None
        if 'projectName' in row:
            project_name = row.get('projectName')
        else:
            project_name = None
        if 'hasActiveWarning' in row:
            has_active_warning = row.get('hasActiveWarning')
        else:
            has_active_warning = None
        if 'uri' in row:
            uri = row.get('uri')
        else:
            uri = None
        if 'vizportalId' in row:
            vizportal_id = row.get('vizportalId')
        else:
            vizportal_id = None
        if 'vizportalUrlId' in row:
            vizportal_url_id = row.get('vizportalUrlId')
        else:
            vizportal_url_id = None
        if 'workbook' in row:
            workbook_row_to_add = [asset_id, name, type_name, is_certified, site_id, site_name, row['workbook'].get('id'),
                                   row['workbook'].get('name'), project_name, owner_id, owner_name, owner_username,
                                   owner_email, has_description, has_owner]
            datasource_workbook_rows.append(workbook_row_to_add)
        if 'downstreamWorkbooks' in row:
            for workbook_instance in row.get('downstreamWorkbooks'):
                workbook_row_to_add = [asset_id, name, type_name, is_certified, site_id, site_name,
                                       workbook_instance.get('id'), workbook_instance.get('name'), project_name,
                                       owner_id, owner_name, owner_username, owner_email, has_description, has_owner]
                datasource_workbook_rows.append(workbook_row_to_add)

        row_to_add = [asset_id, site_id, site_name, name, type_name, contains_unsupported_custom_sql,
                      has_user_reference, has_extracts, extract_last_refresh_time, extract_last_update_time,
                      extract_last_incremental_update_time, luid, project_name, project_vizportal_url_id,
                      container_type, container_name, owner_id, owner_name, owner_username, owner_email, is_certified,
                      description, has_active_warning, uri, vizportal_id, vizportal_url_id, has_description,
                      has_owner]
        datasource_rows.append(row_to_add)

    update_hyper(hyper_connection, datasource_rows, datasource_table_definition)
    update_hyper(hyper_connection, datasource_workbook_rows, datasource_workbooks_table_definition)


def insert_into_project_tables(hyper_connection, site_id, site_name, project_data, project_table_def):
    # Projects data
    project_rows = []
    for row in project_data:
        project_id = row.id
        project_name = row.name
        has_description = False
        description = row.description
        if description != '':
            has_description = True
        content_permissions = row.content_permissions
        parent_id = row.parent_id

        row_to_add = [project_id, site_id, site_name, project_name, description, content_permissions, parent_id,
                      has_description]
        project_rows.append(row_to_add)

    update_hyper(hyper_connection, project_rows, project_table_def)


def insert_into_workbook_tables(hyper_connection, site_id, site_name, workbook_data, workbook_table_definition):
    # Create list to hold data rows
    workbook_rows = []
    for row in workbook_data:
        asset_id = row.get('id')
        luid = row.get('luid')
        name = row.get('name')
        contains_unsupported_custom_sql = row.get('containsUnsupportedCustomSql')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        create_datetime = None
        if row.get('createdAt'):
            create_datetime = iso8601.parse_date(row.get('createdAt'))
        update_datetime = None
        if row.get('updatedAt'):
            update_datetime = iso8601.parse_date(row.get('updatedAt'))
        project_name = row.get('projectName')
        project_viz_portal_id = row.get('projectVizportalUrlId')
        container_name = row.get('containerName')
        container_type = row.get('containerType')
        has_owner = False
        if row['owner']:
            has_owner = True
            owner_id = row['owner'].get('id')
            owner_name = row['owner'].get('name')
            owner_username = row['owner'].get('username')
            owner_email = row['owner'].get('email')
        else:
            owner_id = None
            owner_name = None
            owner_username = None
            owner_email = None
        uri = row.get('uri')
        vizportal_url_id = row.get('vizportalUrlId')

        row_to_add = [asset_id, site_id, site_name, luid, name, contains_unsupported_custom_sql, description,
                      create_datetime, update_datetime, project_name, project_viz_portal_id, container_type,
                      container_name, owner_id, owner_name, owner_username, owner_email, uri, vizportal_url_id,
                      has_description, has_owner]

        workbook_rows.append(row_to_add)

    update_hyper(hyper_connection, workbook_rows, workbook_table_definition)


def insert_into_view_tables(hyper_connection, site_id, site_name, view_data, dashboard_table_definition,
                            sheet_table_definition, sheet_field_table_definition, dashboard_sheet_table_definition,
                            view_table_definition):
    # Create holders for data
    dashboard_rows = []
    sheet_rows = []
    view_rows = []
    sheet_field_rows = []
    dashboard_sheet_rows = []

    for row in view_data:
        asset_id = row.get('id')
        luid = row.get('luid')
        name = row.get('name')
        path = row.get('path')
        typename = row.get('__typename')
        create_datetime = None
        if row.get('createdAt'):
            create_datetime = iso8601.parse_date(row.get('createdAt'))
        update_datetime = None
        if row.get('updatedAt'):
            update_datetime = iso8601.parse_date(row.get('updatedAt'))
        index = row.get('index')
        has_owner = False
        workbook_id = None
        workbook_luid = None
        workbook_owner_id = None
        workbook_owner_luid = None
        workbook_owner_name = None
        workbook_owner_username = None
        workbook_owner_email = None
        if row['workbook']:
            workbook_id = row['workbook'].get('id')
            workbook_luid = row['workbook'].get('luid')
            if row['workbook']['owner']:
                has_owner = True
                workbook_owner_id = row['workbook']['owner'].get('id')
                workbook_owner_luid = row['workbook']['owner'].get('luid')
                workbook_owner_name = row['workbook']['owner'].get('name')
                workbook_owner_username = row['workbook']['owner'].get('username')
                workbook_owner_email = row['workbook']['owner'].get('email')
        if 'containedInDashboards' in row:
            # Get all the dashboards that use this sheet, if applicable
            for sheet_instance in row.get('containedInDashboards'):
                sheet_row_to_add = [sheet_instance.get('id'), asset_id]
                dashboard_sheet_rows.append(sheet_row_to_add)

        if 'sheetFieldInstances' in row:
            # Get all the fields that use are connected to this sheet
            for field_instance in row.get('sheetFieldInstances'):
                field_row_to_add = [asset_id, field_instance.get('id')]
                sheet_field_rows.append(field_row_to_add)

        if typename == 'Dashboard':
            row_to_add = [asset_id, site_id, site_name, luid, name, path, create_datetime, update_datetime, index,
                          workbook_id, workbook_luid, workbook_owner_id, workbook_owner_luid, workbook_owner_name,
                          workbook_owner_username, workbook_owner_email, row.get('__typename'), has_owner]
            dashboard_rows.append(row_to_add)
            view_rows.append(row_to_add)
        elif typename == 'Sheet':
            row_to_add = [asset_id, site_id, site_name, luid, name, path, create_datetime, update_datetime, index,
                          workbook_id, workbook_luid, workbook_owner_id, workbook_owner_luid, workbook_owner_name,
                          workbook_owner_username, workbook_owner_email, row.get('__typename'), has_owner]
            sheet_rows.append(row_to_add)
            view_rows.append(row_to_add)

    update_hyper(hyper_connection, dashboard_rows, dashboard_table_definition)
    update_hyper(hyper_connection, sheet_rows, sheet_table_definition)
    update_hyper(hyper_connection, view_rows, view_table_definition)
    update_hyper(hyper_connection, sheet_field_rows, sheet_field_table_definition)
    update_hyper(hyper_connection, dashboard_sheet_rows, dashboard_sheet_table_definition)


def insert_into_metric_tables(hyper_connection, site_id, site_name, metric_data, metric_table_definition):
    metric_rows = []
    for row in metric_data:
        asset_id = row.get('id')
        luid = row.get('luid')
        project_name = row.get('projectName')
        project_viz_portal_url_id = row.get('projectVizportalUrlId')
        viz_portal_url_id = row.get('vizportalUrlId')
        if row['underlyingView']:
            underlying_view_id = row['underlyingView'].get('id')
        else:
            underlying_view_id = None
        container_name = row.get('containerName')
        container_type = row.get('containerType')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        name = row.get('name')
        has_owner = False
        if row['owner']:
            has_owner = True
            owner_id = row['owner'].get('id')
            owner_name = row['owner'].get('name')
            owner_username = row['owner'].get('username')
            owner_email = row['owner'].get('email')
        else:
            owner_id = None
            owner_name = None
            owner_username = None
            owner_email = None
        create_datetime = None
        if row.get('createdAt'):
            create_datetime = iso8601.parse_date(row.get('createdAt'))
        update_datetime = None
        if row.get('updatedAt'):
            update_datetime = iso8601.parse_date(row.get('updatedAt'))

        row_to_add = [asset_id, luid, site_id, site_name, project_name, project_viz_portal_url_id, viz_portal_url_id,
                      container_type, container_name, underlying_view_id, description, name, owner_id, owner_name,
                      owner_username, owner_email, create_datetime, update_datetime, has_description, has_owner]
        metric_rows.append(row_to_add)

    update_hyper(hyper_connection, metric_rows, metric_table_definition)


def insert_into_owner_tables(hyper_connection, site_id, site_name, table_data_df, owner_table_definition,
                             owner_asset_table_definition):
    # Insert the results into Hyper
    user_rows = []
    owner_asset_rows = []
    for row in table_data_df:
        owner_id = row.get('id')
        luid = row.get('luid')
        name = row.get('name')
        user_name = row.get('username')
        viz_portal_url_id = row.get('vizportalUrlId')
        uri = row.get('uri')
        domain = row.get('domain')
        email = row.get('email')
        asset_name = None
        asset_connection_type = None
        project_name = None
        certified = None
        dqw_type = None
        dqw_asset_id = None
        dqw_asset_name = None
        dqw_asset_type = None
        dqc_asset_id = None
        dqc_asset_name = None
        dqc_asset_type = None
        if 'contactForDatabases' in row:
            for asset_instance in row.get('contactForDatabases'):
                asset_id = asset_instance.get('id')
                asset_name = asset_instance.get('name')
                asset_type = 'Databases'
                asset_subtype = asset_instance.get('__typename')
                asset_connection_type = asset_instance.get('connectionType')
                certified = asset_instance.get('isCertified')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'contactForTables' in row:
            for asset_instance in row.get('contactForTables'):
                asset_id = asset_instance.get('id')
                asset_type = 'Tables'
                asset_subtype = asset_instance.get('__typename')
                certified = asset_instance.get('isCertified')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'ownedDatasources' in row:
            for asset_instance in row.get('ownedDatasources'):
                asset_id = asset_instance.get('id')
                asset_name = asset_instance.get('name')
                asset_type = 'Data Source'
                asset_subtype = asset_instance.get('__typename')
                project_name = asset_instance.get('projectName')
                certified = asset_instance.get('isCertified')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'ownedWorkbooks' in row:
            for asset_instance in row.get('ownedWorkbooks'):
                asset_id = asset_instance.get('id')
                asset_name = asset_instance.get('name')
                asset_type = 'Workbooks'
                asset_subtype = asset_instance.get('__typename')
                project_name = asset_instance.get('projectName')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'ownedVirtualConnections' in row:
            for asset_instance in row.get('ownedVirtualConnections'):
                asset_id = asset_instance.get('id')
                asset_name = asset_instance.get('name')
                asset_type = 'Virtual Connections'
                asset_subtype = asset_instance.get('__typename')
                certified = asset_instance.get('isCertified')
                project_name = asset_instance.get('projectName')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'ownedFlows' in row:
            for asset_instance in row.get('ownedFlows'):
                asset_id = asset_instance.get('id')
                asset_name = asset_instance.get('name')
                asset_type = 'Flows'
                asset_subtype = asset_instance.get('__typename')
                project_name = asset_instance.get('projectName')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'ownedMetrics' in row:
            for asset_instance in row.get('ownedMetrics'):
                asset_id = asset_instance.get('id')
                asset_name = asset_instance.get('name')
                asset_type = 'Metrics'
                asset_subtype = asset_instance.get('__typename')
                project_name = asset_instance.get('projectName')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'authoredDataQualityWarnings' in row:
            for asset_instance in row.get('authoredDataQualityWarnings'):
                asset_id = asset_instance.get('id')
                asset_type = 'Data Quality Warning'
                asset_subtype = asset_instance.get('__typename')
                dqw_type = asset_instance.get('warningType')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)
        if 'authoredDataQualityCertifications' in row:
            for asset_instance in row.get('authoredDataQualityCertifications'):
                asset_id = asset_instance.get('id')
                asset_type = 'Data Quality Certification'
                asset_subtype = asset_instance.get('__typename')
                asset_row_to_add = [owner_id, site_id, site_name, name, user_name, email, domain, asset_id, asset_name,
                                    asset_type, asset_subtype, asset_connection_type, certified, project_name, dqw_type,
                                    dqw_asset_id, dqw_asset_name, dqw_asset_type, dqc_asset_id, dqc_asset_name,
                                    dqc_asset_type]
                owner_asset_rows.append(asset_row_to_add)

        row_to_add = [owner_id, site_id, site_name, luid, name, user_name, viz_portal_url_id, uri, domain, email]

        user_rows.append(row_to_add)

    update_hyper(hyper_connection, user_rows, owner_table_definition)
    update_hyper(hyper_connection, owner_asset_rows, owner_asset_table_definition)


def insert_into_dqw_tables(hyper_connection, site_id, site_name, dqw_data, dqw_table_definition):
    dqw_rows = []
    for row in dqw_data:
        dqw_id = row.get('id')
        luid = row.get('luid')
        if row['author']:
            author_id = row['author'].get('id')
            author_name = row['author'].get('name')
            author_username = row['author'].get('username')
            author_email = row['author'].get('email')
        else:
            author_id = None
            author_name = None
            author_username = None
            author_email = None
        author_display_name = row.get('authorDisplayName')
        viz_portal_url_id = row.get('vizportalUrlId')
        active = row.get('isActive')
        severe = row.get('isSevere')
        warning_type = row.get('warningType')
        message = row.get('message')
        create_datetime = None
        if row.get('createdAt'):
            create_datetime = iso8601.parse_date(row.get('createdAt'))
        update_datetime = None
        if row.get('updatedAt'):
            update_datetime = iso8601.parse_date(row.get('updatedAt'))
        if row['asset']:
            # Get all Field ID for fields used in calculation
            asset_id = row['asset'].get('id')
        else:
            asset_id = None

        row_to_add = [dqw_id, site_id, site_name, luid, author_id, author_display_name, author_name, author_username,
                      author_email, viz_portal_url_id, active, severe, warning_type, message, create_datetime,
                      update_datetime, asset_id]
        dqw_rows.append(row_to_add)

    update_hyper(hyper_connection, dqw_rows, dqw_table_definition)


def insert_into_parameter_tables(hyper_connection, site_id, site_name, parameter_data, parameter_table_definition,
                                 calculation_parameter_table_definition):
    # Insert the results into Hyper
    parameter_rows = []
    referenced_parameter_rows = []
    for row in parameter_data:
        asset_id = row.get('id')
        name = row.get('name')
        parent_name = row.get('parentName')
        if row['workbook']:
            workbook_id = row['workbook'].get('id')
        else:
            workbook_id = None
        if row['datasource']:
            datasource_id = row['datasource'].get('id')
        else:
            datasource_id = None

        if row['referencedByCalculations']:
            # Get all Field ID for fields used in calculation
            for referenced_parameter in row['referencedByCalculations']:
                referenced_parameter_row_to_add = [asset_id, referenced_parameter.get('id'),
                                                   referenced_parameter.get('__typename'), site_id, site_name]
                referenced_parameter_rows.append(referenced_parameter_row_to_add)

        if row['referencedByBins']:
            # Get all Field ID for fields used in calculation
            for referenced_parameter in row['referencedByBins']:
                referenced_parameter_row_to_add = [asset_id, referenced_parameter.get('id'),
                                                   referenced_parameter.get('__typename'), site_id, site_name]
                referenced_parameter_rows.append(referenced_parameter_row_to_add)

        if row['referencedBySets']:
            # Get all Field ID for fields used in calculation
            for referenced_parameter in row['referencedBySets']:
                referenced_parameter_row_to_add = [asset_id, referenced_parameter.get('id'),
                                                   referenced_parameter.get('__typename'), site_id, site_name]
                referenced_parameter_rows.append(referenced_parameter_row_to_add)

        row_to_add = [asset_id, name, parent_name, site_id, site_name, workbook_id, datasource_id]
        parameter_rows.append(row_to_add)

    update_hyper(hyper_connection, parameter_rows, parameter_table_definition)
    update_hyper(hyper_connection, referenced_parameter_rows, calculation_parameter_table_definition)


def insert_into_dqc_tables(hyper_connection, site_id, site_name, dqc_data, dqc_table_definition):
    dqc_rows = []
    for row in dqc_data:
        dqc_id = row.get('id')
        luid = row.get('luid')
        if row['author']:
            author_id = row['author'].get('id')
            author_name = row['author'].get('name')
            author_username = row['author'].get('username')
            author_email = row['author'].get('email')
        else:
            author_id = None
            author_name = None
            author_username = None
            author_email = None
        author_display_name = row.get('authorDisplayName')
        viz_portal_url_id = row.get('vizportalUrlId')
        active = row.get('isActive')
        message = row.get('message')
        create_datetime = None
        if row.get('createdAt'):
            create_datetime = iso8601.parse_date(row.get('createdAt'))
        update_datetime = None
        if row.get('updatedAt'):
            update_datetime = iso8601.parse_date(row.get('updatedAt'))
        if row['asset']:
            asset_id = row['asset'].get('id')
        else:
            asset_id = None

        row_to_add = [dqc_id, site_id, site_name, luid, author_id, author_display_name, author_name, author_username,
                      author_email, viz_portal_url_id, active, message, create_datetime, update_datetime, asset_id]
        dqc_rows.append(row_to_add)

    update_hyper(hyper_connection, dqc_rows, dqc_table_definition)


def insert_into_user_tables(hyper_connection, site_id, site_name, user_data, user_table_def):
    # Users data
    user_rows = []
    for row in user_data:
        user_id = row.id
        user_name = row.name
        full_name = row.fullname
        email = row.email
        domain_name = row.domain_name
        site_role = row.site_role
        ext_auth_user_id = row.external_auth_user_id
        auth_setting = row.auth_setting
        last_login = row.last_login

        row_to_add = [user_id, site_id, site_name, user_name, full_name, email, domain_name, site_role,
                      ext_auth_user_id, auth_setting, last_login]

        user_rows.append(row_to_add)

    update_hyper(hyper_connection, user_rows, user_table_def)


def insert_into_group_tables(tableau_server, hyper_connection, site_id, site_name, group_data, group_table_def,
                             group_user_table_def):
    # Groups data
    group_rows = []
    group_user_rows = []
    for row in group_data:
        group_id = row.id
        domain_name = row.domain_name
        group_name = row.name
        min_site_role = row.minimum_site_role
        license_mode = row.license_mode

        row_to_add = [group_id, site_id, site_name, domain_name, group_name, min_site_role, license_mode]

        group_rows.append(row_to_add)

        # populate users in group
        tableau_server.groups.populate_users(row)

        # get user information
        for user in row.users:
            group_user_id = user.id
            group_row_to_add = [group_id, group_user_id]
            group_user_rows.append(group_row_to_add)

    update_hyper(hyper_connection, group_rows, group_table_def)
    update_hyper(hyper_connection, group_user_rows, group_user_table_def)


def insert_into_tag_tables(hyper_connection, site_id, site_name, tag_data, tag_table_definition, asset_tag_table_definition):
    # Insert the results into Hyper
    tag_rows = []
    tag_asset_rows = []
    for row in tag_data:
        tag_id = row.get('id')
        name = row.get('name')
        if row['assets']:
            # Get all Field ID for fields used in calculation
            for tag_asset in row['assets']:
                tag_asset_row_to_add = [tag_id, tag_asset.get('id'), site_id, site_name]
                tag_asset_rows.append(tag_asset_row_to_add)

        row_to_add = [tag_id, name, site_id, site_name]
        tag_rows.append(row_to_add)

    update_hyper(hyper_connection, tag_rows, tag_table_definition)
    update_hyper(hyper_connection, tag_asset_rows, asset_tag_table_definition)


def insert_into_flow_tables(hyper_connection, site_id, site_name, flow_data, flow_table_definition):
    flow_rows = []
    for row in flow_data:
        asset_id = row.get('id')
        luid = row.get('luid')
        name = row.get('name')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        uri = row.get('uri')
        viz_portal_url_id = row.get('vizportalUrlId')
        has_active_warning = row.get('hasActiveWarning')
        project_name = row.get('projectName')
        portal_viz_portal_url_id = row.get('projectVizportalUrlId')
        personal_space_utl_link = row.get('personalSpaceUrlLink')
        container_name = row.get('containerName')
        container_type = row.get('containerType')
        contains_unsupported_custom_sql = row.get('containsUnsupportedCustomSql')
        create_datetime = None
        if row.get('createdAt'):
            create_datetime = iso8601.parse_date(row.get('createdAt'))
        update_datetime = None
        if row.get('updatedAt'):
            update_datetime = iso8601.parse_date(row.get('updatedAt'))
        has_owner = False
        if row['owner']:
            has_owner = True
            owner_id = row['owner'].get('luid')
            owner_name = row['owner'].get('name')
            owner_username = row['owner'].get('username')
            owner_email = row['owner'].get('email')
        else:
            owner_id = None
            owner_name = None
            owner_username = None
            owner_email = None

        row_to_add = [asset_id, site_id, site_name, luid, name, description, uri, viz_portal_url_id, has_active_warning,
                      project_name, portal_viz_portal_url_id, personal_space_utl_link, container_name, container_type,
                      contains_unsupported_custom_sql, owner_id, owner_name, owner_username, owner_email,
                      create_datetime, update_datetime, has_description, has_owner]

        flow_rows.append(row_to_add)

        # download_flow(site_id, luid, authentication_token, tab_server)

    update_hyper(hyper_connection, flow_rows, flow_table_definition)


def insert_into_lens_tables(hyper_connection, site_id, site_name, lenses_data, lenses_table_definition):
    lenses_rows = []
    for row in lenses_data:
        asset_id = row.get('id')
        luid = row.get('luid')
        name = row.get('name')
        viz_portal_url_id = row.get('vizportalUrlId')
        project_viz_portal_url_id = row.get('projectVizportalUrlId')
        datasource_id = None
        datasource_name = None
        if row['datasource']:
            datasource_id = row['datasource'].get('id')
            datasource_name = row['datasource'].get('name')
        has_owner = False
        owner_id = None
        owner_name = None
        owner_luid = None
        owner_username = None
        owner_uri = None
        owner_email = None
        owner_domain = None
        if row['owner']:
            has_owner = True
            owner_id = row['owner'].get('id')
            owner_name = row['owner'].get('name')
            owner_luid = row['owner'].get('luid')
            owner_username = row['owner'].get('username')
            owner_email = row['owner'].get('email')
            owner_domain = row['owner'].get('domain')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        created_at = None
        if row['createdAt']:
            created_at = iso8601.parse_date(row.get('createdAt'))
        updated_at = None
        if row['updatedAt']:
            updated_at = iso8601.parse_date(row.get('updatedAt'))
        row_to_add = [asset_id, site_id, site_name, luid, name, viz_portal_url_id, project_viz_portal_url_id,
                      datasource_id, datasource_name, owner_id, owner_luid, owner_name, owner_username, owner_uri,
                      owner_domain, owner_email, description, created_at, updated_at, has_owner, has_description]

        lenses_rows.append(row_to_add)

    update_hyper(hyper_connection, lenses_rows, lenses_table_definition)


def insert_into_lens_field_tables(hyper_connection, site_id, site_name, lens_field_data, lens_field_table_definition):
    lens_field_rows = []
    for row in lens_field_data:
        asset_id = row.get('id')
        name = row.get('name')
        has_description = False
        description = row.get('description')
        if description != '':
            has_description = True
        datasource_field_id = None
        datasource_field_name = None
        datasource_field_type = None
        if row['datasourceField']:
            datasource_field_id = row['datasourceField'].get('id')
            datasource_field_name = row['datasourceField'].get('name')
            datasource_field_type = row['datasourceField'].get('__typename')
        lens_id = None
        lens_luid = None
        lens_name = None
        if row['containingLens']:
            lens_id = row['containingLens'].get('id')
            lens_luid = row['containingLens'].get('luid')
            lens_name = row['containingLens'].get('name')
        row_to_add = [asset_id, site_id, site_name, name, description, datasource_field_id, datasource_field_name,
                      datasource_field_type, lens_id, lens_luid, lens_name, has_description]

        lens_field_rows.append(row_to_add)

    update_hyper(hyper_connection, lens_field_rows, lens_field_table_definition)


def insert_into_ask_data_extension_tables(hyper_connection, site_id, site_name, ask_data_extension_data,
                                          ask_data_extension_table_definition):
    ask_data_extension_rows = []
    for row in ask_data_extension_data:
        asset_id = row.get('id')
        lens_id = None
        lens_name = None
        lens_luid = None
        if row['lens']:
            lens_id = row['lens'].get('id')
            lens_name = row['lens'].get('name')
            lens_luid = row['lens'].get('luid')
        dashboard_id = None
        dashboard_luid = None
        dashboard_name = None
        if row['dashboard']:
            dashboard_id = row['dashboard'].get('id')
            dashboard_name = row['dashboard'].get('name')
            dashboard_luid = row['dashboard'].get('luid')
        row_to_add = [asset_id, site_id, site_name, lens_id, lens_luid, lens_name, dashboard_id, dashboard_name,
                      dashboard_luid]
        ask_data_extension_rows.append(row_to_add)

    update_hyper(hyper_connection, ask_data_extension_rows, ask_data_extension_table_definition)


def insert_into_datasource_filter_tables(hyper_connection, site_id, site_name, table_data, table_definition):
    datasource_filter_rows = []
    for row in table_data:
        asset_id = row.get('id')
        field_id = None
        field_name = None
        field_type = None
        has_user_reference = None
        formula = None
        if row['field']:
            field_id = row['field'].get('id')
            field_name = row['field'].get('name')
            field_type = row['field'].get('__typename')
            if field_type == 'CalculatedField':
                has_user_reference = False
            if row['field'].get('hasUserReference'):
                has_user_reference = row['field'].get('hasUserReference')
            if row['field'].get('formula'):
                formula = row['field'].get('formula')
        datasource_id = None
        datasource_name = None
        datasource_luid = None
        if row['datasource']:
            datasource_id = row['datasource'].get('id')
            datasource_name = row['datasource'].get('name')
            if row['datasource'].get('luid'):
                datasource_luid = row['datasource'].get('luid')
        row_to_add = [asset_id, site_id, site_name, field_id, field_name, field_type, has_user_reference, formula,
                      datasource_id, datasource_name, datasource_luid]
        datasource_filter_rows.append(row_to_add)

    update_hyper(hyper_connection, datasource_filter_rows, table_definition)


def insert_into_view_stats_tables(hyper_connection, view_stats_data, view_stats_table_definition):
    view_stats_rows = []
    for row in view_stats_data:
        vs_id = row[0]
        number_views = row[1]
        date = row[2]
        device_type = row[3]
        view_luid = row[4]
        view_name = row[5]
        site_luid = row[6]
        site_name = row[7]
        user_luid = row[8]

        row_to_add = [vs_id, number_views, date, device_type, view_luid, view_name, site_luid, site_name, user_luid]
        view_stats_rows.append(row_to_add)

    update_hyper(hyper_connection, view_stats_rows, view_stats_table_definition)


def insert_into_hist_events_tables(hyper_connection, hist_events_data, hist_events_table_definition):
    hist_events_rows = []
    for row in hist_events_data:
        he_id = row[0]
        date = row[1]
        details = row[2]
        duration = row[3]
        worker = row[4]
        is_failure = row[5]
        event_type_id = row[6]
        action_type = row[7]
        action_name = row[8]
        view_id = row[9]
        view_name = row[10]
        view_luid = row[11]
        project_id = row[12]
        project_name = row[13]
        project_luid = row[14]
        workbook_id = row[15]
        workbook_name = row[16]
        workbook_luid = row[17]
        actor_site_id = row[18]
        actor_site_name = row[19]
        actor_site_luid = row[20]
        actor_user_id = row[21]
        actor_user_luid = row[22]
        database_id = row[23]
        database_name = row[24]
        database_luid = row[25]
        datasource_id = row[26]
        datasource_name = row[27]
        datasource_luid = row[28]
        flow_id = row[29]
        flow_name = row[30]
        flow_luid = row[31]
        metric_id = row[32]
        metric_name = row[33]
        metric_luid = row[34]
        table_id = row[35]
        table_name = row[36]
        table_luid = row[37]
        column_id = row[38]
        column_name = row[39]
        column_luid = row[40]
        comment_id = row[41]
        tag_id = row[42]
        target_site_id = row[43]
        target_site_name = row[44]
        target_site_luid = row[45]
        target_user_id = row[46]
        capability_id = row[47]
        collection_id = row[48]
        config_id = row[49]
        data_connection_id = row[50]
        data_quality_indicator_id = row[51]
        data_role_id = row[52]
        flow_draft_id = row[53]
        group_id = row[54]
        licensing_role_id = row[55]
        published_connection_id = row[56]
        remote_agent_id = row[57]
        schedule_id = row[58]
        task_id = row[59]
        collection_luid = row[60]
        collection_name = row[61]

        row_to_add = [he_id, date, details, duration, worker, is_failure, event_type_id, action_type, action_name,
                      view_id, view_name, view_luid, project_id, project_name, project_luid, workbook_id, workbook_name,
                      workbook_luid, actor_site_id, actor_site_name, actor_site_luid, actor_user_id, actor_user_luid,
                      database_id, database_name, database_luid, datasource_id, datasource_name, datasource_luid,
                      flow_id, flow_name, flow_luid, metric_id, metric_name, metric_luid, table_id, table_name,
                      table_luid, column_id, column_name, column_luid, comment_id, tag_id, target_site_id,
                      target_site_name, target_site_luid, target_user_id, capability_id, collection_id, config_id,
                      data_connection_id, data_quality_indicator_id, data_role_id, flow_draft_id, group_id,
                      licensing_role_id, published_connection_id, remote_agent_id, schedule_id, task_id,
                      collection_luid, collection_name]
        hist_events_rows.append(row_to_add)

    update_hyper(hyper_connection, hist_events_rows, hist_events_table_definition)


def insert_into_asset_tables(hyper_connection, tableau_server_url, site_id, site_name, asset_data,
                             asset_table_definition):
    # Insert the results into Hyper
    asset_rows = []
    valid_assets = ["Workbook", "PublishedDatasource", "Flow", "Metric", "Lens", "VirtualConnection"]
    for row in asset_data:
        asset_type = row.get('__typename')
        if asset_type in valid_assets:
            asset_id = row.get('id')
            luid = row.get('luid')
            name = row.get('name')
            asset_uri = None
            if row.get('uri'):
                asset_uri = row.get('uri')
            create_date = None
            if row.get('createdAt'):
                create_date = iso8601.parse_date(row.get('createdAt'))
            update_date = None
            if row.get('updatedAt'):
                update_date = iso8601.parse_date(row.get('updatedAt'))
            project_name = None
            if row.get('projectName'):
                project_name = row.get('projectName')
            container_name = None
            if row.get('containerName'):
                container_name = row.get('containerName')
            container_type = None
            if row.get('containerType'):
                container_type = row.get('containerType')
            description = row.get('description')
            if description == '':
                has_description = False
            else:
                has_description = True
            has_owner = False
            owner_id = None
            owner_luid = None
            owner_name = None
            owner_username = None
            owner_uri = None
            owner_domain = None
            owner_email = None
            if row['owner']:
                has_owner = True
                owner_id = row['owner'].get('id')
                owner_luid = row['owner'].get('luid')
                owner_name = row['owner'].get('name')
                owner_username = row['owner'].get('username')
                owner_domain = row['owner'].get('domain')
                owner_uri = row['owner'].get('uri')
                owner_email = row['owner'].get('email')
            project_id = None
            certified = None
            if row.get('isCertified'):
                certified = row.get('isCertified')

            row_to_add = [asset_id, site_id, site_name, luid, name, asset_type, asset_uri, create_date, update_date,
                          project_name, project_id, container_type, container_name, owner_id, owner_luid, owner_name,
                          owner_username, owner_uri, owner_domain, owner_email, description, certified, has_owner,
                          has_description]

            asset_rows.append(row_to_add)

    update_hyper(hyper_connection, asset_rows, asset_table_definition)


def update_hyper(hyper_connection, table_rows, table_definition):
    # Insert the results into Hyper
    with Inserter(hyper_connection, table_definition) as project_inserter:
        project_inserter.add_rows(table_rows)
        project_inserter.execute()
    project_inserter.close()
    print('{0}Inserted {1} row(s) into the {2} table...{3}'.format(bcolors.OKGREEN, len(table_rows),
                                                                   table_definition.table_name, bcolors.ENDC))
