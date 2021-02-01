from __future__ import absolute_import

__all__ = ['show']
__version__='0.0.1'



def _import_functions(pkgname="inputs",name='read'):
    """Make read functions available at module level.
    Functions are imported here if:
        - they are defined in a module toto.input.{modname}
        - they are named as read_{modname}
    """
    import os
    import sys
    import glob
    from importlib import import_module

    here = os.path.dirname(os.path.abspath(__file__)).replace('\\library.zip','')
    for filename in glob.glob1(os.path.join(here, pkgname), "*.py"):
        module = os.path.splitext(filename)[0]
        if module == "__init__":
            continue
        func_name = "{}_{}".format(name,module)
        try:
            # globals()[func_name] = getattr(
            #     import_module("toto.{}.{}".format(pkgname, module)), func_name
            # )
            import_module("totoview.{}.{}".format(pkgname, module))
        except Exception as exc:
            print("Cannot import {} function {}:\n{}".format(name,func_name, exc))

# defining main function here, 
_import_functions(pkgname="inputs",name='read')
def show(*args,**kwargs):
    from totoview.totoview import showApp
    showApp(*args,**kwargs)