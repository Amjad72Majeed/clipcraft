# run_cog.py
import sys
from cog.cli import main

if _name_ == "_main_":
    sys.argv[0] = "cog"
    main()