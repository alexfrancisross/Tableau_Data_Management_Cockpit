PG_VIEW_STATS_QUERY = 'SELECT vs.id as id, vs.nviews as nviews, vs.time as time, vs.device_type as device_type, ' \
                      'v.luid as view_luid, v.name as view_name, s.luid as site_luid, s.name as site_name, ' \
                      'u.luid as user_luid FROM ((public.views_stats vs inner join views v on v.id = vs.view_id) ' \
                      'inner join sites s on s.id = vs.site_id) inner join users u on u.id = vs.user_id'

PG_HIST_EVENTS_QUERY = "Select he.id, he.created_at, he.details, he.duration_in_ms, he.worker, he.is_failure, " \
                       "he.historical_event_type_id, het.action_type, het.name, " \
                       "he.hist_view_id as view_id, hv.view_name as view_name, hv.view_luid as view_luid, " \
                       "he.hist_project_id as project_id, hp.project_name as project_name, " \
                       "hp.project_luid as project_luid, " \
                       "he.hist_workbook_id as workbook_id, wb.name as workbook_name, wb.luid as workbook_luid, " \
                       "he.hist_actor_site_id AS hist_actor_site_id, a_s.name as hist_actor_site_name, a_s.luid as hist_actor_site_luid, " \
                       "he.hist_actor_user_id as hist_actor_user_id, u.luid as hist_actor_luid, " \
                       "he.hist_database_id AS database_id, v_db.name as database_name, v_db.luid as database_luid, " \
                       "he.hist_datasource_id AS hist_datasource_id, v_ds.name as datasource_name, v_ds.luid as datasouce_luid, " \
                       "he.hist_flow_id AS hist_flow_id, flows.name as flow_name, flows.luid as flow_luid, " \
                       "he.hist_metric_id AS hist_metric_id, metrics.name as metric_name, metrics.luid as metric_luid, " \
                       "he.hist_table_id AS hist_table_id, tables.name as table_name, tables.luid as table_luid, " \
                       "he.hist_column_id AS hist_column_id, columns.name as column_name, columns.luid as column_luid, " \
                       "he.hist_comment_id AS hist_comment_id, he.hist_tag_id AS hist_tag_id, " \
                       "he.hist_target_site_id AS hist_target_site_id, t_s.name as target_site_name, " \
                       "t_s.luid as target_site_luid, he.hist_target_user_id AS hist_target_user_id, " \
                       "he.hist_capability_id AS hist_capability_id,  " \
                       "he.hist_collection_id AS hist_collection_id, he.hist_config_id AS hist_config_id, " \
                       "he.hist_data_connection_id AS hist_data_connection_id, " \
                       "he.hist_data_quality_indicator_id AS hist_data_quality_indicator_id, " \
                       "he.hist_data_role_id AS hist_data_role_id, he.hist_flow_draft_id AS hist_flow_draft_id, " \
                       "he.hist_group_id AS hist_group_id, he.hist_licensing_role_id AS hist_licensing_role_id, " \
                       "he.hist_published_connection_id AS hist_published_connection_id, " \
                       "he.hist_remote_agent_id AS hist_remote_agent_id, he.hist_schedule_id AS hist_schedule_id, " \
                       "he.hist_task_id AS hist_task_id, h_c.collection_luid, h_c.name " \
                       "from ((((((((((((((historical_events he left join historical_event_types het " \
                       "on het.type_id = he.historical_event_type_id) " \
                       "left join (select hist_views.id as id, hist_views.view_id as view_id, " \
                       "hist_views.name as view_name, views.luid as view_luid from hist_views " \
                       "left join views on hist_views.view_id = views.id) hv on he.hist_view_id = hv.id) " \
                       "left join (select hist_projects.id as id, hist_projects.project_id as project_id, " \
                       "hist_projects.name as project_name, projects.luid as project_luid from hist_projects " \
                       "left join projects on hist_projects.project_id = projects.id) hp on he.hist_project_id = hp.id) " \
                       "left join (select hist_workbooks.id as id, hist_workbooks.workbook_id as workbook_id, " \
                       "hist_workbooks.name as name, workbooks.luid as luid from hist_workbooks " \
                       "left join workbooks on hist_workbooks.workbook_id = workbooks.id) wb on he.hist_workbook_id = wb.id) " \
                       "left join (select hist_sites.id as id, hist_sites.site_id as site_id, " \
                       "hist_sites.name as name, sites.luid as luid from hist_sites " \
                       "left join sites on sites.id = hist_sites.site_id) a_s on he.hist_actor_site_id = a_s.id) " \
                       "left join (select hist_users.id as id, hist_users.user_id as user_id, " \
                       "hist_users.name as name, users.luid as luid from hist_users " \
                       "left join users on users.id = hist_users.user_id) u on u.id = he.hist_actor_user_id) " \
                       "left join (select hist_sites.id as id, hist_sites.site_id as site_id, " \
                       "hist_sites.name as name, sites.luid as luid from hist_sites " \
                       "left join sites on sites.id = hist_sites.site_id) t_s on t_s.id = he.hist_target_site_id) " \
                       "left join (select hist_database_assets.id as id, hist_database_assets.database_id as database_id, " \
                       "hist_database_assets.name as name, database_assets.luid as luid from hist_database_assets " \
                       "left join database_assets on database_assets.id = hist_database_assets.database_id) v_db " \
                       "on v_db.id = he.hist_database_id) " \
                       "left join (select hist_ds.id, hist_ds.datasource_id, hist_ds.name, ds.luid " \
                       "from hist_datasources hist_ds left join datasources ds on hist_ds.datasource_id = ds.id) " \
                       "v_ds on v_ds.id = he.hist_datasource_id) " \
                       "left join (select hist_flows.id, hist_flows.flow_id, hist_flows.name, f.luid " \
                       "from hist_flows left join flows f on hist_flows.flow_id = f.id) " \
                       "flows on flows.id = he.hist_flow_id)" \
                       "left join (select hist_metrics.id, hist_metrics.metric_id, hist_metrics.name, m.luid " \
                       "from hist_metrics left join metrics m on hist_metrics.metric_id = m.id) " \
                       "metrics on metrics.id = he.hist_metric_id)" \
                       "left join (select hist_table_assets.id, hist_table_assets.table_id, hist_table_assets.name, t_a.luid " \
                       "from hist_table_assets left join table_assets t_a on hist_table_assets.table_id = t_a.id) " \
                       "tables on tables.id = he.hist_table_id)" \
                       "left join (select hist_column_assets.id, hist_column_assets.column_id, hist_column_assets.name, c_a.luid " \
                       "from hist_column_assets left join column_assets c_a on hist_column_assets.column_id = c_a.id) " \
                       "columns on columns.id = he.hist_column_id) " \
                       "left join hist_collections h_c on h_c.id = he.hist_collection_id)"


def get_repo_queries_and_tables(table_definitions):

    view_stats_dict = {'query': PG_VIEW_STATS_QUERY, 'table': table_definitions.get('View Stats')}
    hist_events_dict = {'query': PG_HIST_EVENTS_QUERY, 'table':  table_definitions.get('Historic Events')}

    queries_and_tables_dict = {'View Stats': view_stats_dict, 'Historic Events': hist_events_dict}

    return queries_and_tables_dict
