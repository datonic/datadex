---
title: API
emoji: 📊
colorFrom: black
colorTo: yellow
sdk: docker
pinned: false
license: mit
app_port: 8084
---

# DatonicAPI

A simple API built with [RoAPI](https://github.com/roapi/roapi) to serve the datasets that are available in the [Datonic's Hugging Face Organization](https://huggingface.co/datonic).

The API is available at `https://datonic-api.hf.space`.

```bash
curl -X POST -d "select * from world_development_indicators limit 10" https://datonic-api.hf.space/api/sql
```
