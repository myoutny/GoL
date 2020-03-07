import cProfile, pstats, io
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()
exec(open("GoL.py").read())
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
