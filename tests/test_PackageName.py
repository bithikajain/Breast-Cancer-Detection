import numpy as numpy
import numpy.testing as npt # great for array comparisons 

import PackageName

def test_PackageName_smoke():
    # Smoke test 
    # called so because there is not assert here
    obj = PackageName.DC2object() 

def test_PackageName_fizz():
    # Test the fizz function 
    # called regression test 
    obj = PackageName.DC2object()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")