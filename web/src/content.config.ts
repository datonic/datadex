import { DuckDBInstance } from '@duckdb/node-api';
import { defineCollection, z } from 'astro:content';

const countries = defineCollection({
    schema: z.object({
        id: z.string(),
        name: z.string(),
        data: z.any(),
    }),

    loader: async () => {
        const instance = await DuckDBInstance.create("/tmp/datadex.duckdb");
        const connection = await instance.connect();

        await connection.run(`
            create table if not exists world_development_indicators as
            select * from 'https://huggingface.co/datasets/datonic/world_development_indicators/resolve/main/data/world_development_indicators.parquet'
        `);

        const reader = await connection.runAndReadAll(`
            select distinct country_code, country_name
            from world_development_indicators
            where country_code is not null
        `);

        const data = reader.getRows();

        console.log(data);

        return data.map((country: any) => ({
            id: country[0],
            name: country[1]
        }));
    }
});

export const collections = { countries };
