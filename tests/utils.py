import uproot


def create_ntuple(fname, treename, varname, var_array, weightname, weight_array):
    with uproot.recreate(fname) as f:
        f[treename] = uproot.newtree({varname: "float64", weightname: "float64"})
        f[treename].extend({varname: var_array, weightname: weight_array})