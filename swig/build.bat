SET VS90COMNTOOLS=%VS120COMNTOOLS%
swig -outdir x64dbg_python -o x64dbg_python\__x64dbg.cpp -I..\pluginsdk -c++ -cpperraswarn -python -builtin x64dbg.i
python setup.py build