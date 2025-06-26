#!/usr/bin/env python3
"""
Simple script to run Pelican commands without needing 'make'.
Usage: python run.py [build|serve|dev|publish|clean]
"""

import subprocess
import sys
import os
import shutil

def run_command(cmd, description):
    """Run a command and handle errors gracefully."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"Command: {' '.join(cmd)}")
        print(f"Error: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"❌ Error: 'pelican' command not found.")
        print("Make sure you have installed the requirements:")
        print("  pip install -r requirements-simple.txt")
        return False

def clean_output():
    """Remove the output directory."""
    output_dir = "output"
    if os.path.exists(output_dir):
        print(f"🧹 Cleaning {output_dir} directory...")
        try:
            shutil.rmtree(output_dir)
            print(f"✅ {output_dir} directory removed!")
            return True
        except Exception as e:
            print(f"❌ Error removing {output_dir}: {e}")
            return False
    else:
        print(f"ℹ️  {output_dir} directory doesn't exist.")
        return True

def main():
    if len(sys.argv) < 2:
        print("🚀 Pelican Blog Runner")
        print("=" * 30)
        print("Usage: python run.py [command]")
        print("\nAvailable commands:")
        print("  build    - Build the site for development")
        print("  serve    - Serve the site locally (no auto-reload)")
        print("  dev      - Serve with auto-reload (development mode)")
        print("  publish  - Build for production")
        print("  clean    - Remove the output directory")
        print("\nExamples:")
        print("  python run.py build")
        print("  python run.py dev")
        return
    
    command = sys.argv[1].lower()
    
    if command == "build":
        success = run_command(
            ["python", "-m", "pelican", "content", "-o", "output", "-s", "pelicanconf.py"],
            "Building site for development"
        )
        if success:
            print("\n📁 Site built! Check the 'output' directory.")
            
    elif command == "serve":
        print("🌐 Starting local server...")
        print("📱 Your site will be available at: http://localhost:8000")
        print("⏹️  Press Ctrl+C to stop the server")
        try:
            subprocess.run(["python", "-m", "pelican", "-l", "content", "-o", "output", "-s", "pelicanconf.py"])
        except KeyboardInterrupt:
            print("\n👋 Server stopped.")
            
    elif command == "dev":
        print("🚀 Starting development server with auto-reload...")
        print("📱 Your site will be available at: http://localhost:8000")
        print("🔄 The site will automatically reload when you make changes")
        print("⏹️  Press Ctrl+C to stop the server")
        try:
            subprocess.run(["python", "-m", "pelican", "-lr", "content", "-o", "output", "-s", "pelicanconf.py"])
        except KeyboardInterrupt:
            print("\n👋 Development server stopped.")
            
    elif command == "publish":
        success = run_command(
            ["python", "-m", "pelican", "content", "-o", "output", "-s", "publishconf.py"],
            "Building site for production"
        )
        if success:
            print("\n📁 Production site built! Check the 'output' directory.")
            print("🚀 Ready for deployment!")
            
    elif command == "clean":
        clean_output()
        
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: build, serve, dev, publish, clean")

if __name__ == "__main__":
    main() 