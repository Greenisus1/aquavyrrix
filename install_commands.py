import itertools,os,pathlib,shlex,sys
NAME='aquavyrrix'
ROOT=pathlib.Path(__file__).resolve().parent
BIN=pathlib.Path.home()/'.local/bin'
TARGET=BIN/('.'+NAME+'-launcher')
CONTENT='#!/bin/sh\n# owned-by-'+NAME+'\nexec python3 '+shlex.quote(str(ROOT/(NAME+'.py')))+' "$@"\n'
def aliases(name):return [''.join(x) for x in itertools.product(*[(c.lower(),c.upper()) if c.isalpha() else (c,) for c in name])]
def install():
 BIN.mkdir(parents=True,exist_ok=True);names=aliases(NAME)
 if TARGET.is_symlink():raise RuntimeError('Refusing launcher symlink')
 if TARGET.exists() and not TARGET.read_text().startswith('#!/bin/sh\n# owned-by-'+NAME+'\n'):raise RuntimeError('Refusing unrelated launcher overwrite')
 for name in names:
  p=BIN/name
  if p.exists() or p.is_symlink():
   if not p.is_symlink() or os.readlink(p)!=str(TARGET):raise RuntimeError('Refusing existing command '+name)
 TARGET.write_text(CONTENT);TARGET.chmod(0o700)
 for name in names:
  p=BIN/name
  if not p.is_symlink():p.symlink_to(TARGET)
 print('Installed',len(names),'case variants in',BIN)
 if str(BIN) not in os.environ.get('PATH','').split(os.pathsep):print('Add ~/.local/bin to PATH to use commands, or use bash app-store.sh run.')
def uninstall():
 for name in aliases(NAME):
  p=BIN/name
  if p.is_symlink() and os.readlink(p)==str(TARGET):p.unlink()
 if TARGET.exists() and TARGET.read_text()==CONTENT:TARGET.unlink()
if __name__=='__main__':
 try:uninstall() if sys.argv[1:] == ['uninstall'] else install()
 except (OSError,RuntimeError) as e:print(e);raise SystemExit(1)
