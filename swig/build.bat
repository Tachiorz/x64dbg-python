SET VS90COMNTOOLS=%VS120COMNTOOLS%
swig -outdir x64dbg_python -o x64dbg_python\__x64dbg.cpp -I..\pluginsdk -c++ -cpperraswarn -python -builtin x64dbg.i
%Python27x86%\python setup.py build
swig -DSWIGWORDSIZE64 -outdir x64dbg_python -o x64dbg_python\__x64dbg.cpp -I..\pluginsdk -c++ -cpperraswarn -python -builtin x64dbg.i
%Python27x64%\python setup.py build
