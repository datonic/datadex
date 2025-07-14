#!/usr/bin/env python3
"""
Create torrent files for datasets with HuggingFace webseeds
"""
import os
from pathlib import Path
from torf import Torrent
from huggingface_hub import hf_hub_url


def create_torrent_for_dataset(dataset_dir: Path, repo_name: str, filename: str):
    """Create a torrent file for a dataset with HuggingFace webseed"""
    
    # Define the torrent file path
    torrent_path = dataset_dir / f"{dataset_dir.name}.torrent"
    
    # Create the torrent
    torrent = Torrent(
        path=str(dataset_dir),
        name=dataset_dir.name,
        comment=f"Dataset: {dataset_dir.name}. Source: https://github.com/datonic/datadex",
        trackers=[
            "udp://tracker.openbittorrent.com:80",
            "udp://tracker.opentrackr.org:1337",
            "udp://tracker.coppersurfer.tk:6969",
            "udp://exodus.desync.com:6969",
            "udp://tracker.torrent.eu.org:451",
            "udp://tracker.tiny-vps.com:6969",
            "udp://open.stealth.si:80"
        ]
    )
    
    # Add HuggingFace webseed URL for HTTP fallback
    webseed_url = hf_hub_url(repo_id=repo_name, filename=filename, repo_type="dataset")
    torrent.webseeds = [webseed_url]
    
    # Generate the torrent
    torrent.generate()
    
    # Write the torrent file
    with open(torrent_path, 'wb') as f:
        f.write(torrent.dump())
    
    print(f"Created torrent: {torrent_path}")
    print(f"Webseed: {webseed_url}")
    print(f"Size: {torrent.size / 1024 / 1024:.1f} MB")


def main():
    """Create torrents for all datasets"""
    data_dir = Path("data")
    
    # World Development Indicators
    wdi_dir = data_dir / "world_development_indicators"
    if wdi_dir.exists():
        create_torrent_for_dataset(
            wdi_dir, 
            "datonic/world_development_indicators", 
            "world_development_indicators.parquet"
        )
    
    # OWID Indicators
    owid_dir = data_dir / "owid_indicators"
    if owid_dir.exists():
        create_torrent_for_dataset(
            owid_dir,
            "datonic/owid_indicators",
            "owid_indicators.parquet"
        )


if __name__ == "__main__":
    main()