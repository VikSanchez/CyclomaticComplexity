import git
import os.path
from radon.visitors import ComplexityVisitor
import radon.complexity
import subprocess
import lizard

def get_complexity(f_name):
    result = lizard.analyze_file(f_name)

    cc = result.average_cyclomatic_complexity

    return cc
