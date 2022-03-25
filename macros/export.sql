
{% macro export() %}
    export database 'target_directory' (format parquet);
{% endmacro %}