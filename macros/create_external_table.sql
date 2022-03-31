{% macro duckdb__create_external_table(source_node) %}

    {%- set external = source_node.external -%}

    install 'httpfs';
    load 'httpfs';
    CREATE OR REPLACE VIEW {{source(source_node.source_name, source_node.name).include(database=False)}} AS
    (
        SELECT * FROM '{{external.location}}'
    )
{% endmacro %}
