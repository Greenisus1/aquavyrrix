#!/bin/bash
# pi-app-store: 1
# pi-app-store-category: games
# pi-app-store-description: Original offline water-slide race against three computer rivals; jump shortcuts, curves, falls and1000-distance finish.
set -eu
cd -- "$(dirname -- "$0")"
case "${1:-}" in
 install) python3 -c 'import curses;from pathlib import Path;[compile(p.read_bytes(),str(p),"exec") for p in Path(".").glob("*.py")]';python3 install_commands.py ;;
 uninstall) python3 install_commands.py uninstall ;;
 run) shift;exec python3 aquavyrrix.py "$@" ;;
 *) echo 'Use: bash app-store.sh install|run|uninstall';exit 1 ;;
esac
