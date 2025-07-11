#!/usr/bin/env python3
"""
Create torrent files with HuggingFace webseeds for datadex datasets.
Requires: py3createtorrent
"""

import os
import sys
from pathlib import Path

try:
    import py3createtorrent
except ImportError:
    print("Error: py3createtorrent not found. Please install with: uv add py3createtorrent")
    sys.exit(1)


def create_torrent_with_webseed(file_path, hf_dataset_name, output_dir="torrents"):
    """Create a torrent file with HuggingFace webseed URL."""
    
    file_path = Path(file_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Check if file exists
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return None
    
    # HuggingFace dataset URL pattern
    hf_base_url = f"https://huggingface.co/datasets/datonic/{hf_dataset_name}/resolve/main/"
    webseed_url = f"{hf_base_url}data/{file_path.name}"
    
    # Create torrent
    torrent_path = output_dir / f"{file_path.stem}.torrent"
    
    print(f"📦 Creating torrent for: {file_path.name}")
    print(f"🌐 Webseed URL: {webseed_url}")
    
    try:
        # Create torrent with webseed
        py3createtorrent.create_torrent(
            str(file_path),
            str(torrent_path),
            url_list=[webseed_url],  # Webseed URLs
            comment=f"Dataset: {hf_dataset_name} - Hybrid P2P + HTTP distribution",
            created_by="Datadex",
            private=False
        )
        
        print(f"✅ Created torrent: {torrent_path}")
        return torrent_path
        
    except Exception as e:
        print(f"❌ Error creating torrent: {e}")
        return None


def main():
    """Main function to create torrents for all datasets."""
    
    datasets = [
        ("data/world_development_indicators/world_development_indicators.parquet", "world_development_indicators"),
        ("data/owid_indicators/owid_indicators.parquet", "owid_indicators")
    ]
    
    created_torrents = []
    
    print("🔄 Creating torrents with HuggingFace webseeds...")
    
    for file_path, hf_dataset in datasets:
        if os.path.exists(file_path):
            torrent_path = create_torrent_with_webseed(file_path, hf_dataset)
            if torrent_path:
                created_torrents.append(torrent_path)
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print(f"\n📊 Summary: Created {len(created_torrents)} torrent files")
    
    if created_torrents:
        print("\n🎯 Torrent files created:")
        for torrent in created_torrents:
            print(f"  - {torrent}")
        
        print("\n📘 Usage:")
        print("  - Add torrent files to your BitTorrent client")
        print("  - Share the .torrent files or magnet links")
        print("  - Files will download from HuggingFace if no peers available")
    
    return len(created_torrents)


if __name__ == "__main__":
    main()