# aquavyrrix1.0.0

Original offline water-slide race against three computer rivals; jump shortcuts, curves, falls and1000-distance finish.

Fullscreen terminal, original Unicode/color block art. No accounts, ads, network, purchases, branded game assets, saved progress or desktop. Small first release, not feature parity with its commercial inspiration. Controls printed on screen. Space/P pauses, R resets, Esc/q exits. Python3+curses only; no pip downloads needed. Missing Python/curses stops with a clear error rather than silently running apt as root. Install checks dependencies, compiles source and creates this user's case-insensitive command variants in ~/.local/bin, without sudo. It refuses unrelated command overwrites; uninstall removes only owned links. If ~/.local/bin is not on PATH, installer prints a warning; no profile edits.

    bash app-store.sh install
    bash app-store.sh run
    aquavyrrix
    AQUAVYRRIX
    python3 aquavyrrix.py --version
    python3 -m unittest -v
    bash app-store.sh uninstall

Game drawing scales with terminal. Resize too small pauses simulation; restore to continue. State disappears on exit. Linux core tests and fullscreen PTY interaction/resize/clean-exit/restoration inspected; physical Raspberry Pi and non-Linux untested. MIT license. No Pi packages or real device settings changed during testing.
