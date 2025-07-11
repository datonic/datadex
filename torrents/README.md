# Datadex Torrents

This directory contains torrent files for Datadex datasets, providing hybrid P2P + HTTP distribution.

## Available Torrents

- `world_development_indicators.torrent` - World Development Indicators dataset
- `owid_indicators.torrent` - Our World in Data indicators dataset

## Features

- **Hybrid Distribution**: Torrents include webseeds pointing to HuggingFace datasets
- **Fallback Support**: Downloads from HuggingFace if no peers available
- **Webseed URLs**: Direct HTTP access to dataset files
- **Distributed Bandwidth**: Reduces server load through P2P sharing

## Usage

### Using BitTorrent Clients

1. **Add torrent file** to your BitTorrent client (qBittorrent, Transmission, etc.)
2. **Start download** - will use both P2P peers and HTTP webseeds
3. **Share back** - seed the file to help others download

### Webseed URLs

If you prefer direct HTTP access, torrents include webseed URLs:

- World Development Indicators: `https://huggingface.co/datasets/datonic/world_development_indicators/resolve/main/data/world_development_indicators.parquet`
- OWID Indicators: `https://huggingface.co/datasets/datonic/owid_indicators/resolve/main/data/owid_indicators.parquet`

## Creating Torrents

Torrents are automatically generated when running:

```bash
make torrents
```

This will:
1. Generate dataset files if needed
2. Create torrent files with HuggingFace webseeds
3. Place torrent files in this directory

## Technical Details

- **Protocol**: BitTorrent with BEP 19 webseed support
- **Webseeds**: HuggingFace dataset URLs as HTTP fallback
- **Created by**: Datadex torrent generation script
- **Comment**: Includes dataset name and distribution type

## Benefits

- **Reduced bandwidth costs** for dataset hosting
- **Improved download speeds** through distributed peers
- **Reliable fallback** via HuggingFace HTTP servers
- **Academic sharing** following open data principles